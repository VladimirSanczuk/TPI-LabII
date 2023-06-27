from View.main_view import vistaPrincipal
from Model.book_model import modeloReservas
from Model.costList_model import modeloPrecios

from datetime import datetime
from tkinter import messagebox

import os

class controller:
	def __init__(self):
		self.vista_Principal = vistaPrincipal(self.presiona_Boton_Aceptar_fecha, self.boton_acepta_formulario, \
			self.boton_cancela_formulario, self.boton_siguiente_ventana_resumen_costos, \
			self.boton_cancela_ventana_resumen_costos, self.boton_confirma_reserva, self.boton_cancela_operacion, \
			self.mostrar_ventana_cancelar_reserva, self.boton_confirma_cancelacion, self.boton_cancela_eliminacion)

		self.reservas = modeloReservas("BBDD/reservas.txt") #Instancio la clase modeloReservas

		self.precios = modeloPrecios("BBDD/precios.txt")


	def lanzaInterfaz(self):
		self.vista_Principal.mostrar()


	def cierraInterfaz(self):
		self.vista_Principal.cerrar()


	#Metodo llamado apenas inicia el sistema para comprobar los archivos fundamentales de BBDD
	def comprueba_situacion_BBDD(self):

		#### Primero se hacen las comprobaciones con el archivo de reservas ####

		#Verificamos si el archivo que guarda las reservas existe
		if os.path.isfile("BBDD/reservas.txt"):
		#Si entra aca el archivo existe, verificamos si esta vacio
			if os.path.getsize("BBDD/reservas.txt") == 0:
				self.reservas.crea_archivo_reservas()
		else:
			#Si el archivo de reservas no existe, lo va a crear
			self.reservas.crea_archivo_reservas()

		
		#### Ahora se hacen las comprobaciones con el archivo de precios ####

		if os.path.isfile("BBDD/precios.txt"):
			if os.path.getsize("BBDD/precios.txt") == 0:
				self.precios.crea_archivo_precios()
		else:
			self.precios.crea_archivo_precios()


	#Cuando presiono aceptar en el boton de la ventana que pide el nombre, llama al metodo que confirma la reserva.
	def boton_confirma_reserva(self):

		#Creo una lista y guardo los datos que devuelve el metodo de confirma reserva.
		#Los datos recibidos son el nombre del cliente y el dinero para la seña
		datosReserva = []
		datosReserva = self.vista_Principal.confirma_reserva()

		if datosReserva[0] != "" or datosReserva [1] != "":
			#A la fecha que el usuario eligio para la reserva la formateamos y la insertamos en la posicion 1 de datosReserva
			fecha_str = datetime.strftime(self.fecha, "%d/%m/%y")
			datosReserva.insert(1, fecha_str)

			#Aca hay que calcular los gastos totales por la reserva
			precioTotal = self.precios.devuelve_precios(self.serviciosDeseados)
			datosReserva.append(str(precioTotal))
			señaMinima = precioTotal*0.3
			datosReserva.append(str(señaMinima))


			for i, valor in enumerate(self.serviciosDeseados):
				datosReserva.insert(2+i, valor)


			#Una vez se armaron todos los datos, se guarda la reserva
			self.reservas.agrega_nueva_reserva(datosReserva)

			self.vista_Principal.reserva_exitosa()


	#Cuando presiono cancelar en la ventana quue pide el nombre, llama al metodo que cierra esa ventana emergente.
	def boton_cancela_operacion(self):
		self.vista_Principal.cancela_operacion()
	

	#Cuando presiono aceptar en la ventana de servicios deseados (formulario) llama a este metodo
	def boton_acepta_formulario(self):
		self.serviciosDeseados = []

		self.serviciosDeseados = self.vista_Principal.devuelve_opciones_elegidas()

		precioTotal = self.precios.devuelve_precios(self.serviciosDeseados)

		self.vista_Principal.ocultar_formulario()

		self.vista_Principal.mostrar_ventana_detalles_costos(precioTotal) #aca pasar los precios para que pueda calcular


	#Cuando presiono cancelar en la ventana de servicios deseados (formulario) llama a este metodo
	def boton_cancela_formulario(self):
		self.vista_Principal.ocultar_formulario()


	def boton_siguiente_ventana_resumen_costos(self):
		precioTotal = self.precios.devuelve_precios(self.serviciosDeseados)

		self.vista_Principal.mostrar_formulario_confirmacion(precioTotal)


	def boton_cancela_ventana_resumen_costos(self):
		self.vista_Principal.ocultar_ventana_detalle_costos()


	#Se comprueba que la fecha cumpla con el formato correcto y que este disponible. Si esta disponible, muestra el formulario
	def presiona_Boton_Aceptar_fecha(self):

		#Obtengo el valor introducido en el Entry y borro lo que habia en el
		fecha_deseada = self.vista_Principal.fecha_deseada_entry.get()
		self.vista_Principal.fecha_deseada_entry.delete("0", "end")

		try:
			#A la fecha introducida por el usuario la combierto en objeto datetime para compararlo posteriormente
			self.fecha = datetime.strptime(fecha_deseada, "%d/%m/%y")

			if self.fecha < datetime.now():
				#Esto se podria lanzar desde el main_view llamando a un metodo
				messagebox.showwarning("Fecha invalida!", "No se puede seleccionar una fecha anterior a hoy")
			else:
				fecha_disponible = self.reservas.fecha_disponible(self.fecha) #Si se retorna False, la fecha no esta disponible

				if fecha_disponible == True:
					#La fecha esta disponible, llamar a metodo que carga demas datos
					self.vista_Principal.mostrar_formulario()

				else:
					#La fecha no esta disponible, devuelve las mas cercanas
					fechaMayorMasCercana, fechaMenorMasCercana = self.reservas.devuelve_fecha_cercana(self.fecha)
					messagebox.showwarning("Fecha existente", "La fecha elegida ya tiene reserva. Las fechas mas cercanas a"
						+ " la elegida son " + fechaMayorMasCercana + " y " + fechaMenorMasCercana)

		except ValueError:
			#Esto se podria lanzar desde el main_view llamando a un metodo
			messagebox.showwarning("Formato de fecha erroneo", "El formato de fecha debe ser DD/MM/YY")


	#En base a los servicios elegidos por el usuario se deben calcular los gastos totales
	def calcula_gastos(self):
		pass


	def usuario_abona_30(self):
		pass


	def usuario_abona_total(self):
		pass


	def mostrar_ventana_cancelar_reserva(self):
		self.vista_Principal.ventana_cancelar_reserva()


	def boton_confirma_cancelacion(self):
		nombreCliente = self.vista_Principal.boton_confirma_cancelacion()

		#Consulta a BBDD y calcular el reintegro puede ser $0 o el 20% de la seña si cancela 15 dias antes
		reintegro = self.reservas.devuelve_reintegro(nombreCliente)

		if reintegro != -1:
			self.vista_Principal.mostrar_reintegro(reintegro)

			self.reservas.borra_reserva(nombreCliente)

			self.vista_Principal.operacion_exitosa()
		else:
			self.vista_Principal.operacion_erronea()
	

	def boton_cancela_eliminacion(self):
		self.vista_Principal.boton_cancelar_ventana_eliminacion()



