#### ESTE ARCHIVO ES LA VISTA PRINCIPAL, DESDE AQUI SE GESTIONA LA CAPA DE VISTA ####

#Import
from .calendar_view import vistaCalendario
from .form_view import vistaFormulario
from .costInfo_view import vistaInformacion
from .confirm_view import ventanaConfirmacion
from .cancel_view import vistaCancelar


from tkinter import *
from tkinter import messagebox


#clases
class vistaPrincipal:
	def __init__(self, presiona_Boton_Aceptar_Fecha, boton_acepta_formulario, boton_cancela_formulario,\
		boton_siguiente_ventana_resumen_costos, boton_cancela_ventana_resumen_costos, boton_confirma_reserva, \
		boton_cancela_operacion, mostrar_ventana_cancelar_reserva, boton_confirma_cancelacion, boton_cancela_eliminacion):

		#Construyo la vista principal	
		self.root = Tk()
		self.root.title("SocialEvent S.A")
		self.root.resizable(False,False)
		#self.root.iconbitmap("resources/favicon2.ico")

		self.miframe = Frame(self.root)
		self.miframe.pack()
		self.miframe.config(width="800", height="600", bg="#002342") #ancho x alto
		self.miframe.pack_propagate(False)

		#---------- Esta parte del código es para hacer que la interfaz aparezca centrada ----------
		self.wframe=800 #Ancho del Frame
		self.hframe=600 #Alto del Frame
		#---------------------
		self.pwidth=round((self.root.winfo_screenwidth())/2-self.wframe/2)
		self.pheight=round((self.root.winfo_screenheight())/2-self.hframe/2)
		#---------------------
		self.root.geometry(str(self.wframe)+"x"+str(self.hframe)+"+"+str(self.pwidth)+"+"+str(self.pheight))


		#Instancio distintas vistas
		self.formulario = vistaFormulario(self.miframe, boton_acepta_formulario, boton_cancela_formulario)
		self.formulario.ocultar()

		self.ventanaResumenCostos = vistaInformacion(self.root, boton_siguiente_ventana_resumen_costos,\
			boton_cancela_ventana_resumen_costos)
		self.ventanaResumenCostos.cancelar()

		self.ventanaConfirmacion = ventanaConfirmacion(self.root, boton_confirma_reserva, boton_cancela_operacion)
		self.ventanaConfirmacion.cancelar()

		self.ventanaCancelacion = vistaCancelar(self.root, boton_confirma_cancelacion, boton_cancela_eliminacion)
		self.ventanaCancelacion.cancelar()


		#Creamos la barra de menu
		menuBar = Menu(self.root)
		self.root.config(menu=menuBar)

		opciones_menu = Menu(menuBar, tearoff=0)
		about_menu = Menu(menuBar, tearoff=0)

		menuBar.add_cascade(label="Opciones", menu=opciones_menu)
		menuBar.add_cascade(label="Informacion", menu=about_menu)

		opciones_menu.add_command(label="Cancelar Reserva", command=mostrar_ventana_cancelar_reserva) #Cancelar la reserva es porque el cliente no quiere el evento
		opciones_menu.add_command(label="Pagar Deuda") #Esta opcion es para cuando el usuario debia el 70% y viene a pagarlo

		about_menu.add_command(label="About", command=self.mostrar_ventana_about)


		self.label_titulo = Label(self.miframe, text="SocialEvent SA", fg="#ffffff", bg="#002342", font=("Courier New", 24))
		self.label_titulo.place(relx=0.5, y = "25", anchor="center")

		self.label_subtitulo = Label(self.miframe, text="Gestion de reservas", fg="#ffffff", bg="#002342", font=("Courier New", 16))
		self.label_subtitulo.place(relx=0.5, y="50", anchor="center")

		self.fecha_deseada_label = Label(self.miframe, text="Fecha deseada:", fg="#ffffff", bg="#002342", \
			font=("Courier New", 12), anchor="w")
		self.fecha_deseada_label.place(x="10", y="100", width="150", height="35")

		self.fecha_deseada_entry = Entry(self.miframe, justify="center")
		self.fecha_deseada_entry.place(x="170", y="100", width="100", height="35")

		self.boton_aceptar_fecha = Button(self.miframe, justify="center", text="Aceptar", command=presiona_Boton_Aceptar_Fecha)
		self.boton_aceptar_fecha.place(x="280", y="100", width="100", height="35")


	#Metodo llamado para mostrar la pantalla principal
	def mostrar(self):
		self.root.mainloop()


	#Metodo llamado para cerrar la pantalla principal
	def cerrar(self):
		self.root.destroy()


	#Metodo llamado para mostrar el formulario de servicios deseados
	def mostrar_formulario(self):
		self.formulario.mostrar()


	#Metodo llamado para ocultar el formulario de servicios deseados
	def ocultar_formulario(self):
		self.formulario.ocultar()


	#Este metodo muestra en pantalla el formulario donde se carga el nombre y el dinero abonado para la reserva
	def mostrar_formulario_confirmacion(self, precioTotal):
		self.ventanaResumenCostos.cancelar()
		self.ventanaConfirmacion.mostrar(precioTotal)


	def confirma_reserva(self):
		datosReserva = []
		datosReserva = self.ventanaConfirmacion.aceptar()

		if datosReserva[0] == "" or datosReserva[1] == "":
			self.ventanaConfirmacion.cancelar()

			return datosReserva
		else:
			return datosReserva


	def cancela_operacion(self):
		self.ventanaConfirmacion.cancelar()


	def reserva_exitosa(self):
		messagebox.showinfo("Confirmacion", "La operacion se completo de manera exitosa")


	def mostrar_ventana_about(self):
		messagebox.showinfo("About", "Aplicacion de gestion de reserva de SocialEvent SA\n"
			+"Desarrollado por Vladimir Sanczuk\n\n" + "© 2023 SocialEvent SA. Todos los derechos reservados.")


	def boton_siguiente_ventana_resumen_costos(self):
		#ACA FALTARIA QUE RECIBA UNA LISTA CON DATOS A MOSTRAR EN LA VENTANA Y LOS ENVIA
		self.ventanaResumenCostos.cancelar()

		self.ventanaEmergente = ventanaConfirmacion(self.root, self.boton_confirma_reserva, self.boton_cancela_operacion)


	def boton_cancelar_ventana_resumen_costos(self):
		self.ventanaResumenCostos.cancelar()


	#Al presionar Aceptar en el formulario se me despliega una ventana con los detalles de costos
	def mostrar_ventana_detalles_costos(self, precioTotal):

		#Muestra un resumen de costos, le paso el precio total del evento
		self.ventanaResumenCostos.mostrar(precioTotal)


	def ocultar_ventana_detalle_costos(self):
		self.ventanaResumenCostos.cancelar()


	def devuelve_opciones_elegidas(self):
		self.valores_checkbuttons = []
		self.valores_checkbuttons = self.formulario.captar_servicios()

		return self.valores_checkbuttons



		







	def ventana_cancelar_reserva(self):
		self.ventanaCancelacion.mostrar()


	def boton_confirma_cancelacion(self):
		nombreCliente = self.ventanaCancelacion.aceptar()

		return nombreCliente


	def boton_cancelar_ventana_eliminacion(self):
		self.ventanaCancelacion.cancelar()


	def mostrar_reintegro(self, reintegro):
		if reintegro == 0:
			messagebox.showinfo("Reintegro", "Como canceló la reserva faltando solo 15 dias para el evento, no se\
				le debe reintegrar nada al cliente")
		else:
			messagebox.showinfo("Reintegro", "El total a reintegrar es $" + str(reintegro))


	def operacion_exitosa(self):
		messagebox.showinfo("Operacion Exitosa", "La operacion fue un exito")


	def operacion_erronea(self):
		messagebox.showwarning("Error de nombre", "El nombre de cliente no fue encontrado")
