

import json

with open('C:/Users/Javier/Desktop/TFG/Programa/directory_info.json') as json_file:
        total_classes = 0
        total_functions = 0
        total_doc_classes = 0
        total_doc_functions = 0
        data = json.load(json_file)
        for directory, files in data.items():
            if directory == "directory_tree":
                print("IGNORING directory_tree key")
                continue
            print(f"> Parsing directory {directory}")
            for file in files:
                filename = f"{file['file']['fileNameBase']}.{file['file']['extension']}"
                print(f">>> Parsing file {filename}")
                if "classes" in file:
                    classes_in_file = len(file["classes"])
                    total_classes += classes_in_file
                    print(f">>>>>> {classes_in_file} classes on file {filename}")
                    for doc,busca in file["classes"].items():
                        if "doc" in busca:
                            total_doc_classes += 1
                else:
                    print(f">>>>>> NO classes on {filename}")

                if "functions" in file:
                    functions_in_file = len(file["functions"])
                    total_functions += functions_in_file
                    print(f">>>>>> {functions_in_file} functions on file {filename}")
                    for doc,busca in file["functions"].items():
                        if "doc" in busca:
                            total_doc_functions += 1
                else:
                    print(f">>>>>> NO functions on {filename}")
                    

                    
                    

print(f"TOTAL CLASS NUMBER: {total_classes}")
print(f"TOTAL CLASS DOC: {total_doc_classes}")
print(f"TOTAL FUNCTION NUMBER: {total_functions}")
print(f"TOTAL FUNCTION DOC: {total_doc_functions}")

porcentaje_classes = ( total_doc_classes / total_classes) * 100
porcentaje_functions = ( total_doc_functions / total_functions) * 100

print("Hay un",round(porcentaje_classes, 2),"% de clases documentadas", )
print("Hay un",round(porcentaje_functions, 2),"% de funciones documentadas", )






































""" import json




with open('C:/Users/Javier/Desktop/TFG/Programa/directory_info.json') as f:
   data = json.load(f)
   
   for a,b in data.items():
      print(a)
      print(b)
      listaA = a
      listaB = b

      print (listaA)

      #print (listaB)
      for c in listaB:
          print("-------------------------")
          print(c.keys())
          
          if (c.keys()):
             print(c.keys())
              if c.get('classes'):
                  print(c.get('classes')
           
       for h in c.get('classes'):
          print(h)

          
          if c["classes"]: 
              print(c["classes"])
          else:
              print("No tiene clases")
          

          
   print (data['test/output_dir/outputdt//docs'])
   for a,b in data['test/output_dir/outputdt//docs'].items():
      print(a)
     



         





print(data['test/output_dir/outputdt//'])

                                                
print(data.get('test/output_dir/outputdt//'))

    

              
        



    
  print(len(lines))

"""
