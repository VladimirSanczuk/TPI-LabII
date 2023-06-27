##### VISTA DE LA VENTANA EMERGENTE QUE PIDE EL NOMBRE DEL CLIENTE PARA GUARDAR LA RESERVA #####

from tkinter import *
from tkinter import messagebox


class ventanaConfirmacion:
    def __init__(self, parent, boton_confirma_reserva, boton_cancela_operacion):
        self.root = parent

        self.ventana_emergente = Toplevel(self.root)
        self.ventana_emergente.title("Confirmacion")
        self.ventana_emergente.geometry("300x250")
        self.ventana_emergente.config(bg="#002342")

        self.label_instruccion = Label(self.ventana_emergente, justify="center", fg="#ffffff", text="Nombre del cliente", bg="#002342")
        self.label_instruccion.pack(padx=10, pady=10)

        self.entry_nombre = Entry(self.ventana_emergente, width="150", justify="center")
        self.entry_nombre.pack(padx=10, pady=10)

        self.label_seña = Label(self.ventana_emergente, justify="center", fg="#ffffff",\
         text="Seña", bg="#002342")
        self.label_seña.pack(padx=10, pady=10)

        self.entry_seña = Entry(self.ventana_emergente, width="150", justify="center")
        self.entry_seña.pack(padx=10, pady=10)

        self.frameBotones = Frame(self.ventana_emergente, width="200", height="55", bg="#002342")
        self.frameBotones.pack(padx=10, pady=10)

        self.boton_aceptar = Button(self.frameBotones, text="Aceptar", command=boton_confirma_reserva)
        self.boton_aceptar.place(x="20", y="10", width="70", height="30")

        self.boton_cancelar = Button(self.frameBotones, text="Cancelar", command=boton_cancela_operacion)
        self.boton_cancelar.place(x="110", y="10", width="70", height="30")

    def cancelar(self):
        self.ventana_emergente.withdraw()

    def mostrar(self, precioTotal):
        self.precioTotalConIva = precioTotal * 1.21

        self.ventana_emergente.deiconify()

    def aceptar(self):
        #self.label_seña.config(text="Introduzca la seña\n Minima: $" + str(self.precioTotalConIva*0.3))

        try:
            nombreYSeña = []

            nombreCliente = self.entry_nombre.get()
            seña = self.entry_seña.get()

            if nombreCliente == "" or seña == "":
                messagebox.showwarning("Error de formato", "Los campos no pueden estar vacios")

                nombreYSeña.append(nombreCliente)
                
                nombreYSeña.append(seña)

                return nombreYSeña

            else:
                if(int(seña) < self.precioTotalConIva*0.3 or int(seña) > self.precioTotalConIva):
                    messagebox.showwarning("Error de cantidad", "La seña debe estar entre $" + str(self.precioTotalConIva*0.3) \
                        + " y $" + str(self.precioTotalConIva))
                
                else:
                    nombreYSeña.append(nombreCliente)

                    nombreYSeña.append(seña)

                    self.ventana_emergente.withdraw()

                    return nombreYSeña

        except ValueError:
            messagebox.showwarning("Error de formato", "El total a pagar debe ser un valor numerico")
