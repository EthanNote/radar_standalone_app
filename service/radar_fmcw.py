from datetime import datetime
from math import cos, sin
from struct import Struct
from socket import *
from threading import Thread

from worker import Worker
import config
import json
# class Target:
#     def __init__(self, position, time):
#         self.position = position
#         self.time = time
#         self.raw = None


class RadarTCPServer:
    
    def __init__(self):
        self.targetlist = []
        self.sock = None
        self.keep_running = True
        self.state = 'idle'
        self.thread = None
        self.w = Worker()

    def __del__(self):
        if self.sock is not None:
            self.sock.close()

        # if self.thread is not None:
        #     print('kill thread')
        #     self.thread.join()
        #     print('kill thread')

    def start(self, sub_thread=True):
        def server_thread():
            self.sock = socket(AF_INET, SOCK_STREAM)
            self.sock.bind(('0.0.0.0', 5100))
            while self.keep_running:
                self.state = 'listening'
                self.sock.listen()
                client, addr = self.sock.accept()
                print('connection from ', addr)
                while self.keep_running:
                    try:
                        frame = client.recv(1024)
                        self.on_data(frame)
                        self.state = 'reading'

                    except Exception as e:
                        print(e)
                time.sleep(1)

        if sub_thread:
            self.thread = Thread(target=server_thread)
            self.thread.setDaemon(True)
            self.thread.start()

        else:
            server_thread()

    def on_data(self, data_bytes):

        # print('data')

        if data_bytes[0:2] == b'U\xaa':
            datasize = Struct('!h').unpack(data_bytes[3:5])
            # print('Message type: ',hex(data_bytes[2]),' size: ',datasize)

        else:
            # print('Unknown header: ', hex(data_bytes[0]), hex(data_bytes[1]))
            return

        if (data_bytes[2] == 18):
            self.on_target_data(data_bytes)

    def on_target_data(self, data_bytes):

        target_count = data_bytes[5]
        now = datetime.now()
        for i in range(target_count):
            # distance, angle, x, y, velocity = Struct('!ihiih').unpack()
            start = 6 + 17 * i
            end = start + 16
            data = Struct('!ihiih').unpack(data_bytes[start:end])
            distance = data[0] * 0.01
            angle = data[1] * 0.01
            x = data[2] * 0.01
            y = data[3] * 0.01

            angle_corr_param = config.param['radar']['correction']['angle']
            dist_corr_param = config.param['radar']['correction']['distance']

            _angle = angle * angle_corr_param[0] + angle_corr_param[1]
            _distance = distance * dist_corr_param[0] + dist_corr_param[1]

            rad = _angle * 0.0174533
            _x, _y = _distance * sin(rad), _distance * cos(rad)

            dotdata = {"dispatch":"workers", "emit":{"event":"dot", "args": {"x":_x, "y":_y}}}
            self.w.sendMessage(json.dumps(dotdata))
            # target = Target((_x, _y), now)
            # target.raw = data
            # self.targetlist.append(target)
            print((_x, _y), data)


if __name__ == '__main__':
    s = RadarTCPServer()
    s.start(False)