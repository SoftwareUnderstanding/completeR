import json
import os
import sys
class DockerImage:
    def Docker(self):
        existe = 0
        path = ''
        for dirpath, dirnames, filenames in os.walk("C:/Users/Javier/Desktop/TFG/somef"):
            #print("Ruta actual:", dirpath)
            #print("Carpetas:", ", ".join(dirnames))
            #print("Archivos:", ", ".join(filenames))
            for name in filenames:
                #print(os.path.join(name))
                if os.path.join(name) == "Dockerfile":
                    #print("Existe Dockerfile")
                    existe = 1
                    #print (os.path.join(dirpath))
                    path = os.path.join(dirpath)
                    break
        with open('C:/Users/Javier/Desktop/TFG/Programa/ProyectoUnificado/NewPythonProject/src/test(somef).json') as json_file:
            data = json.load(json_file)
            encontrado = 0
            nombre = ""
            for directory, files in data.items():
                if directory == "installation":
                   for iter in files:
                         for text,text2 in iter.items(): 
                             y = json.dumps(text2)
                             if y.__contains__("docker build"):
                                  encontrado == 1
                if directory == "name":
                    nombre = files['excerpt']
                            
            
        with open ('C:/Users/Javier/Desktop/TFG/Programa/ProyectoUnificado/NewPythonProject/src/README.md','a+') as h:                        
            if encontrado == 0:
                image= nombre+"image"
                h.write('## Dockerfile\n')
                h.write('Path of the Dockerfile:\n')
                h.write("```\n")
                h.write(''+path+' \n')
                h.write("```\n") 
                h.write('You can see the Dockerfile [here](Dockerfile.txt) \n')
                h.write('\n')
                h.write('First build the image using the Dockerfile in project folder:\n')
                h.write("```\n")
                h.write('docker build -t '+nombre+' '+image+ ' . \n')
                h.write("```\n")
                h.write("Then, we can execute the aplication with:\n")
                h.write("```\n")
                h.write('docker run $FLAGS '+image+' $PARAMS \n')
                h.write("```\n")
                h.write(">**NOTE:** Please, replace $FLAGS and $PARAMS with the right invocation of the image\n")
    pass            



