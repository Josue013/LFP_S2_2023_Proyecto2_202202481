from Token import Token

class analizador:
    def __init__(self) -> None:
        self.lexema=""
        self.estado =0
        self.tokens = []
        self.errores = []
        self.simbolo = {"=":"Tk_igual",";":"Tk_PuntoyC","{":"Tk_AbreL","[":"Tk_AbreC","]":"Tk_CierraC","}":"Tk_CierraL",",":"Tk_Coma","(":"Tk_AbreP",")":"Tk_CierraP"}
        self.reservada = ["claves","registros","imprimir","imprimirln","conteo","promedio","contarsi","datos","sumar","max","min","exportarreporte"]
    def getTokens(self):
        return self.tokens
    def getErrores(self):
        return self.errores
    def palabraReservada(self,palabra):
        for a in self.reservada:
            if palabra.lower() == a:
                return True
        return False
    def nuevoToken(self,tipo,lexema,fila,columna):
        tok = Token(tipo,lexema,fila,columna)
        if tipo!="Error":
            self.tokens.append(tok)
            self.lexema = ""
            self.estado = 0
        else:
            self.errores.append(tok)
    def mostrarTokens(self):
        print("--Lista Tokens--")
        for tok in self.tokens:
            tok.mostrar()
    def mostrarErrores(self):
        print("--Lista Errores--")
        for tok in self.errores:
            tok.mostrar()
    def analizar(self,entrada):
        i=0
        fila =1
        columna =0
        tkSimbolo = ""
        while i < len(entrada):
            actual = entrada[i] 
            if self.estado == 0:
                if actual.isalpha():
                    self.lexema+=actual
                    self.estado = 1
                    columna+=1
                    print("Letra")
                    i+=1
                elif actual.isdigit():
                    self.lexema+=actual
                    self.estado=2
                    columna+=1
                    i+=1
                elif actual == "\"":
                    self.lexema+=actual
                    self.estado=3
                    columna+=1
                    i+=1
                elif actual == "#":
                    self.lexema+=actual
                    self.estado=4
                    columna+=1
                    i+=1
                elif not self.simbolo.get(actual) == None: 
                    tkSimbolo = self.simbolo.get(actual)
                    self.lexema+=actual
                    self.estado=5
                    columna+=1
                elif actual == "\'":
                    self.lexema+=actual
                    self.estado=6
                    columna+=1
                    i+=1
                elif actual == '\n':
                    fila+=1
                    columna = 0
                    i+=1
                elif actual == '\t' or actual == ' ' or actual == '\r'  : 
                    columna +=1
                    i+=1
                else:
                    print("El símbolo: "+actual+" no pertenece al lenguaje") 
                    self.nuevoToken("Error",actual,fila,columna)
                    columna+=1
                    i+=1
            elif self.estado == 1:
                if actual.isalpha():
                    self.lexema+=actual
                    self.estado = 1
                    columna+=1
                    print("Letra")
                    i+=1
                else:
                    if self.palabraReservada(self.lexema):
                        self.nuevoToken("Tk_"+self.lexema.lower(),self.lexema,fila,columna) 
                        print("Aceptamos la palabra")
                    else:
                        self.nuevoToken("Error",self.lexema,fila,columna)
                        self.lexema=""
                        self.estado=0
                        columna+=1
                        i+=1
            elif self.estado == 2:
                if actual.isdigit():
                    self.lexema+=actual
                    self.estado=2
                    columna+=1
                    i+=1
                elif actual ==".":
                    self.lexema+=actual
                    self.estado=7
                    columna+=1
                    i+=1
                else:
                    self.nuevoToken("Tk_Numero",self.lexema,fila,columna)
                    print("numero entero")
            elif self.estado == 3:
                if actual.isalpha() or actual.isdigit():
                    self.lexema+=actual
                    self.estado=3
                    columna+=1
                    i+=1
                elif actual == "\"":
                    self.lexema+=actual
                    self.estado=5
                    columna+=1
                else:
                    self.lexema+=actual
                    self.estado=3
                    columna+=1
                    i+=1
            elif self.estado == 4: 
                if actual.isalpha() or actual.isdigit():
                    self.lexema+=actual
                    self.estado=4
                    columna+=1
                    i+=1
                elif actual == "\n":
                    self.nuevoToken("Tk_ComentarioLinea",self.lexema,fila,columna)
                    print("aceptarmos el comentario")
                else:
                    self.lexema+=actual
                    self.estado=4
                    i+=1
            elif self.estado == 5:
                if actual == "\"":
                    print("añadir token cadena")
                    self.nuevoToken("Tk_Cadena",self.lexema,fila,columna)
                    
                elif actual == "\'":
                    print("aniadir token de comentario multilinea")
                    self.nuevoToken("Tk_ComentarioMultilinea",self.lexema,fila,columna)
                    
                else:
                    print("añadir token de simbolo")
                    self.nuevoToken(tkSimbolo,self.lexema,fila,columna)
                i+=1
            elif self.estado == 6:
                if actual=="\'":
                    self.lexema+=actual
                    self.estado = 8
                    columna+=1
                    i+=1
                else:
                    print("Caracter desconocido")
                    self.estado=0
            elif self.estado == 7:
                if actual.isdigit():
                    self.lexema+=actual
                    self.estado=9
                    columna+=1
                    i+=1
                else:
                    self.estado=0
                    print("no hay numero luego de punto")
            elif self.estado == 8:
                if actual=="\'":
                    self.lexema+=actual
                    self.estado = 10
                    columna+=1
                    i+=1
                else:
                    print("Caracter desconocido")
                    self.estado=0
            elif self.estado == 9:
                if actual.isdigit():
                    self.lexema+=actual
                    self.estado=9
                    columna+=1
                    i+=1
                else:
                    self.nuevoToken("Tk_Numero",self.lexema,fila,columna)
                    print("Aceptamos numero decimal")
            elif self.estado == 10:
                if actual.isalpha() or actual.isdigit():
                    self.lexema+=actual
                    self.estado=10
                    columna+=1
                    i+=1
                elif actual=="\'":
                    self.lexema+=actual
                    self.estado = 11
                    columna+=1
                    i+=1
                else:
                    self.lexema+=actual
                    self.estado=10
                    columna+=1
                    i+=1
            elif self.estado == 11:
                if actual=="\'":
                    self.lexema+=actual
                    self.estado = 12
                    columna+=1
                    i+=1
                else:
                    print("Caracter desconocido")
                    self.estado=0
            elif self.estado == 12:
                if actual=="\'":
                    self.lexema+=actual
                    self.estado = 5
                    columna+=1
                else:
                    print("Caracter desconocido")
                    self.estado=0
        self.mostrarTokens()
        self.mostrarErrores()
        