class Cliente:
    ID = 0
    def __init__(nombre_completo, fecha_nac, sexo):
        self._nombre_comlpeto = nombre_completo
        self._fecha_nac = fecha_nac
        self._sexo = sexo
        self._boletos_comprados = 0
        self._ID = Cliente.ID
        self._premio = False
        Cliente.ID += 1
    
    def agregar_vuelo(self):
        """Agrega un boleto a su contador de boletos"""
        self._boletos_comprados += 1
        
    def comprobar_premios(self):
        """comprueba si es suceptible a un premio"""
        if self._boletos_comprados == 3:
            self._boletos_comprados = 0
            self._premio = True
            
    def canjear_premio(self,costo):
        """retorna el costo del boleto con descuento del 10%, sino devuelve el mismo costo"""
        if self._premio = True:
            self._premio = False
            return costo*.90
        else:
            return costo
if __name__ == "__main__":
    cliente1 =Cliente("Daniel Fuentes Castro","20/05/00","M")