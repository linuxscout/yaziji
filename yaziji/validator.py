import logging

from libqutrub.verb_const import TenseImperative,  TensePast, TensePassivePast, TenseFuture
from libqutrub.verb_const import  ImperativePronouns, PronounsTable


# Local libraries

from yaziji_const import VERBAL_PHRASE, NOMINAL_PHRASE
from yaziji_const import ACTIVE_VOICE, PASSIVE_VOICE, AFFIRMATIVE, NEGATIVE

from components_set import componentsSet
from error_listener import ErrorListener, INFO_CONST, WARNING_CONST
# from yaziji.phrase_generator import PhraseGenerator
class Validator:
    def __init__(self, dictionary=None, error_observer:ErrorListener=None):
        """
        Initialize the Validator class with a rules base.
        """
        self.components_config = componentsSet()
        self.error_observer = error_observer
        self.rules_base = {}

        self.notes = []
        self.dictionary = dictionary
        self.debug = False

    def set_ddebug(self,debug):
        """
        Set debug flag
        :param debug:
        :return:
        """
        self.debug = bool(debug)

    def notify(self, error_id, message_id, args, type="error"):
        """
        Nofify error or info
        :param type:
        :param error_id:
        :param message_id:
        :param args:
        :return:
        """
        # get error message from observer
        if self.error_observer:
            error_message = self.error_observer.error_message(message_id)
            formatted_message = f"{error_message}".format_map(args)
            self.error_observer.notify(message_id, formatted_message, type=type)
        else:
             formatted_message = message_id + str(args)
             logging.info(f"{type.upper()} #{error_id}: {formatted_message}")
        return True

    def add_note(self, note: str, args:dict= {}) -> None:
        """
        add a note to signal an error
        :param note:
        :return:
        """
        self.notes.append(note)
        self.notify(-15, note, args)

    def add_note_info(self, note: str, args:dict= {}) -> None:
        """
        add a note to signal an error
        :param note:
        :return:
        """
        self.notes.append("INFO:"+note)
        self.notify(-15, note, args, type=INFO_CONST)

    def get_note(self)-> str:
        """
        Return the last note
        :return:
        """
        return self.notes[-1] if  self.notes else ""

    def check_verb_object_relationship(self, verb, obj):
        """
        Check the compatibility between a verb and its object.
        :param verb: The verb to check.
        :param obj: The object to check.
        :return: True (placeholder logic).
        """
        return True

    def check_verb_subject_relationship(self, verb, subject):
        """
        Check the compatibility between a verb and its subject.
        :param verb: The verb to check.
        :param subject: The subject to check.
        :return: True (placeholder logic).
        """
        return True

    def check_sufficient_components(self, components):
        """
        Check if the sentence contains sufficient components (subject, verb, object, etc.).
        :param components: The sentence to check.
        :return: True (placeholder logic).
        """
        # many case to be a valid sentence
        # else False
        # a mimimal verb subject
        """
        تكون الجملة مفيدة فيما يلي:
        - فعل فاعل
        فعل مفعول به وزمن مبني للمجهول لا يكون أمرًا
        فالع/مبتدأ خبر (صفة)
        مبتدأ مكان
        
        الحالات المانعة
        جملة اسمية بلا اسم (مبتدأ أو مفعول به)
        جملة فعلية بلا فعل
        مبني للمجهول بلا نائب فاعل
        أمر بلا ضمير مخاطب
        فعل مبني للمعلوم بلا فاعل  مثال: فعل: ضرب، فاعل: ""
        """

        verb = components.get("verb",'')
        subject = components.get("subject",'')
        object = components.get("object",'')
        place = components.get("place",'')
        predicate = components.get("adjective",'')
        active_voice = True if components.get("voice",'') == ACTIVE_VOICE else False
        passive_voice = True if components.get("voice",'') == PASSIVE_VOICE else False
        imperative  = True if components.get("tense",'') == TenseImperative else False
        verbal  = True if components.get("phrase_type",'') == VERBAL_PHRASE else False
        nominal  = True if components.get("phrase_type",'') == NOMINAL_PHRASE else False

        # verbal phrase without verb, return false
        if verbal and not verb:
            self.add_note("VERBAL_PHRASE_NO_VERB")
            # self.add_note("INVALID: a verbal phrase witheout verb")
            return False

        # nominal phrase without subject, or no subject, but object, within passive voice and verb
        if nominal and not subject and not object:
            # self.add_note("INVALID: a nominal phrase witheout noun")
            self.add_note("NOMINAL_PHRASE_NO_NOUN")
            return False


        # verb without subject neiter object
        if verb and not subject and not object:
            self.add_note("VERB_NO_SUB_NO_OBJ")
            # self.add_note("INVALID: Verb without subject or object")
            return False


        # subject not imperative pronoun and tense is pronoun
        if not subject.startswith("أنت") and imperative:
            # self.add_note(")
            # self.add_note("INVALID: Incompatible Subject with Imperative tense")
            self.add_note("INCOMPATIBLE_SUBJECT_TENSE", {"subject":subject,"tense":TenseImperative})
            return False

        # active voice with no subject
        if not subject and  active_voice:
            # self.add_note("INVALID: Active voice but no subject")
            self.add_note("ACTIVE_VOICE_NO_SUB")
            return False

        # if the fphrase contain the
        # a mimimal verb subject
        if verb and subject:
            self.add_note_info("VALID COMPONENTS_VERB_SUBJ", {"verb":verb, "subject":subject})
            return True
        # a mimimal subject place, can form a nominal phrase أحمد في السوق
        if subject and place:
            self.add_note_info("VALID COMPONENTS_SUBJ_PLACE",{"place":place, "subject":subject} )
            return True
        if subject and predicate:
            # self.add_note_info("VALID: Subject + APredicate")
            self.add_note_info("VALID COMPONENTS_SUBJ_PREDICATE",{"predicate":predicate, "subject":subject} )
            return True

        # a mimimal no subject, verb objectwith passive voice
        # print("subject;", subject, "verb:", verb, "object",object, "imperative",imperative, "passive_voice",passive_voice)
        if not subject and verb and object and not imperative and passive_voice:
            # self.add_note("VALID: verb + Object + Passive voice")
            self.add_note_info("VALID COMPONENTS_VERB_OBJ_PASSIVE",{"verb":verb, "object":object})
            return True

        self.add_note("INSUFFICIENT_COMPONENTS")
        # self.add_note("INVALID: Insufficient components to build a phrase")
        return False


    def check_features(self, features):
        """
        Check if the the given features are compatible.
        :param subject: The subject to check.
        :param voice: The voice to check.
        :return: True (placeholder logic).
        """
        active_voice = True if features.get("voice",'') == ACTIVE_VOICE else False
        passive_voice = True if features.get("voice",'') == PASSIVE_VOICE else False
        imperative  = True if features.get("tense_verb",'') == TenseImperative else False
        # verbal  = True if components.get("phrase_type",'') == VERBAL_PHRASE else False
        pronoun = features.get("pronoun_verb","")
        transitive = True if features.get("transitive",True) else False
        intransitive = False if features.get("transitive",True) else True
        verb   = True if features.get("has_verb", "") else False
        object = True if features.get("has_object", "") else False

        # INVALID: a intransitive verb with Passive voice
        if verb and intransitive and  passive_voice:
            # self.add_note("INVALID: a intransitive verb with Passive voice")
            self.add_note("INTRANS_VERB_PASSIVE_VOICE")
            return False

        # INVALID: a intransitive verb with Object
        if verb and intransitive and  object:
            self.add_note("INTRANS_VERB_WITH_OBJ")
            # self.add_note("INVALID: a intransitive verb with Object")
            return False
        # INVALID: a transitive verb without Object
        if verb and transitive and  not object:
            self.add_note("TRANS_VERB_NO_OBJ")
            return False

        # INVALID: imperative and not pronoun in ImperativePronouns
        if verb and imperative and not pronoun in ImperativePronouns and  not object:
            self.add_note("INCOMPATIBLE_SUBJECT_TENSE")
            return False

        self.add_note_info("NO_FREATURES_ISSUE")
        return True

    def is_required(self, name):
        """
        test if the name is required ins etting
        :param name:
        :return:
        """
        return self.components_config.is_required(name)

    def check_required_components(self, components):
        """
        Check the  required components in the input components
        :param components: The object to check.
        :return: True (placeholder logic).
        """
        # check if a required name is not found
        for name in self.components_config.nodes_config:
            if self.is_required(name) and not components.get(name, ""):
                self.add_note("REQUIRED_NAME", {"name": name})
                return False
        return True

    def check_unsupported_components(self, components):
        """
        Check the  unsupported components in the input components
        :param names:
        :param features:
        :param components: The object to check.
        :return: True (placeholder logic).
        """
        # check if a required name is not found
        for key in components:
            if not self.components_config.is_supported(key):
                self.add_note("UNSUPPORTED_COMPONENT", {"name":key})
                return False
        return True


    def check_semantic(self, components):
        """
        Check the compatible relaton ship between words.
        :param components: The object to check.
        :return: True (placeholder logic).
        """
        verb = components.get("verb",'')
        subject = components.get("subject",'')
        object = components.get("object",'')
        place = components.get("place",'')
        predicate = components.get("adjective",'')

        if not self.check_verb_subject_relationship(verb, subject):
            self.add_note("SEM_INCOMP_VERB_SUBJ",{"verb":verb, "subject":subject})
            return False
        if not self.check_verb_object_relationship(verb, object):
            self.add_note("SEM_INCOMP_VERB_OBJ",{"verb":verb, "object":object})
            return False

        self.add_note_info("NO_SEMANTIC_ISSUE")
        return True
    # def check_verb_voice_compatible(self, verb, voice):
    #     """
    #     Check if the verb is compatible with the given voice
    #     :param verb: The verb to check.
    #     :param voice: The tense to check.
    #     :return: True (placeholder logic).
    #     """
    #     return True

    def check_adverb_tense_compatible(self, adverb, tense):
        """
        Check if the adverb is compatible with the given tense.
        :param adverb: The adverb to check.
        :param tense: The tense to check.
        :return: True (placeholder logic).
        """
        return True


    # def check_object_voice_compatible(self, obj, voice):
    #     """
    #     Check if the object is compatible with the given voice (active/passive).
    #     :param obj: The object to check.
    #     :param voice: The voice to check.
    #     :return: True (placeholder logic).
    #     """
    #     return True

    # def check_subject_voice_compatible(self, subject, voice):
    #     """
    #     Check if the subject is compatible with the given voice (active/passive).
    #     :param subject: The subject to check.
    #     :param voice: The voice to check.
    #     :return: True (placeholder logic).
    #     """
    #     return True

    def check(self, **args):
        """
        Check if the subject is compatible with the given voice (active/passive).
        :param subject: The subject to check.
        :param voice: The voice to check.
        :return: True (placeholder logic).
        """
        return True

