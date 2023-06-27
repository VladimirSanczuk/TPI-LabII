#### Clasa encargada de modelar las reservas hechas ####

from datetime import datetime, timedelta
import os

class modeloReservas:
	def __init__(self, ruta_archivo):
		self.ruta_archivo = ruta_archivo

	def crea_archivo_reservas(self):
		encabezado = ['Nombre', 'Fecha', 'DJ', 'Decoracion', 'Cotillon', 'MaquinaHumo', 'Maquillaje', 'MusicaVivo', \
		'TotalAbonado', 'PrecioTotal', 'SeñaMinima']
		with open(self.ruta_archivo, "w") as archivoReservas:
			linea = ','.join(encabezado) + "\n"
			archivoReservas.write(linea)


	def fecha_disponible(self, fecha):
		try:
			bandera = 0 
			archivo_fechas = open(self.ruta_archivo, 'r')

			for fila in archivo_fechas:
				campo = fila.split(",")
				fecha_archivo = campo[1]

				if fecha_archivo.lower() != "fecha":
					fecha_archivo_str = datetime.strptime(fecha_archivo, "%d/%m/%y")

					if fecha_archivo_str == fecha:
						bandera = 1
						return False

			if bandera == 0:
				return True

		except FileNotFoundError:
			print("No se encontro el archivo")


	def agrega_nueva_reserva(self, datosReserva):
		try:
			archivo_fechas = open(self.ruta_archivo, 'a+')
			datosReserva_str = ','.join(str(dato) for dato in datosReserva)
			archivo_fechas.write(datosReserva_str + "\n")
			archivo_fechas.close()

		except FileNotFoundError:
			print("No se pudo abrir el archivo de reservas")


	def devuelve_fecha_cercana(self, fechaIntroducida):
		#Como vamos a comparar fechas, primero formateo la fecha a un objeto de tipo datetime
		#fechaIntroducida = datetime.strptime(fechaIntroducida, "%d/%m/%y")

		fechas_reservadas=[]

		with open(self.ruta_archivo, "r") as archivoReservas:

			#Cargo todas las fechas reservadas en fechas_reservadas
			next(archivoReservas) #Ignoramos la primer fila
			
			for linea in archivoReservas:
				datos = linea.strip().split(',')
				fecha_reservada = datetime.strptime(datos[1], "%d/%m/%y")
				fechas_reservadas.append(fecha_reservada)


		#Ordenamos las fechas de manera ascendente
		fechas_reservadas_ordenadas = sorted(fechas_reservadas)

		#Se busca la fecha proxima mas cercana libre
		fechaMayorMasCercana = fechaIntroducida + timedelta(days=1)
		while fechaMayorMasCercana in fechas_reservadas_ordenadas:
			fechaMayorMasCercana += timedelta(days=1)

		#Se busca la fecha anterior mas cercana
		fechaMenorMasCercana = fechaIntroducida - timedelta(days=1)
		while fechaMenorMasCercana in fechas_reservadas_ordenadas:
			fechaMenorMasCercana -= timedelta(days=1)

		#Formateo las fechas hayadas a string
		fechaMayorMasCercana_str = datetime.strftime(fechaMayorMasCercana, "%d/%m/%y")
		fechaMenorMasCercana_str = datetime.strftime(fechaMenorMasCercana, "%d/%m/%y")

		#Retorno las fechas mas cercanas
		return fechaMayorMasCercana_str, fechaMenorMasCercana_str
		



	def devuelve_reintegro(self, nombreCliente):
		bandera = 0

		fecha_actual = datetime.now().date()

		with open(self.ruta_archivo, "r") as archivo:
			next(archivo)

			for linea in archivo:
				datos = linea.strip().split(',')

				if datos[0] == nombreCliente:
					bandera = 1

					fecha_reserva = datetime.strptime(datos[1], "%d/%m/%y").date()

					seña = float(datos[10])

					dias_faltantes = (fecha_reserva - fecha_actual).days

					if dias_faltantes < 15:
						return 0
					else:
						reintegro = seña*0.2
						return reintegro

		if bandera == 0:
			return -1


	def borra_reserva(self, nombreCliente):

		with open(self.ruta_archivo, "r") as archivoOriginal:

			with open("BBDD/temporal.txt", "w") as temporal:

				cabecera = archivoOriginal.readline()

				temporal.write(cabecera)

				for linea in archivoOriginal:
					datos = linea.strip().split(',')

					if datos[0] != nombreCliente:
						temporal.write(linea)

		#Reemplazamos el archivo original por el temporal
		os.replace("BBDD/temporal.txt", self.ruta_archivo)

