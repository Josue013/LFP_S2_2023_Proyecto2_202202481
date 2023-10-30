from Reportes import Reporte
from tkinter import *

class management:
    def __init__(self,tokens,consola) -> None:
        self.tokens = tokens
        self.informacion = []
        self.consola = consola
        self.cant = 0
        self.arbol = ""
        self.asintactico = []
       
    def llenar(self,error):
        if not error:
            i=0
            n = 1
            while i<len(self.tokens):
                actual = self.tokens[i]
                if actual.getTipo() == "Tk_claves":
                    self.arbol="->Instruccion"+str(n)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+1].getTipo()+str(n)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+2].getTipo()+str(n)+"\n"
                    campos = []
                    i+=3
                    actual = self.tokens[i]
                    while actual.getTipo()!="Tk_CierraC":
                        if actual.getTipo() != "Tk_Coma":
                            self.arbol+="Instruccion"+str(n)+"->\""+actual.getTipo()+str(n+i)+"\"->"+actual.getLexema()+str("\".\""*n)+"\n"
                            campos.append(actual.getLexema().replace("\"","").strip())
                        else:
                            self.arbol+="Instruccion"+str(n)+"->\""+actual.getLexema()+str(n+i)+"\"\n"
                        i+=1
                        actual = self.tokens[i]
                    self.informacion.append(campos)
                    self.arbol+="Instruccion"+str(n)+"->\""+actual.getTipo()+str(n)+"\"\n"
                    self.asintactico.append(self.arbol)   
                    n+=1
                elif actual.getTipo() == "Tk_registros":
                    self.arbol="->Instruccion"+str(n)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i].getTipo()+str(n)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+1].getTipo()+str(n)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+2].getTipo()+str(n)+"\n"
                    registro = []
                    i+=4
                    actual = self.tokens[i]
                    while actual.getTipo()!="Tk_CierraC":
                        if actual.getTipo() != "Tk_Coma" and actual.getTipo() != "Tk_CierraL" and actual.getTipo() != "Tk_AbreL":
                            self.arbol+="Instruccion"+str(n)+"->\""+actual.getTipo()+str(n+i)+"\"->"+actual.getLexema()+str("\".\""*n)+"\n"
                            registro.append(actual.getLexema().replace("\"","").strip())
                        else:
                            self.arbol+="Instruccion"+str(n)+"->\""+actual.getTipo()+str(n+i)+"\"\n"    
                        if actual.getTipo() == "Tk_CierraL":
                            self.arbol+="Instruccion"+str(n)+"->"+actual.getTipo()+str(n+i)+"\n"   
                            self.informacion.append(registro)
                            self.cant+=1
                            registro = []
                        i+=1
                        actual = self.tokens[i]
                    self.arbol+="Instruccion"+str(n)+"->\""+actual.getTipo()+str(n)+"\"\n"  
                    self.asintactico.append(self.arbol)   
                    n+=1
                elif actual.getTipo() == "Tk_imprimir":
                    self.arbol="->Instruccion"+str(n)+"\n"
                    self.imprimir(self.tokens[i+2].getLexema().replace("\"",""))
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+1].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+2].getTipo()+str(n+i)+"->"+self.tokens[i+2].getLexema()+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+3].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+4].getTipo()+str(n+i)+"\n"
                    self.asintactico.append(self.arbol)   
                    n+=1
                elif actual.getTipo() == "Tk_imprimirln":
                    self.arbol="->Instruccion"+str(n)+"\n"
                    self.imprimirln(self.tokens[i+2].getLexema().replace("\"",""))
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+1].getTipo()+str(n)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+2].getTipo()+str(n+i)+"->"+self.tokens[i+2].getLexema()+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+3].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+4].getTipo()+str(n+i)+"\n"
                    self.asintactico.append(self.arbol)
                    n+=1
                elif actual.getTipo() == "Tk_conteo":
                    self.arbol="->Instruccion"+str(n)+"\n"
                    self.conteo()
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+1].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+2].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+3].getTipo()+str(n+i)+"\n"
                    self.asintactico.append(self.arbol)
                    n+=1
                elif actual.getTipo() == "Tk_promedio":
                    self.arbol="->Instruccion"+str(n)+"\n"
                    self.promedio(self.tokens[i+2].getLexema().replace("\"",""))
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+1].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+2].getTipo()+str(n+i)+"->"+self.tokens[i+2].getLexema()+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+3].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+4].getTipo()+str(n+i)+"\n"
                    self.asintactico.append(self.arbol)
                    n+=1
                elif actual.getTipo() == "Tk_contarsi":
                    self.arbol="->Instruccion"+str(n)+"\n"
                    self.contarsi(self.tokens[i+2].getLexema().replace("\"",""),float(self.tokens[i+4].getLexema()))
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+1].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+2].getTipo()+str(n+i)+"->"+self.tokens[i+2].getLexema()+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+3].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+4].getTipo()+str(n+i)+"->"+self.tokens[i+4].getLexema()+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+5].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+6].getTipo()+str(n+i)+"\n"
                    self.asintactico.append(self.arbol)
                    n+=1
                elif actual.getTipo() == "Tk_datos":
                    self.arbol="->Instruccion"+str(n)+"\n"
                    self.datos()
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+1].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+2].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+3].getTipo()+str(n+i)+"\n"
                    self.asintactico.append(self.arbol)
                    n+=1
                elif actual.getTipo() == "Tk_sumar":
                    self.arbol="->Instruccion"+str(n)+"\n"
                    self.suma(self.tokens[i+2].getLexema().replace("\"",""))
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+1].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+2].getTipo()+str(n+i)+"->"+self.tokens[i+2].getLexema()+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+3].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+4].getTipo()+str(n+i)+"\n"
                    self.asintactico.append(self.arbol)
                    n+=1
                elif actual.getTipo() == "Tk_max":
                    self.arbol="->Instruccion"+str(n)+"\n"
                    self.max(self.tokens[i+2].getLexema().replace("\"",""))
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+1].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+2].getTipo()+str(n+i)+"->"+self.tokens[i+2].getLexema()+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+3].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+4].getTipo()+str(n+i)+"\n"
                    self.asintactico.append(self.arbol)
                    n+=1
                elif actual.getTipo() == "Tk_min":
                    self.arbol="->Instruccion"+str(n)+"\n"
                    self.min(self.tokens[i+2].getLexema().replace("\"",""))
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+1].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+2].getTipo()+str(n+i)+"->"+self.tokens[i+2].getLexema()+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+3].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+4].getTipo()+str(n+i)+"\n"
                    self.asintactico.append(self.arbol)
                    n+=1
                elif actual.getTipo() == "Tk_exportarreporte":
                    self.arbol="->Instruccion"+str(n)+"\n"
                    self.reporte(self.tokens[i+2].getLexema().replace("\"",""))
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+1].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+2].getTipo()+str(n+i)+"->"+self.tokens[i+2].getLexema()+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+3].getTipo()+str(n+i)+"\n"
                    self.arbol+="Instruccion"+str(n)+"->"+self.tokens[i+4].getTipo()+str(n+i)+"\n"
                    self.asintactico.append(self.arbol)
                    n+=1
                
                i+=1
            print(self.informacion) 
        else:
            self.consola.insert(INSERT,"\nSyntaxError\nRevisar reporte de errores")
     
    def imprimir(self,cadena):
        self.consola.insert(INSERT,cadena)
    def imprimirln(self,cadena):
        self.consola.insert(INSERT,cadena+"\n")
    def conteo(self):
        self.consola.insert(INSERT,str(self.cant)+"\n")
    def promedio(self,campo):
        i=0
        promedio = 0
        for j in range(len(self.informacion[0])):
            if self.informacion[0][j] == campo:
                i=j
        for j in range(1,len(self.informacion)):
            promedio+= float(self.informacion[j][i])
        if i==0:
            i+=1
        promedio = promedio/i
        self.consola.insert(INSERT,str(promedio)+"\n")  
    def contarsi(self,campo,valor):
        cantidad = 0
        for j in range(len(self.informacion[0])):
            if self.informacion[0][j] == campo:
                i=j
        for j in range(1,len(self.informacion)):
            if valor == float(self.informacion[j][i]):
                cantidad+=1 
        self.consola.insert(INSERT,str(cantidad)+"\n")  
    def datos(self):
        self.consola.insert(INSERT,">>>")  
        for linea in self.informacion[0]:  
            self.consola.insert(INSERT,str(linea)+"\t\t")
        
        for i in range(1,len(self.informacion)):
            self.consola.insert(INSERT,"\n>>>") 
            for j in range(len(self.informacion[i])):  
                self.consola.insert(INSERT,self.informacion[i][j]+"\t\t")   
        self.consola.insert(INSERT,"\n")  
          
    def suma(self,campo):
        i=0
        suma = 0
        for j in range(len(self.informacion[0])):
            if self.informacion[0][j] == campo:
                i=j
        for j in range(1,len(self.informacion)):
            suma+= float(self.informacion[j][i])
        self.consola.insert(INSERT,str(suma)+"\n") 
    def max(self,campo):
        i=0
        max = 0
        for j in range(len(self.informacion[0])):
            if self.informacion[0][j] == campo:
                i=j
        for j in range(1,len(self.informacion)):
            if max < float(self.informacion[j][i]):
                max = float(self.informacion[j][i])
        self.consola.insert(INSERT,str(max)+"\n")  
    def min(self,campo):
        i=0
        for j in range(len(self.informacion[0])):
            if self.informacion[0][j] == campo:
                i=j
        min = float(self.informacion[1][i])
        for j in range(1,len(self.informacion)):
            if min > float(self.informacion[j][i]):
                min = float(self.informacion[j][i])
        self.consola.insert(INSERT,str(min)+"\n")
    def reporte(self,titulo):
        report = Reporte()
        report.reporteHTML(titulo,self.informacion)