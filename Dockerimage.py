import json
import os
import sys

with open('C:/Users/Javier/Desktop/TFG/Programa/test(somef).json') as json_file:
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
                            
            
with open ('C:/Users/Javier/Desktop/TFG/Programa/README.md','a+') as h:                        
     if encontrado == 0:
         image= nombre+"image"
         h.write('## Dockerfile\n')
         h.write('First build the image using the Dockerfile in project folder:\n')
         h.write("```\n")
         h.write('docker build -t '+nombre+' '+image+ ' . \n')
         h.write("```\n")
         h.write("Then, we can execute the aplication with:\n")
         h.write("```\n")
         h.write('docker run '+image+' \n')
         h.write("```\n")


