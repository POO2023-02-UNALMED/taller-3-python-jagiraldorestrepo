class Control:
    def __init__(self):
        self._tv = None

    def setTv(self, tv):
        self._tv = tv

    def getTv(self):
        return self._tv
    
    def enlazar(self, tv):
        tv.setControl(self)
        self._tv = tv
        
    
    def turnOn(self):
        self._tv.turnOn()
    
    def turnOff(self):
        self._tv.turnOff()
    
    def canalUp(self):
        self._v.turnOff()
    
    def canalDown(self):
        self._tv.canalDown()

    def volumenUp(self):
        self._tv.volumenUp()

    def volumenDown(self):
        self.__tv.volumenDown()
    

    def setCanal(self, canal):
        self._tv.setCanal(canal)
    
    def setVolumen(self, volumen):
        self._tv.setVolumen(volumen)
    
