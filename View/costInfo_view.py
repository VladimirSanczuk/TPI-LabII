##### VISTA DE LA VENTANA EMERGENTE INFORMA TODOS LOS GASTOS ANTES DE CONFIRMAR LA RESERVA #####

from tkinter import *


class vistaInformacion:
    def __init__(self, parent, boton_siguiente_ventana_resumen_costos, boton_cancela_ventana_resumen_costos):
        self.root = parent

        self.ventana_emergente = Toplevel(self.root)
        self.ventana_emergente.title("Resumen")
        self.ventana_emergente.geometry("300x200")
        self.ventana_emergente.config(bg="#002342")

        self.label_instruccion = Label(self.ventana_emergente, justify="center", fg="#ffffff",\
         text="Resumen", bg="#002342")
        self.label_instruccion.pack(padx=10, pady=10)

        self.entry_nombre = Label(self.ventana_emergente, width="150", justify="center", fg="#ffffff",\
         text="Aca toda la data", bg="#002342")
        self.entry_nombre.pack(padx=10, pady=10)

        self.frameBotones = Frame(self.ventana_emergente, width="200", height="55", bg="#002342")
        self.frameBotones.pack(padx=10, pady=10)

        self.boton_siguiente = Button(self.frameBotones, text="Siguiente", command=boton_siguiente_ventana_resumen_costos)
        self.boton_siguiente.place(x="20", y="10", width="70", height="30")

        self.boton_cancelar = Button(self.frameBotones, text="Cancelar", command=boton_cancela_ventana_resumen_costos)
        self.boton_cancelar.place(x="110", y="10", width="70", height="30")

    def cancelar(self):
        self.ventana_emergente.withdraw()

    def mostrar(self, precioTotalNeto):
        self.ventana_emergente.deiconify()

        self.entry_nombre.config(text="El total neto a pagar es: $" + str(precioTotalNeto) + "\n"\
         + "El precio bruto con IVA del 21[%] es: $" + str(precioTotalNeto*1.21) + "\n"\
         + "La seña minima es: $" + str((precioTotalNeto*1.21)*0.3))
