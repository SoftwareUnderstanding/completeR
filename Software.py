import json
import os
class Software:
    def Software(self):
        with open('C:/Users/Javier/Desktop/TFG/Programa/ProyectoUnificado/NewPythonProject/src/directory_infoSI.json') as json_file:
            data = json.load(json_file)
            with open ('C:/Users/Javier/Desktop/TFG/Programa/ProyectoUnificado/NewPythonProject/src/README.md','a+') as h:
                for directory, files in data.items():
                
                    if directory == "software_invocation":
                        for a in files:
                            if a["run"]:
                                h.write('\n')
                                h.write('## Installation \n')
                                h.write("```\n")
                                h.write('#Install\n')
                                h.write('pip install -e . \n')
                                for b in a["run"]:
                                    #print(b)
                                    h.write(''+b+' $PARAMS \n' )
                                    h.write('>**NOTE**: You can try the $PARAMS of the software\n')
                                break
                        h.write("```\n")        

                    if directory == "software_type":
                        type_soft = files


                h.write('\n')   
                h.write('## Software Type')
                h.write('\n')
                h.write('This software is a '+type_soft+': \n')
                h.write ("![Software_type](https://img.shields.io/badge/Software-"+type_soft+"-blue.svg)\n")
    pass

