import json

class Estadisticas_Descriptiva(object):
    moda = 0
    media = 0
    mediana = 0
    desv_estandar = 0
    varianza = 0

class Estadisticas(object):
    estadisticas_t_arribo: Estadisticas_Descriptiva
    estadisticas_t_servicio: Estadisticas_Descriptiva
    histograma_t_arribo = [] # Clases
    histograma_t_servicio = [] # Datos generados 

    def __init__(self):
        self.estadisticas_t_arribo = Estadisticas_Descriptiva()
        self.estadisticas_t_servicio = Estadisticas_Descriptiva()

    def toJSON(self):
        return json.dumps(self, default = lambda o:o.__dict__, 
            sort_keys = True, indent = 4)

class Data_Histograma(object):
    index = 0 
    rango = ""
    dato = 0


