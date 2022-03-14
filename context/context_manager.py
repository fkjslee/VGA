class ContextManager:
    # status include None, add sentence, modify sentence, delete sentence
    pre_status = None
    pre_sentence = None

    def modify_pre_sentence(self, kwargs, method):
        assert method in ["replace", "delete", "append"], "Error! not implement {} yet.".format(method)

        def replace_sentence(pre_sentence: src_word, dst_word):
            return pre_sentence.replace(src_word, dst_word)

        if method == "replace":
            replace_sentence(**kwargs)
        elif method == "delete":
            replace_sentence(**kwargs)
        elif method == "append":
            replace_sentence(**kwargs)
        self.pre_status = "modify"

    def add_sentence(self, sentence):
        self.pre_status = "add"
        self.pre_sentence = sentence

    def delete_sentence(self):
        self.pre_status = "delete"
        self.pre_sentence = None
