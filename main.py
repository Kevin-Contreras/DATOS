import json
from string import Template
import webbrowser as wb
archivoHTML = open("index.html")
temple = Template(archivoHTML.read())

def Json (archivo):
  nombres = ""
  edad =""
  activo =""
  promedio=""
  with open(archivo) as archivojson:
    archivoJson = json.load(archivojson)
    for linea in archivoJson:
      nombres = nombres + str(linea.get("nombre"))+ " "
      edad = edad + str(linea.get("edad")) +" "
      activo = activo + str(linea.get("activo")) + " "
      promedio = promedio + str(linea.get("promedio")) + " "
      file2 = open("json.html","w")
      resultado = temple.substitute({'nombre':nombres, 'edad': edad, 'activa':activo, 'promedio': promedio})
      file2.writelines(resultado)
  wb.open_new("json.html")
Json("archivo2.json")