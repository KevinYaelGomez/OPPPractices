class TVCLASS():
    def __init__(self):
        self.isOn = False
        self.isMute = False
        self.listChannels = [2, 4, 8, 17, 22, 41, 58, 67]
        self.nChannels = len(self.listChannels)
        self.indexChannel = 0
        self.MINVOLUME = 0 #CONSTANTE
        self.MAXVOLUME = 10 #CONSTANTE
        self.volume = self.MAXVOLUME

    def power(self):
        self.isOn = not self.isOn

    def volumUp(self):
        if not self.isOn:
            return
        #Se cambie el volumen y al mismo tiempo quita el esta de muteado
        if self.isMute:
            self.isMute = False 
        if self.volume < self.MAXVOLUME:
            self.volume = self.volume + 1 

    def volumeDown(self):
        if not self.isOn:
            return
        if self.isMute:
            self.isMute = False
        if self.volume > self.MINVOLUME:
            self.volume = self.volume - 1

    def channelUp(self):
        if not self.isOn:
            return
        self.indexChannel = self.indexChannel + 1
        if self.indexChannel > self.nChannels:
            self.indexChannel = 0 #Regresa al primer canal
    
    def channelDown(self):
        if not self.isOn:
            return
        self.indexChannel = self.indexChannel - 1
        if self.indexChannel < self.nChannels:
            self.indexChannel = self.nChannels - 1 #Regresa el ultimo canal

    def mute(self):
        if not self.isOn:
            return
        self.isMute = not self.isMute
        
    def setChannel(self, newChannel):
        if newChannel in self.listChannels:
            self.indexChannel = self.listChannels.index(newChannel)
        #Si el newChannel no esta en la lista de canales, hace nada

    def showInfo(self):
        print()
        print("TV status")
        if self.isOn:
            print("TV is: On")
            print("Channel is:", self.listChannels[self.indexChannel])
            if self.isMute:
                print("Volumen id:", self.volume, "(sound is muted)")
            else:
                print("Volumen is:", self.volume)
        else:
            print("TV is off")

model1 = TVCLASS()