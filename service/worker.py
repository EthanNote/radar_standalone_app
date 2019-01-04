import socket
import re
import threading

HOST = '127.0.0.1'    # The remote host
PORT = 6666             # The same port as used by the server


class Worker:
    def __init__(self):
        self.server_addr = ('127.0.0.1', 6666)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(self.server_addr)

    def run(self):
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

# class LogWorker(Worker):
#     def onMessage(self, string):
#         print('[LOG]', string)


# class EchoWorker(Worker):
#     def onMessage(self, string):
#         print('[ECHO WORKER]<', string)
#         print('[ECHO WORKER]>', string)
#         self.sendMessage('echo '+string)




#test
if __name__=="__main__":
    import random
    import json

    w = Worker()
 
    def build_random_targets():
        result = []
        for i in range(5+random.randint(0, 5)):
            result.append({"x":random.random(), "y":random.random()})
        return result

    def build_random_playback():
        nodes = []
        cx=0
        cy=80
        ct=1545052667717
        for i in range(8+random.randint(0, 8)):
            cx+=random.random()*85
            cy+=random.random()*50-10
            ct+=random.random()*5000
            nodes.append([int(cx), int(cy), int(ct)])
        
        return {"nodes":nodes, "images":[]}

    while True:
        input()
        # testdata = {"dispatch":"workers", "emit":{"event":"playback", "args": build_random_playback() }}
        y = random.random()
        x = random.random()
        testdata = {"dispatch":"workers", "emit":{"event":"dot", "args": {"x":(x-0.5)/2, "y":y/2+0.5}}}
        print(testdata)
        w.sendMessage(json.dumps(testdata))

    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #     s.connect((HOST, PORT))
    #     try:
    #         while True:
    #             # line = input('>')
    #             input()
    #             # data='%d:%s,'%(len(line), line)
    #             # s.send(data.encode())
    #             # testdata = {"dispatch":"workers", "data":build_random_targets()}

    #             # mail
    #             testdata = {"dispatch":"workers", "emit":{"event":"mail", "args":build_random_targets()}}
                
    #             # path
    #             testdata = {"dispatch":"workers", "emit":{"event":"playback", "args":{"nodes":[[0,0,0],[100,100,100000]], "images":[]}}}
    #             line = json.dumps(testdata)
    #             print('\n\nSEND:')
    #             print(line)
    #             data='%d:%s,'%(len(line), line)
    #             s.send(data.encode())

    #     except Exception as e:
    #         print(e)
