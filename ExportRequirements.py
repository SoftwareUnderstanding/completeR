import json
import os

with open('C:/Users/Javier/Desktop/TFG/Programa/Requirements\directory_info.json') as json_file:
        data = json.load(json_file)
#        print(data)

        file = open("C:/Users/Javier/Desktop/TFG/Programa/Requirements\Requirements.txt", "w")
        for directory, files in data.items():
#            print (directory)
            if directory == "requirements":
                for a,b in files.items():
                    print (a)
                    file.write(a+"\n")
                    
        file.close()
        
with open ('C:/Users/Javier/Desktop/TFG/Programa/README.md','a+') as h:
        h.write('\n')
        h.write('## Requiremens')
        h.write('\n')
        h.write('Los requirements necesarios para el proyecto serian los que tenemos aqui adjuntados [Requirements.txt](requirements.txt)')        
