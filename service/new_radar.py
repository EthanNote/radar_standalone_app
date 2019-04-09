import socket
import time
import struct
import sys
import collections
import logging
import datetime
import json
from worker import Worker

w = Worker()

def recvFromRadar():

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    radar_address = ('', 50000)
    sock.bind(radar_address)
    pack = 0
    filename = str(datetime.datetime.now()).replace(':','：')
    while True:
        # print(pack)
        # print('DEBUG')
        pack += 1
        msg1, addr = sock.recvfrom(8192)
        if msg1[0] != 1 or msg1[2] != 1:
            continue

        msg2, addr = sock.recvfrom(8192)
        if msg2[0] != 2 or msg2[2] != 2:
            continue
        # msg_list.append(msg)
        # print(type(msg), type(addr))
        if(msg1[0] == 1 and msg1[2] == 1 and msg2[0] == 2 and msg2[2] == 2):
            msg = msg1[4:]+msg2[4:]
            targetcount = struct.unpack('<f', msg[0:4])[0]
            Type = struct.unpack('<f', msg[4:8])[0]
            Version = struct.unpack('<f', msg[8:12])[0]
            curtime = struct.unpack('<f', msg[12:16])[0]
            # print({'Pack':pack,'Count':targetcount, 'Type':Type, 'Version':Version, 'Curtime':curtime})
            if targetcount < 1:
                sys.stdout.write('.')
                sys.stdout.flush()
                continue
            # print('DEBUG')

            target_data = []
            for i in range(32):

                sector = msg[16+i*60:16+(i+1)*60]
                # print(len(sector))

                dic = collections.OrderedDict({
                    'target_id': struct.unpack('<f', sector[0:4])[0],
                    'x': struct.unpack('<f', sector[4:8])[0],
                    'y': struct.unpack('<f', sector[8:12])[0],
                    'v': struct.unpack('<f', sector[12:16])[0],
                    'acc': struct.unpack('<f', sector[16:20])[0]
                })

                if (dic['target_id'] == 0.0):
                    break

                target_data.append(dic)
                # if(dic['x'] != 0 or dic['y'] != 0):
                print(dic, end='\n')
                dotdata = {"dispatch":"workers", "emit":{"event":"dot", "args": dic}}
                w.sendMessage(json.dumps(dotdata))
                if dic['target_id'] != 0:
                    logging.basicConfig(level=logging.INFO, filename="./logs/" + filename + ".log", datefmt='%Y/%m/%d %H:%M:%S',
                                        format="%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(module)s - %(message)s")
                    logger = logging.getLogger(__name__)
                    logger.info(dic)

            # rp.report({'data':target_data})
        else:
            print("sequence error", msg1[0:3], msg2[0:3])

    # print(msg_list)


if __name__ == '__main__':
    print('start receive the radar data...')
    recvFromRadar()
