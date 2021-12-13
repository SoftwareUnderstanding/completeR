import json

class Notebooks:
    def Note(self):
        with open('C:/Users/Javier/Desktop/TFG/Programa/ProyectoUnificado/NewPythonProject/src/test(somef).json') as json_file:
            data = json.load(json_file)
            i = 0

            for directory, files in data.items():
                if directory == "hasExecutableNotebook":
                    with open ('C:/Users/Javier/Desktop/TFG/Programa/ProyectoUnificado/NewPythonProject/src/README.md','a+') as h:
                        h.write('## Notebooks\n')
                        h.write('You can try the following examples in Binder:\n')
                        for a,b in files.items():
                            if a == "excerpt":
                                for iter in b:
                                    i=i+1
                                    #print(iter)
                                    cadena = iter.split("/")
                                    nombre = cadena.pop()
                                    #print(nombre)
                                    h.write (" "+ str(i) + ". "+ nombre +": ")
                                    h.write ("[![Binder](https://mybinder.org/badge_logo.svg)]("+iter+")\n")
    pass
