class Control:
    def __init__(self):
        self.tv = None

    def enlazar(self, tv):
        tv.setControl(self)
        self.tv = tv
    
    def setTv(self, tv):
        self.tv = tv

    def getTv(self):
        return self.tv

    
    def turnOn(self):
        self.tv.turnOn()
    
    def turnOff(self):
        self.tv.turnOff()
    
    def canalUp(self):
        self.tv.turnOff()
    
    def canalDown(self):
        self.tv.canalDown()

    def volumenUp(self):
        self.tv.volumenUp()

    def setCanal(self, canal):
        self.tv.setCanal(canal)
    
    def setVolumen(self, volumen):
        self.tv.setVolumen(volumen)
    
    
    
