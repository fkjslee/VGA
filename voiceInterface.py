from abc import ABC, abstractmethod


class VoiceInterface(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def add_sentence(self, sentence):
        pass

    @abstractmethod
    def delete_sentence(self):
        pass

    @abstractmethod
    def modify_sentence(self, old_word, new_word):
        pass


class Voice(VoiceInterface):

    def modify_sentence(self, old_word=None, new_word=None):
        with open("article.txt", "r", encoding="utf-8") as f:
            content = f.readlines()
        if len(content) == 0:
            return {"status": "error", "code": "no previous sentence to modify"}
        pre_sentence = content[-1]
        if old_word is None and new_word is None:
            return {"status": "error", "code": "nothing to modify"}
        elif old_word is None:  # add word
            pre_sentence += new_word
            content[-1] = pre_sentence
        else:  # modify sentence
            if pre_sentence.find(old_word) == -1:
                return {"status": "error", "code": "fail to find {}".format(new_word)}
            new_word = "" if new_word is None else new_word
            pre_sentence.replace(old_word, new_word)
        with open("article.txt", "w+", encoding="utf-8") as f:
            f.writelines(content)
            f.write(sentence + "\n")
        return {"status": "success"}


    def add_sentence(self, sentence):
        with open("article.txt", "r", encoding="utf-8") as f:
            content = f.readlines()
        with open("article.txt", "w+", encoding="utf-8") as f:
            f.writelines(content)
            f.write(sentence + "\n")
        return {"status": "success"}

    def delete_sentence(self):
        with open("article.txt", "r", encoding="utf-8") as f:
            content = f.readlines()
        if len(content) == 0:
            return {"status": "error", "code": "no previous sentence to modify"}
        with open("article.txt", "w+", encoding="utf-8") as f:
            f.writelines(content[0:-1])
            return {"status": "success"}

