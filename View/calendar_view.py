from tkinter import *
from calendar import *

class vistaCalendario:
	def __init__(self, parent):
		self.parent = parent
		self.miframe = Frame(self.parent)
		self.miframe.place(x="250", y="250", width="250", height="250")
		self.miframe.config(bg="#9aafaf")

		# Obtener el año y el mes actual
		self.year = 2023 # Puedes cambiarlo para que sea dinámico
		self.month = 6  # Puedes cambiarlo para que sea dinámico

		# Obtenemos el calendario del mes actual
		self.cal = monthcalendar(self.year, self.month)

		dias_semana = ['lun', 'mar', 'mie', 'jue', 'vie', 'sab', 'dom']

		for day_num, dia_semana in enumerate(dias_semana):
			label_dia_semana = Label(self.miframe, text=dia_semana, bg="#9aafaf", font=("Courier New", 11))
			label_dia_semana.grid(row=0, column=day_num)

		#Crear una grilla para mostrar los dias
		for week_num, week in enumerate(self.cal):
			separador = Frame(self.miframe, height=1, bg="#000000")
			separador.grid(row = week_num + 1, columnspan = 7, sticky="we")
			for day_num, day in enumerate(week):
				if day != 0:
					label_dia = Label(self.miframe, text=str(day), bg="#9aafaf", font=("Courier New", 11))
					label_dia.grid(row=week_num, column=day_num)




	def mostrar():
		self.miframe.pack()

	def ocultar():
		self.miframe.pack_forget()

