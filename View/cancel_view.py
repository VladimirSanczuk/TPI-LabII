from tkinter import *
from tkinter import messagebox

class vistaCancelar:
	def __init__(self, parent, boton_confirma_cancelacion, boton_cancela_eliminacion):
		self.root = parent

		self.ventana_emergente = Toplevel(self.root)
		self.ventana_emergente.title("Cancelar Reserva")
		self.ventana_emergente.geometry("300x250")
		self.ventana_emergente.config(bg="#002342")

		self.label_instruccion = Label(self.ventana_emergente, justify="center", fg="#ffffff", text="Nombre del cliente", bg="#002342")
		self.label_instruccion.pack(padx=10, pady=10)

		self.entry_nombre = Entry(self.ventana_emergente, width="150", justify="center")
		self.entry_nombre.pack(padx=10, pady=10)

		self.frameBotones = Frame(self.ventana_emergente, width="200", height="55", bg="#002342")
		self.frameBotones.pack(padx=10, pady=10)

		self.boton_aceptar = Button(self.frameBotones, text="Aceptar", command=boton_confirma_cancelacion)
		self.boton_aceptar.place(x="20", y="10", width="70", height="30")

		self.boton_cancelar = Button(self.frameBotones, text="Cancelar", command=boton_cancela_eliminacion)
		self.boton_cancelar.place(x="110", y="10", width="70", height="30")

	def cancelar(self):
		self.ventana_emergente.withdraw()

	def mostrar(self):
		self.ventana_emergente.deiconify()

	def aceptar(self):
		try:
			nombreCliente = self.entry_nombre.get()

			self.ventana_emergente.withdraw()

			return nombreCliente

		except ValueError:
			messagebox.showwarning("Error de formato", "El formato de nombre es erroneo")
