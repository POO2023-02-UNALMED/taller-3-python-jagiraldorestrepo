class TV:
    numTV = 0

    def __init__(self,marca,estado):
        self._canal = 1
        self._volumen = 1
        self._marca = marca
        self._precio = 500
        self._estado = estado
        self._control = None
        TV.numTV +=1

    #getters y setters-------------------------
    def getMarca(self):
        return self._marca
    
    def setMarca(self, marca):
        self._marca = marca

    def getCanal(self):
        return self._canal

    def setCanal(self, canal):
        if (self._estado == True and 1<=canal<=120):
            self._canal = canal

    def getPrecio(self):
        return self._precio
    
    def setPrecio(self,precio):
        self._precio = precio

    def getVolumen(self):
        return self._volumen
    
    def setVolumen(self, volumen):
        if (self._estado==True and 0<=volumen<=7):
            self._volumen = volumen

    def getControl(self):
        return self._control
    
    def setControl(self):
        return self._control
    
    
    
    
    
    #metodos de clase--------------------
    
    @classmethod
    
    def getNumTv(cls):
        return cls.numTV
    
    def setNumTv(cls,numTV):
        cls.numTV = numTV

    #-----------------------------

    def turnOn(self):
        self.estado = True
    
    def turnOff(self):
        self.estado = False
    
    def getEstado(self):
        return self._estado
    
    def canalUp(self):
        if (self._estado == True and 1<=self._canal<120):
            self._canal+=1

    def canalDown(self):
        if (self._estado == True and 1<self._canal<=120):
            self._canal-=1
    
    def volumenUp(self):
        if (self._estado == True and 0<=self._volumen<7):
            self._volumen+=1
   
    
    def volumenDown(self):
        if (self._estado == True and 0<self._volumen<=7):
            self._volumen-=1


                


