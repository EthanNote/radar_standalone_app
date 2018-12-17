import socket
import re
import threading

HOST = '127.0.0.1'    # The remote host
PORT = 6666             # The same port as used by the server


class Worker:
    def __init__(self, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        self.socket.connect((HOST, PORT))
        # try:
        while True:
            s = self.socket.recv(4096).decode()
            print(s)
            matchObj = re.match(r'([0-9][0-9]*):(.*),', s)
            if(matchObj):   
                lenstr = matchObj.group(1)
                datastr = matchObj.group(2)
                print("Reg match: ", lenstr, datastr, len(datastr))
                if(int(lenstr) == len(datastr)):
                    self.onMessage(datastr)

        # except Exception as e:
        #     print(e)


    def onMessage(self, string):
        print(string)
    
    def sendMessage(self, string):       
        data='%d:%s,'%(len(string), string)
        self.socket.send(data.encode())

class LogWorker(Worker):
    def onMessage(self, string):
        print('[LOG]', string)


class EchoWorker(Worker):
    def onMessage(self, string):
        print('[ECHO WORKER]<', string)
        print('[ECHO WORKER]>', string)
        self.sendMessage('echo '+string)




#test
if __name__=="__main__":
    import random
    import json
    # def run_echo_worker():
    #     w = EchoWorker(5001)
    #     w.run()

    # def run_log_worker():
    #     w = LogWorker(5002)
    #     w.run()
    # threading.Thread(target=run_echo_worker).start()
    # threading.Thread(target=run_log_worker).start()

    def build_random_targets():
        result = []
        for i in range(5+random.randint(0, 5)):
            result.append({"x":random.random(), "y":random.random()})
        return result

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        try:
            while True:
                # line = input('>')
                input()
                # data='%d:%s,'%(len(line), line)
                # s.send(data.encode())
                # testdata = {"dispatch":"workers", "data":build_random_targets()}
                testdata = {"dispatch":"workers", "emit":{"event":"mail", "args":build_random_targets()}}
                line = json.dumps(testdata)
                print('\n\nSEND:')
                print(line)
                data='%d:%s,'%(len(line), line)
                s.send(data.encode())

        except Exception as e:
            print(e)
