import time

class createLog():
    when = time.strftime("[%m%d%H%M]")

    def open_file(self):
        return open('log.evlp','a+')

    def writeFile(self,text):
        f = self.open_file()
        f.write('\n' + text)
        f.close()

    def BEGIN(self):
        self.writeFile('------------')

    def WARMING(self,text):
        print('WARMING: '+ str(text))
        self.writeFile('WARMING: {} {}'.format(str(text),self.when))

    def EXCEPTION(self,text):
        print('ERROR: ' + str(text))
        self.writeFile('ERROR: {} {}'.format(str(text),self.when))

    def LOG(self,text):
        print(str(text))
        self.writeFile('STATUS: {} {}'.format(str(text),self.when))
