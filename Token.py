class Token:
    def __init__(self,tipo,lexema,fila,columna) -> None:  
        self.tipo = tipo
        self.lexema = lexema
        self.fila = fila
        self.columna = columna
    def getTipo(self):
        return self.tipo
    def setTipo(self,tipo):
        self.tipo = tipo
    def getLexema(self):
        return self.lexema
    def setLexema(self,lex):
        self.lexema = lex
    def getFila(self):
        return self.fila
    def setFila(self,fila):
        self.fila = fila
    def getColumna(self):
        return self.columna
    def setTipo(self,columna):
        self.columna = columna
    def mostrar(self):
        print("["+self.getTipo()+" , "+self.getLexema()+" , "+str(self.getFila())+" , "+str(self.getColumna())+"]")