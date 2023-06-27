#### Clase encargada de modelar la lista de precios ####

class modeloPrecios:
	def __init__(self, ruta_archivo):
		self.ruta_archivo = ruta_archivo

	def crea_archivo_precios(self):
		encabezado = ['DJ', 'Decoracion', 'Cotillon', 'MaquinaHumo', 'Maquillaje', 'MusicaVivo']
		precios = ['0', '0', '0', '0', '0', '0']
		with open(self.ruta_archivo, "w") as archivoPrecios:
			linea = ','.join(encabezado) + "\n"
			archivoPrecios.write(linea)

			linea = ','.join(precios) + "\n"
			archivoPrecios.write(linea)

	def devuelve_precios(self, serviciosDeseados):
		precios = {}
		precioTotal = 0

		with open(self.ruta_archivo, "r") as archivoPrecios:
			lineas = archivoPrecios.readlines()

			encabezado = lineas[0].strip().split(',')

			precios = lineas[1].strip().split(',')

			precios = dict(zip(encabezado, precios))

		for i, servicio in enumerate(serviciosDeseados):
			if servicio == True:
				precio = int(precios.get(encabezado[i], 0))
				precioTotal += precio

		return precioTotal


