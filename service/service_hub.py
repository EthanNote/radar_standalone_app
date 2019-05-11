from twisted.internet import reactor, protocol, endpoints
from twisted.protocols import basic
import json

class HUB(protocol.Factory):
    def __init__(self):
        self.workers=set()
        self.groups={}
    def buildProtocol(self, addr):
        print('# INCOMMING # ', addr)
        return WorkerProtocol(self, '%s:%s'%(addr.host, addr.port))

# class RadarProtocol(basic.NetstringReceiver):
#     def __init__(self, factory):
#         self.factory = factory

#     def connectionMade(self):
#         self.factory.radars.add(self)

#     def connectionLost(self, reason):
#         self.factory.radars.remove(self)

#     def stringReceived(self, string):
#         print('[RADAR]', string)


class WorkerProtocol(basic.NetstringReceiver):
    def __init__(self, factory, addr):
        self.factory = factory
        self.name = addr
        self.workertype = 'WORKER'

    def connectionMade(self):
        print("[%s %s] CONNECTION MADE"%(self.workertype, self.name))
        self.factory.workers.add(self)

    def connectionLost(self, reason):
        print("[%s %s] CONNECTION LOST: %s"%(self.workertype, self.name, reason))
        self.factory.workers.remove(self)

    def stringReceived(self, string):
        print('[%s %s]: %s'%(self.workertype, self.name, string.decode()))
        j=None
        try:
            j = json.loads(string.decode())
        except Exception as e:
            pass

        if j == None and type(j) is not dict:
            return
        if 'dispatch' in j.keys():
            target = j['dispatch']
            if target == 'workers':
                print('Dispatch to workers')
                for w in self.factory.workers:
                    print('    => %s'%(w.name))
                    w.sendString(string)
            elif target in self.factory.groups.keys:
                target_group = self.factory.groups[target]
                print('Dispatch to group ', target)
                for w in target_group:
                    print('    => %s'%(w.name))
                    w.sendString(string)
            else:
                print('Unknown dispatch target ', target)
            # if j['dispatch'] == 'radars':
            #     for w in self.factory.radars:
            #         w.sendString(string)
            # if j['dispatch'] == 'clients':
            #     for w in self.factory.clients:
            #         w.sendString(string)

        if 'rename' in j.keys():
            self.name = j['rename']





endpoints.serverFromString(reactor, "tcp:6666").listen(HUB())
reactor.run()
