import json

class Notebooks:
    def Note(self,direct_out):
        with open('C:/Users/Javier/Desktop/TFG/Programa/ProyectoUnificado/NewPythonProject/src/SalidasAux/test(somef).json') as json_file:
            data = json.load(json_file)
            i = 0

            for directory, files in data.items():
                if directory == "hasExecutableNotebook":
                    with open (direct_out+'/README.md','a+') as h:
                        h.write('## Notebooks\n')
                        h.write('You can try the following examples in Binder:\n')
                        h.write('| Name  | Binder |\n')
                        h.write('| ------------- | ------------- |\n')
                        for a,b in files.items():
                            if a == "excerpt":
                                for iter in b:
                                    i=i+1
                                    cadena = iter.split("/")
                                    nombre = cadena.pop()
                                    #h.write ('| '+ nombre +' | [![Binder](https://mybinder.org/badge_logo.svg)]|'\n) 
                                    h.write ('| '+ nombre +' | ![Binder](https://mybinder.org/badge_logo.svg)|\n')
                                    #h.write (" "+ str(i) + ". "+ nombre +": " )
                                    #h.write ("[![Binder](https://mybinder.org/badge_logo.svg)]("+iter+")\n")
                        h.write('\n')
    pass
