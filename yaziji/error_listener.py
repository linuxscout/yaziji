# Error listener class to handle errors
ERROR_MESSAGES = {
    "UNKNOWN_ERROR": "Error not defined",
    -2: "A required name not found.",
    -3: "Unsupported component key.",
    -4: "ERROR: Required Phrase type is empty.",
    "REQUIRED_NAME":       "ERROR: A required name '{name}' not found.",
    "EMPTY_PHRASE_TYPE":   "ERROR: Required Phrase type is empty.",
    "UNSUPPORTED_COMPONENT":     "ERROR: Unsupported component key '{name}'.",
    "INCOMPATIBLE_SUBJECT_TENSE":"ERROR: Incompatible Subject '{subject}' and tense '{tense}'.",
    "VERBAL_PHRASE_NO_VERB":  "INVALID: a verbal phrase witheout verb.",
    "NOMINAL_PHRASE_NO_NOUN": "INVALID: a nominal phrase witheout noun.",
    "VERB_NO_SUB_NO_OBJ":     "INVALID: Verb without subject or object.",
    "ACTIVE_VOICE_NO_SUB":    "INVALID: Active voice but no subject.",
    "INSUFFICIENT_COMPONENTS": "INVALID: Insufficient components to build a phrase.",
    "INTRANS_VERB_PASSIVE_VOICE": "INVALID: a intransitive verb  with Passive voice.",
    "INTRANS_VERB_WITH_OBJ":   "INVALID: a intransitive verb with Object.",
    "TRANS_VERB_NO_OBJ":       "INVALID: a transitive verb  without Object.",
    "SEM_INCOMP_VERB_SUBJ":    "Semantic: incomatibility between verb '{verb}' and subject '{subject}'. ",
    "SEM_INCOMP_VERB_OBJ":     "INVALID: Semantic incomatibility between verb '{verb}' and object '{object}'. ",
    "VALIDATOR_NOT_INITIALIZED": "ERORR: The Validator instance is not set in PhrasePattern object ",
# }
#
# INFO_MESSAGES= {
	"NO_FREATURES_ISSUE":"VALID: No features issue found",
	"VALID COMPONENTS_VERB_SUBJ": "VALID:verb '{verb}' + subject '{subject}'",
 	"VALID COMPONENTS_SUBJ_PLACE":"VALID: Subject '{subject}' + place '{place}'",
	"VALID COMPONENTS_SUBJ_PREDICATE": "VALID: Subject '{subject}' + Predicate '{predicate}'",
	"VALID COMPONENTS_VERB_OBJ_PASSIVE":"VALID: verb '{verb}' + Object '{object}'+ Passive voice",
    "NO_SEMANTIC_ISSUE":"VALID: No semantic issues found"
}

INFO_CONST = "info"
WARNING_CONST = "warning"
ERROR_CONST = "error"
class ErrorListener:
    def __init__(self,):
        pass
        self.error_list = []
        self.info_list = []
        self.warning_list = []

    def notify_error(self, errorno, error_message, type='error'):
        """
        store errors
        :param error_message:
        :return:
        """
        if not error_message:
            error_message =  self.error_message(errorno)
        msg = f"{type.capitalize()} received {errorno}: {error_message}"
        if type == INFO_CONST:
            self.error_list.append(msg)
        elif type == WARNING_CONST:
            self.warning_list.append(msg)
        else:
            self.error_list.append(msg)
        return msg

    def notify(self, errorno, error_message, type='error'):
        """
        store errors
        :param error_message:
        :return:
        """
        if not error_message:
            error_message =  self.error_message(errorno)
        msg = f"{type.capitalize()} received {errorno}: {error_message}"
        if type == INFO_CONST:
            self.info_list.append(msg)
        elif type == WARNING_CONST:
            self.warning_list.append(msg)
        else:
            self.error_list.append(msg)
        return msg


    def notify_error(self, errorno, error_message):
        """
        store errors
        :param error_message:
        :return:
        """
        return self.notify(errorno, error_message, type="error")


    def error_message(self, errorno):

        return ERROR_MESSAGES.get(errorno, "Input Error")

    def show_errors(self):
        """
        show errors
        :return:
        """
        return self.error_list

    def show_errors_to_string(self):
        """
        show errors
        :return:
        """
        return ";".join(self.error_list)


    def show_infos(self):
        """
        show infos
        :return:
        """
        return self.info_list

    def show_infos_to_string(self):
        """
        show infos
        :return:
        """
        return ";".join(self.info_list)

    def show_warnings(self):
        """
        show warnings
        :return:
        """
        return self.warning_list

    def show_warnings_to_string(self):
        """
        show warnings
        :return:
        """
        return ";".join(self.warning_list)
    @staticmethod
    def get_errorno(message_id):
        """
        Return a numeric value for error message key
        :param message_id:
        :return:
        """
        # lookup for key
        key = message_id
        if key in ERROR_MESSAGES:
            errorno = list(ERROR_MESSAGES.keys()).index(key) + 1
            # print(errorno)
            return errorno
        return 0


    def reset(self):
        """
        reset error list
        :return:
        """
        self.error_list = []
