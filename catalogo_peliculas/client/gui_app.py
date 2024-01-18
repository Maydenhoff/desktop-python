import tkinter as tk 

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width=300, height=300)

    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Inicio", menu= menu_inicio)

    menu_inicio.add_command(label="Crear Registro en DB")
    menu_inicio.add_command(label="Eliminar Registro en DB")
    menu_inicio.add_command(label="Salir", command= root.destroy) ##Command para el evento 
    

class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()
        self.config(bg="grey")