##### FICHERO DE EJECUCION PRINCIPAL #####

#Import
from Controller.controller import controller

#Creo instancia de clase controller
controlador = controller()

#Llamado a metodos y atributos
controlador.comprueba_situacion_BBDD()
controlador.lanzaInterfaz()

