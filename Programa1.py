
import json




#with open('C:/Users/Javier/Desktop/TFG/Programa/directory_info.json') as f:
 #   data = json.load(f)

archivo = open('C:/Users/Javier/Desktop/TFG/Programa/directory_info.json','r')
 #   print(data['test/output_dir/outputdt//'])
i = 0
acumulador = 0

h = 0
acumulador_texto = 0

porcentaje = 0

for linea in archivo.readlines():
    lista_sin_puntos = linea.split(".")
    texto_sin_puntos = " ".join(lista_sin_puntos)
    lista_sin_llaves = texto_sin_puntos.split("{")
    texto_sin_llaves = " ".join(lista_sin_llaves)
    lista_sin_comas = texto_sin_llaves.split(",")
    texto_sin_comas = " ".join(lista_sin_comas)
    lista_sin_dospuntos = texto_sin_comas.split(":")
    texto_sin_dospuntos = " ".join(lista_sin_dospuntos)
    lista = texto_sin_dospuntos.split()
    i = lista.count('"extend"')
    acumulador = acumulador + i

    h = lista.count('"doc"')
    acumulador_texto = acumulador_texto + h

porcentaje = ( acumulador_texto / acumulador) * 100

print(acumulador)
print(acumulador_texto)
print(porcentaje)

print("Hay un",round(porcentaje, 2),"% documentado", )
                                                
archivo.close()
                                                
#print(data.get('test/output_dir/outputdt//'))

    

              
        


  #      for line in f: 
  #      print (line)
    
  #print(len(lines))


