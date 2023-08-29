class Control:
    def __init__(self):
        self.__tv=None
    


    def enlazar(self, tv):
        self.__tv=tv
        tv.setControl(self)

    def setTv(self, tv):
        self.__tv=tv
    

    def getTv(self):
        return self.__tv
    

    def turnOn(self):
        self.__tv.turnOn()

    def turnOff(self):
        self.__tv.turnOff()

    

    def volumenUp(self):
        self.__tv.volumenUp()

    def volumenDown(self):
        self.__tv.volumenDown()

    def setCanal(self, canal):
        self.__tv.setCanal(canal)

    def setVolumen(self, volumen):
        self.__tv.setVolumen(volumen)

    def canalUp(self):
        self.__tv.canalUp()

    def canalDown(self):
        self.__tv.canalDown()