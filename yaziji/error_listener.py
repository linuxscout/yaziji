# Error listener class to handle errors
ERROR_MESSAGES = {
    -1: "Imperative Tense Incompatible with pronoun.",
    -2: "A required name not found.",
    -3: "Unsupported component key.",
    -4: "ERROR: Required Phrase type is empty.",
    "REQUIRED_NAME": "ERROR: A required name '{name}' not found.",
    "EMPTY_PHRASE_TYPE": "ERROR: Required Phrase type is empty.",
    "UNSUPPORTED_COMPONENT":"ERROR: Unsupported component key '{name}'.",
    "INCOMPATIBLE_SUBJECT_TENSE":"ERROR: Incompatible Subject {subject} and tense '{tense}'.",
}

class ErrorListener:
    def __init__(self,):
        pass
        self.error_list = []
    def notify_error(self, errorno, error_message):
        """
        store errors
        :param error_message:
        :return:
        """
        if not error_message:
            error_message =  self.error_message(errorno)

        self.error_list.append(f"Error received {errorno}: {error_message}")
        return error_message

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

    def reset(self):
        """
        reset error list
        :return:
        """
        self.error_list = []
