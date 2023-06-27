from tkinter import *


class vistaFormulario:
	def __init__(self, parent, boton_acepta_formulario, boton_cancela_formulario):

		self.parent = parent
		self.framePrincipal = Frame(self.parent)
		#self.framePrincipal.place(x="10", y="55", width="780", height="290")
		self.framePrincipal.config(bg="#9aafaf", relief="solid", bd=2)

		self.framePrincipal.place_forget()

		self.textoEligeOpcion = Label(self.framePrincipal, text="Servicios extras:", font=("Courier New", 11), bg="#9aafaf", anchor="w")
		self.textoEligeOpcion.place(x="10", y="10", width="200", height="35")

		self.frameChecks = Frame(self.framePrincipal, width="760", height="235", bg="#9aafaf")
		self.frameChecks.place(x="10", y="55")

		self.frameChecks.grid_columnconfigure((0, 1), minsize=50, weight=1)
		self.frameChecks.grid_rowconfigure((0, 1, 2), minsize=50, weight=1)

		self.opcion1_var = BooleanVar()
		self.opcion1 = Checkbutton(self.frameChecks, text="DJ", bg="#9aafaf", variable = self.opcion1_var)
		self.opcion1.grid(row=0, column=0, padx=10, pady=10, sticky="w")

		self.opcion2_var = BooleanVar()
		self.opcion2 = Checkbutton(self.frameChecks, text="Decoracion", bg="#9aafaf", variable = self.opcion2_var)
		self.opcion2.grid(row=1, column=0, padx=10, pady=10, sticky="w")

		self.opcion3_var = BooleanVar()
		self.opcion3 = Checkbutton(self.frameChecks, text="Cotillon", bg="#9aafaf", variable = self.opcion3_var)
		self.opcion3.grid(row=2, column=0, padx=10, pady=10, sticky="w")

		self.opcion4_var = BooleanVar()
		self.opcion4 = Checkbutton(self.frameChecks, text="Maquina de humo", bg="#9aafaf", variable = self.opcion4_var)
		self.opcion4.grid(row=0, column=1, padx=10, pady=10, sticky="w")

		self.opcion5_var = BooleanVar()
		self.opcion5 = Checkbutton(self.frameChecks, text="Maquillaje", bg="#9aafaf", variable = self.opcion5_var)
		self.opcion5.grid(row=1, column=1, padx=10, pady=10, sticky="w")

		self.opcion6_var = BooleanVar()
		self.opcion6 = Checkbutton(self.frameChecks, text="Musica en vivo", bg="#9aafaf", variable = self.opcion6_var)
		self.opcion6.grid(row=2, column=1, padx=10, pady=10, sticky="w")

		self.boton_aceptar = Button(self.framePrincipal, justify="center", text="Aceptar", command=boton_acepta_formulario)
		self.boton_aceptar.place(x="10", y="235", width="100", height="35")

		self.boton_cancelar = Button(self.framePrincipal, justify="center", text="Cancelar", command=boton_cancela_formulario)
		self.boton_cancelar.place(x="120", y="235", width="100", height="35")

	def mostrar(self):
		self.framePrincipal.place(x="10", y="145", width="780", height="290")

	def ocultar(self):
		self.framePrincipal.place_forget()

	def captar_servicios(self):
		valores_checkbuttons = []

		if self.opcion1_var.get():
			valores_checkbuttons.append(True)
		else:
			valores_checkbuttons.append(False)

		if self.opcion2_var.get():
			valores_checkbuttons.append(True)
		else:
			valores_checkbuttons.append(False)

		if self.opcion3_var.get():
			valores_checkbuttons.append(True)
		else:
			valores_checkbuttons.append(False)

		if self.opcion4_var.get():
			valores_checkbuttons.append(True)
		else:
			valores_checkbuttons.append(False)

		if self.opcion5_var.get():
			valores_checkbuttons.append(True)
		else:
			valores_checkbuttons.append(False)

		if self.opcion6_var.get():
			valores_checkbuttons.append(True)
		else:
			valores_checkbuttons.append(False)

		return valores_checkbuttons

	def cancela_servicios(self):
		pass

