import json
import os

class MissingFields:
    def Missing(self):
        with open('C:/Users/Javier/Desktop/TFG/Programa/ProyectoUnificado/NewPythonProject/src/salida_missing.json') as json_file:
            with open ('C:/Users/Javier/Desktop/TFG/Programa/ProyectoUnificado/NewPythonProject/src/README.md','a+') as h:
                h.write('\n')
                h.write('## Missing fields')
                h.write('\n')
                h.write('Consider adding the following sections in your readme: \n')
                h.write("```\n")
                data = json.load(json_file)
                for fields in data["missing"]:
                    #print (fields)
                    h.write(''+fields+'\n')
                h.write("```\n")    
    pass
