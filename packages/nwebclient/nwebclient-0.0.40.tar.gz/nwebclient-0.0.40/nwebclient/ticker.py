import time
import os

class Process:
    name = 'process'
    cpu = None
    def __init__(self, name='Process'):
        self.name = name
    def tick(self):
        pass
    def cmd(self, args):
        return False

class CmdEcho(Process):
    def __init__(self):
        super().__init__('CmdEcho')
    def cmd(self, args):
        print("CMD: " + ' '.join(args))
        return False

class Ticker(Process):
    last = 0
    interval = 10
    def __init__(self, name = 'ticker', interval = 15):
        super().__init__(name) 
        self.interval = interval
    def tick(self):
        t = int(time.time())
        dur = t - self.last;
        if dur > self.interval:
            self.last = t
            self.execute()
    def cmd(self, args):
        if args[0]==self.name and args[1]=='set_interval':
            self.interval = int(args[2])
            return true
        return super().cmd(args)
    def execute(self):
        pass

class FileExtObserver(Ticker):
    def __init__(self, name = 'ext_observer', ext='.sdjob', interval = 15):
        super().__init__(name=name, interval=interval) 
        self.ext = ext
    def execute(self):
        filelist = [ f for f in os.listdir('.') if f.endswith(self.ext) ]
        for f in filelist:
            print(self.name + ": Found file: "+ f)

class Cpu:
    processes = []
    def __init__(self, *args):
        for arg in args:
            self.add(arg)
    def __iter__(self):
        return self.processes.__iter__()
    def add(self, process):
        process.cpu = self
        self.processes.append(process)
    def tick(self):
        for p in self.processes:
            p.tick()
        time.sleep(1)
    def cmd(self, args):
        for p in self.processes:
            p.cmd(args)
    def loop(self):
        while True:
            self.tick()

