from libqutrub.verb_const import TenseImperative,  TensePast, TensePassivePast, TenseFuture
from libqutrub.verb_const import  ImperativePronouns, PronounsTable


# Local libraries

from yaziji_const import VERBAL_PHRASE, NOMINAL_PHRASE
from yaziji_const import ACTIVE_VOICE, PASSIVE_VOICE, AFFIRMATIVE, NEGATIVE


# from yaziji.phrase_generator import PhraseGenerator
class Validator:
    def __init__(self, dictionary=None):
        """
        Initialize the Validator class with a rules base.
        """
        self.rules_base = {}
        self.notes = []
        self.dictionary = dictionary

    def add_note(self, note: str) -> None:
        """
        add a note to signal an error
        :param note:
        :return:
        """
        self.notes.append(note)
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
            self.add_note("INVALID: a verbal phrase witheout verb")
            return False

        # nominal phrase without subject, or no subject, but object, within passive voice and verb
        if nominal and not subject and not object:
            self.add_note("INVALID: a nominal phrase witheout noun")
            return False


        # verb without subject neiter object
        if verb and not subject and not object:
            self.add_note("INVALID: Verb without subject or object")
            return False


        # subject not imperative pronoun and tense is pronoun
        if not subject.startswith("أنت") and imperative:
            self.add_note("INVALID: Incompatible Subject with Imperative tense")
            #     self.notify_error_id(-1, "INCOMPATIBLE_SUBJECT_TENSE", {"subject":subject,"tense":tense})
            return False

        # active voice with no subject
        if not subject and  active_voice:
            self.add_note("INVALID: Active voice but no subject")
            return False

        # if the fphrase contain the
        # a mimimal verb subject
        if verb and subject:
            self.add_note("VALID: verb + subject")
            return True
        # a mimimal subject place, can form a nominal phrase أحمد في السوق
        if subject and place:
            self.add_note("VALID: Subject + place")
            return True
        if subject and predicate:
            self.add_note("VALID: Subject + APredicate")
            return True

        # a mimimal no subject, verb objectwith passive voice
        print("subject;", subject, "verb:", verb, "object",object, "imperative",imperative, "passive_voice",passive_voice)
        if not subject and verb and object and not imperative and passive_voice:
            self.add_note("VALID: verb + Object + Passive voice")
            return True

        self.add_note("INVALID: Insufficient components to build a phrase")
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
            self.add_note("INVALID: a intransitive verb with Passive voice")
            return False

        # INVALID: a intransitive verb with Object
        if verb and intransitive and  object:
            self.add_note("INVALID: a intransitive verb with Object")
            return False
        # INVALID: a transitive verb without Object
        if verb and transitive and  not object:
            self.add_note("INVALID: a transitive verb without Object")
            return False

        # INVALID: imperative and not pronoun in ImperativePronouns
        if verb and imperative and not pronoun in ImperativePronouns and  not object:
            self.add_note("INVALID: Imperative tense with imcompatible pronoun")
            return False

        self.add_note("VALID: No features incompatibility")
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
            self.add_note("INVALID: Semantic incomatibility between verb '{verb}' and subject '{subject}'. ")
            return False
        if not self.check_verb_object_relationship(verb, object):
            self.add_note("INVALID: Semantic incomatibility between verb '{verb}' and object '{object}'. ")
            return False

        self.add_note("VALID: No features incompatibility")
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

