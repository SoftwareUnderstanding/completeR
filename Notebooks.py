import json
import os

with open('C:/Users/Javier/Desktop/TFG/Programa/test(somef).json') as json_file:
        data = json.load(json_file)
#        print(data)
        i = 0

        for directory, files in data.items():
#            print (directory)
            if directory == "hasExecutableNotebook":
                with open ('C:/Users/Javier/Desktop/TFG/Programa/README.md','a+') as h:
                    h.write('## Notebooks\n')
                    h.write('You can try the following examples in Binder:\n')
                    for a,b in files.items():
                        if a == "excerpt":
                        
                            #print ("##Notebooks\n")
                            #print ("You can try the following examples in Binder:\n")
                            for iter in b:
                                i=i+1
                              
                                h.write (" "+ str(i) + ". Example:")
                                h.write ("[![Binder](https://mybinder.org/badge_logo.svg)]("+iter+")\n")
                         #   print(i,". Example:")
                         #  print ("[![Binder](https://mybinder.org/badge_logo.svg)](",iter,")\n")
                    #file.write(a+"\n")
                   
               
        
