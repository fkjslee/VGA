from abc import ABC, abstractmethod
import time


class VoiceInterface(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def add_sentence(self, sentence):
        pass

    @abstractmethod
    def delete_sentence(self):
        pass


class Voice(VoiceInterface):

    def add_sentence(self, sentence):
        with open("article.txt", "r", encoding="utf-8") as f:
            content = f.readlines()
        with open("article.txt", "w+", encoding="utf-8") as f:
            content.append(sentence)
            f.writelines(content)

    def delete_sentence(self):
        with open("article.txt", "r", encoding="utf-8") as f:
            content = f.readlines()
        with open("article.txt", "w+", encoding="utf-8") as f:
            f.writelines(content[0:-1])



# if __name__ == "__main__":
#     client = Client()
#     while True:
#         return_msg = client.sendMsg("nothing")
#         print(return_msg)


import sys
sys.path.append("./network")
from network import Server
import time

voice_command = Voice()
while True:
    try:
        result = Server.receive_msg()
        import json
        result = json.loads(result)
        intent = result['intent']
        if intent == "add_sentence" or intent == "delete_sentence":
            sentence = result['sentence']
            voice_command.add_sentence(sentence)
            print("intent = ", intent)
            print("sentence = ", sentence)
    except Exception as e:
        print(e)
