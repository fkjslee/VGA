import time
from voiceInterface import Voice
import sys
sys.path.append("./network")
from network import Server
import time
import json


if __name__ == "__main__":
    voice_command = Voice()
    while True:
        try:
            result = Server.receive_msg()
            result = json.loads(result)
            intent = result['intent']
            if intent == "add_sentence":
                sentence = result['sentence']
                rtn_msg = voice_command.add_sentence(sentence)
            elif intent == "delete_sentence":
                rtn_msg = voice_command.delete_sentence()
            elif intent == "modify":
                rtn_msg = voice_command.modify_sentence(result.get("S-wrong-word"), result.get("S-right-word"))
            else:
                print("error command!")
                continue
            print(rtn_msg)
        except Exception as e:
            print(e)
