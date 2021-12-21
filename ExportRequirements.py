import json
import os

class ExportRequirements:
    def exportReq(self,direct_in,direct_out):
        existe = 0
        path = ''
        

        
        for dirpath, dirnames, filenames in os.walk(direct_in):
            #print("Ruta actual:", dirpath)
            #print("Carpetas:", ", ".join(dirnames))
            #print("Archivos:", ", ".join(filenames))
            for name in filenames:
                #print(os.path.join(name))
                if os.path.join(name) == "requirements.txt":
                    print("Existe requiremets")
                    existe = 1
                    path = os.path.join(dirpath)
                    print (path)
                    with open('C:/Users/Javier/Desktop/TFG/Programa/ProyectoUnificado/NewPythonProject/src/Pruebas/Requirements.txt', 'r') as file1:
                        with open('C:/Users/Javier/Desktop/TFG/Programa/ProyectoUnificado/NewPythonProject/src/Pruebas/Requirements1.txt', 'r') as file2:
                            difference = set(file1).difference(file2)
                    break

        with open('C:/Users/Javier/Desktop/TFG/Programa/ProyectoUnificado/NewPythonProject/src/SalidasAux/directory_info.json') as json_file:
            data = json.load(json_file)
            if existe == 0:
                file = open(direct_out+"Requirements.txt", "w")
                for directory, files in data.items():
                    #print (directory)
                    if directory == "requirements":
                        for a,b in files.items():
                            print (a)
                            file.write(a+"\n")
                    
                file.close()                            
                        



        with open (direct_out+'/README.md','a+') as h:
            h.write('\n')
            h.write('## Requirements')
            h.write('\n')
            h.write('The necessary requirements for the project would be those that we have here attached [Requirements.txt](requirements.txt)\n')
            h.write('For the instalation of requirements:\n')
            h.write("```\n")
            h.write('pip install -r requirements.txt\n')
            h.write("```\n")
            h.write('>**NOTE:** The following differences in requirements have been found: \n')
            for i in difference:
                print(i)
                h.write('>'+i+',')
            h.write('\n')  
            h.write('\n')
            h.write('>Check your document in case they need to be added.\n')
            h.write('\n')
    pass
