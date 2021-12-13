import json
import os

class ExportRequirements:
    def exportReq(self):
        existe = 0
        path = ''
        for dirpath, dirnames, filenames in os.walk("C:/Users/Javier/Desktop/TFG/somef"):
            #print("Ruta actual:", dirpath)
            #print("Carpetas:", ", ".join(dirnames))
            #print("Archivos:", ", ".join(filenames))
            for name in filenames:
                #print(os.path.join(name))
                if os.path.join(name) == "requirements.txt":
                    #print("Existe requiremets")
                    existe = 1
                    path = os.path.join(dirpath)
                    #print (os.path.join(dirpath))
                    break
            
        with open('C:/Users/Javier/Desktop/TFG/Programa/ProyectoUnificado/NewPythonProject/src/Requirements/directory_info.json') as json_file:
            data = json.load(json_file)
            if existe == 0:
                file = open("C:/Users/Javier/Desktop/TFG/Programa/ProyectoUnificado/NewPythonProject/src/Requirements/Requirements.txt", "w")
                for directory, files in data.items():
                    #print (directory)
                    if directory == "requirements":
                        for a,b in files.items():
                            print (a)
                            file.write(a+"\n")
                    
                file.close()

                        


        with open ('C:/Users/Javier/Desktop/TFG/Programa/ProyectoUnificado/NewPythonProject/src/README.md','a+') as h:
            h.write('\n')
            h.write('## Requirements')
            h.write('\n')
            h.write('The necessary requirements for the project would be those that we have here attached [Requirements.txt](requirements.txt)\n')
            h.write('For the instalation of requirements:\n')
            h.write("```\n")
            h.write('pip install -r requirements.txt\n')
            h.write("```\n")
    pass
