import json
import os

class MissingFields:
    def Missing(self,direct_out):
        with open('C:/Users/Javier/Desktop/TFG/Programa/ProyectoUnificado/NewPythonProject/src/SalidasAux/salida_missing.json') as json_file:
            with open (direct_out+'/README.md','a+') as h:
                file = open(direct_out+"/Missing.md", "w")
                h.write('\n')
                h.write('## Missing fields')
                h.write('\n')
                h.write('Consider adding the following sections in your readme: \n')
                h.write("```\n")
                data = json.load(json_file)
                for fields in data["missing"]:
                    #print (fields)
                    h.write(''+fields+'\n')
                    file.write(fields+"\n")
                h.write("```\n")
                file.close()
    pass
