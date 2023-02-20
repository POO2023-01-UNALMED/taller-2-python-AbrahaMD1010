class Asiento:
    def __init__(self,color:str,precio:int,registro:int) -> None:
        self.color = color
        self.precio = precio
        self.registro = registro 
        pass
    def cambiarColor(self,color) :
        if (color=="rojo" or color=="verde" or color=="blanco" or color=="amarillo" or color=="negro"):
            self.color = color
class Auto:
    cantidadCreados = 0 #atributo de clase
    def __init__(self,modelo:str,precio:int,asientos:list[Asiento],marca:str,motor:object,registro:int) -> None:
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        pass

    def cantidadAsientos(self) -> int :
        for elementos in self.asientos:
            i=0
            if (elementos!=None):
                i+=1
        return i
    def verificarIntegridad(self) -> str:
        for asiento in self.asientos :
            if (asiento==None):
                continue
            if (asiento.registro == self.motor.registro and asiento.registro == self.registro) :
                return "Auto original"
            else:
                return "Las piezas no son originales"


class Motor:
    def __init__(self,numeroCilindros:int,tipo:str,registro:int) -> None:
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
        pass
    def cambiarRegistro(self,numero:int) :
        self.registro = numero
    def asignarTipo(self,tipo:str) :
        if (tipo=="gasolina" or tipo=="electrico") :
            self.tipo = tipo 



