class test_digital_sequence(experiment):
    name = 'Test Digital Sequence'

    exp_parameters = []
    exp_parameters.append(('testTTL', 'starttime'))
    exp_parameters.append(('testTTL', 'duration'))
    exp_parameters.append(('testTTL','timeSep'))

    @classmethod
    def all_required_parameters(cls):

        return cls.exp_parameters

    def set_scannable_parameters(self):

        '''
        gets parameters, called in run so scan works
        '''
        self.starttime = self.p.testTTL.starttime
        self.duration = self.p.testTTL.duration
        self.cycles = self.p.testTTL.cycles

    def initialize(self, cxn, context, ident):
        self.t=take_pic()

    def run(self,cxn,context):
        self.t.start_threads()
        for t in self.t.threads: ##not sure whether they need to be joined? :')
            while t.isAlive():
                t.join(5)
        self.t.save_pictures()
  #      self.t.send_udp()
        self.t.save_png()




if __name__ == '__main__':
    cxn = labrad.connect()
    scanner = cxn.scriptscanner
    exprt = test_digital_sequence(cxn=cxn)
    ident = scanner.register_external_launch(exprt.name)
    exprt.execute(ident)