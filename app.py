import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

class app:
    def __init__(self,root:tk.Toplevel) -> None:
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
        filemenu.add_command(label="Abrir", ) #Cargar Archivo
        filemenu.add_separator()
        filemenu.add_command(label="Salir", ) #Salir
        barra_Menu.add_cascade(label="Archivo", menu=filemenu)

        editmenu = Menu(barra_Menu, tearoff=0)
        editmenu.add_command(label="Analizar", ) #Analizar Archivo
    
        barra_Menu.add_cascade(label="Analizar", menu=editmenu)

        #Reportes
        Menu_de_reportes = Menu(barra_Menu, tearoff=0)
        Menu_de_reportes.add_command(label="Tokens", ) #reporte de tokens
        Menu_de_reportes.add_command(label="Errores", ) #reporte de errores
        Menu_de_reportes.add_command(label="Árbol de Derivación", ) # arbol
        barra_Menu.add_cascade(label="Reportes", menu=Menu_de_reportes)
        root.config(menu=barra_Menu)
        
        self.label = Label(text="Proyecto #2: BizData - 202202481 - Lenguajes formales Seccion B-", font=("bebas", 12), bg="white", fg="black")
        self.label.grid(row=0, column=0, padx=10, pady=25, sticky="ew")

        self.text = Text(codeFrame,width=150,height=15)
        self.text.grid(row=0,column=0,padx=10,pady=10)

        self.console = Text(consoleFrame,width=150,height=15)
        self.console.grid(row=0,column=0,padx=10,pady=10)
        self.console.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = app(root)
    root.mainloop() 