import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from Analizador_Lexico import analizador
from Analizador_Sintactico import Sintactico
from management import management
from Reportes import Reporte


class app:
    def __init__(self,root:tk.Toplevel) -> None:
        self.entrada= ""
        self.tokens = []
        self.errores = []
        self.erroresSintacticos=[]
        #configuracion de la ventana
        root.title("Proyecto 2 - Analizador Bizdata")
        root.resizable(0,0)
        root.geometry("1280x720")
        root.config(bg="orange")
        root.config(bd=5)
        root.config(relief="groove")
        #Cuadro de texto
        codeFrame = tk.Frame(root,width=700,height=300, bg="#FF5733", )
        codeFrame.grid(row=1,padx=25,pady=10)
        #Consola
        consoleFrame = tk.Frame(root,width=100,height=100, bg="#FF5733", )
        consoleFrame.grid(row=2,padx=25,pady=10)
        
        #Menu
        barra_Menu = Menu(root)
        filemenu = Menu(barra_Menu, tearoff=0)
        filemenu.add_command(label="Abrir", command=self.carga) #Cargar Archivo
        filemenu.add_separator()
        filemenu.add_command(label="Salir", command=root.quit) #Salir
        barra_Menu.add_cascade(label="Archivo", menu=filemenu)

        editmenu = Menu(barra_Menu, tearoff=0)
        editmenu.add_command(label="Analizar", command=self.analizar) #Analizar Archivo
    
        barra_Menu.add_cascade(label="Analizar", menu=editmenu)

        #Reportes
        Menu_de_reportes = Menu(barra_Menu, tearoff=0)
        Menu_de_reportes.add_command(label="Tokens", command=self.reporteTokens) #reporte de tokens
        Menu_de_reportes.add_command(label="Errores", command=self.reporteErrores) #reporte de errores
        barra_Menu.add_cascade(label="Reportes", menu=Menu_de_reportes)
        root.config(menu=barra_Menu)
        
        self.label = Label(text="Proyecto #2: BizData - 202202481 - Lenguajes formales Seccion B-", font=("bebas", 12), bg="white", fg="black")
        self.label.grid(row=0, column=0, padx=10, pady=25, sticky="ew")

        self.text = Text(codeFrame,width=150,height=15)
        self.text.grid(row=0,column=0,padx=10,pady=10)

        self.console = Text(consoleFrame,width=150,height=15)
        self.console.grid(row=0,column=0,padx=10,pady=10)
        #self.console.config(state="disabled")

    def carga(self):
        try:
            path = filedialog.askopenfilename(filetypes=[('Texto plano', '*.bizdata')])
            self.entrada = open(path,"r").read()
            self.text.delete("1.0",END)
            self.text.insert(INSERT,self.entrada)
            messagebox.showinfo("Carga","Se cargaron los archivos con exito")
        except:
            messagebox.showerror("Error","Error al cargar el archivo")

    def analizar(self):
        text = self.text.get("1.0",END)
        analizar = analizador()
        analizar.analizar(text)
        self.tokens = analizar.getTokens()
        self.errores = analizar.getErrores()
        sintact = Sintactico(self.tokens)
        self.erroresSintacticos = sintact.error
        self.ges = management(sintact.tokens,self.console)
        self.ges.llenar(sintact.errorSintactico)
        messagebox.showinfo("Genial","Análisis finalizado")
    def reporteTokens(self):
        report = Reporte()
        report.reporteTokens("Tokens",self.tokens,None)
    
    def reporteErrores(self):
        report = Reporte()
        report.reporteTokens("Errores",self.errores,self.erroresSintacticos)


if __name__ == "__main__":
    root = tk.Tk()
    app = app(root)
    root.mainloop() 