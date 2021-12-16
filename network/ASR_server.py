import os
import sys
import socket
sys.path.append(os.path.join(os.path.dirname(__file__), '../python'))

import VoiceCommand.ASRCommand
import VoiceCommand.VoiceOperationCommand
import VoiceCommand.UnionCommand

x = []
print(x.append(123))

class Server:
    @classmethod
    def receive_msg(cls, ip="127.0.0.1", port=9001):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((ip, port))
        server_socket.listen(2)
        conn, addr = server_socket.accept()

        buffer = conn.recv(1024)
        conn.close()
        server_socket.close()

        vc = VoiceCommand.ASRCommand.ASRCommand.GetRootAs(buffer)

        assert vc.Name() == b'command'
        assert vc.CommandType() == VoiceCommand.UnionCommand.UnionCommand().VoiceOperationCommand

        operation = VoiceCommand.VoiceOperationCommand.VoiceOperationCommand()
        operation.Init(vc.Command().Bytes, vc.Command().Pos)

        print("Here")
        result = operation.Object()
        return result.decode("utf-8")
