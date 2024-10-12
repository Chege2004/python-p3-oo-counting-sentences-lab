class MyString:
    def __init__(self, value=""):
        self._value = ""
        self.value = value  # This will use the setter for validation

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        import re
        # This regex splits the string by ".", "?", or "!" and ensures non-empty strings are counted
        sentences = re.split(r'[.!?]+', self.value.strip())
        # Filter out empty strings and count non-empty parts
        return len([s for s in sentences if s.strip()])
