from tkinter import Tk, Menu, messagebox, simpledialog, Text
import pandas as pd

class MenuApp:
    def __init__(self, master):
        self.master = master
        self.create_menu()
        self.nombreArchivo = "/media/b5/santino bongiorno/Santino Bongiorno/thony/pueba.xls"
        try:
            self.estudiantes = pd.read_excel(self.nombreArchivo)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo leer el archivo: {e}")
            self.estudiantes = pd.DataFrame()  # Evitar errores posteriores si no se carga el archivo

        self.text_area = Text(master, wrap='word', height=40, width=60)
        self.text_area.pack(side='left', fill='both', expand=True)
    
    def create_menu(self):
        barra_menus = Menu(self.master)

        menu_calculo = Menu(barra_menus, tearoff=0)
        menu_excel = Menu(barra_menus, tearoff=0)
        
        barra_menus.add_cascade(label="Excel", menu=menu_excel)
        barra_menus.add_cascade(label="Calculos", menu=menu_calculo)
        
        menu_excel.add_command(label="Todos", command=self.show_all)
        menu_excel.add_command(label="Nombre", command=self.show_name)
        menu_excel.add_command(label="Mayores de 18", command=self.show_over_18)
        
        menu_calculo.add_command(label="Promedio", command=self.show_all)  # Cambiar según tu lógica
        menu_calculo.add_command(label="Mediana", command=self.show_name)  # Cambiar según tu lógica
        menu_calculo.add_command(label="Moda", command=self.show_over_18)  # Cambiar según tu lógica
        
        self.master.config(menu=barra_menus)

    def clear_area(self):
        self.text_area.delete(1.0, 'end')

    def show_all(self):
        messagebox.showinfo("Opción seleccionada", "Mostrar todos los datos.")
        self.clear_area()
        self.text_area.insert('end', str(self.estudiantes))

    def show_name(self):
        self.clear_area()  # Limpiar el área de texto
        if not self.estudiantes.empty:
            nombres = self.estudiantes['nombreApellido'].tolist()  # Extraer los nombres como lista
            self.text_area.insert('end', '\n'.join(nombres))  # Mostrar nombres en el área de texto
        else:
            messagebox.showinfo("Sin datos", "No hay estudiantes para mostrar.")

    def show_over_18(self):
        self.clear_area()
        if not self.estudiantes.empty and 'edad' in self.estudiantes.columns:
            mayores_de_18 = self.estudiantes[self.estudiantes['edad'] >= 18]
            if not mayores_de_18.empty:
                self.text_area.insert('end', str(mayores_de_18))
            else:
                messagebox.showinfo("Sin datos", "No hay estudiantes mayores de 18 años.")
        else:
            messagebox.showinfo("Sin datos", "No hay datos disponibles.")

class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("Aplicación con Menú Excel")
        
        self.menu_app = MenuApp(self.root)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()

