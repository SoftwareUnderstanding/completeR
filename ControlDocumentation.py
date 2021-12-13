import json

class ControlDocumentation:
    def control(self):
        with open('C:/Users/Javier/Desktop/TFG/Programa/ProyectoUnificado/NewPythonProject/src/directory_info.json') as json_file:
            total_classes = 0
            total_functions = 0
            total_doc_classes = 0
            total_doc_functions = 0
            data = json.load(json_file)
            for directory, files in data.items():
                if directory == "directory_tree":
                    continue
                for file in files:
                    filename = f"{file['file']['fileNameBase']}.{file['file']['extension']}"
                    if "classes" in file:
                        classes_in_file = len(file["classes"])
                        total_classes += classes_in_file
                        for doc,busca in file["classes"].items():
                            if "doc" in busca:
                                total_doc_classes += 1
                    if "functions" in file:
                        functions_in_file = len(file["functions"])
                        total_functions += functions_in_file
                        for doc,busca in file["functions"].items():
                            if "doc" in busca:
                                total_doc_functions += 1


        porcentaje_classes = ( total_doc_classes / total_classes) * 100
        porcentaje_functions = ( total_doc_functions / total_functions) * 100



        if porcentaje_classes <25:
         colorc="red"
        if  25 > porcentaje_classes > 75:
            colorc="orange"
        if porcentaje_classes > 75:
            colorc="green"
        if porcentaje_functions <25:
            colorf="red"
        if 25 > porcentaje_functions > 75:
            colorf="orange"
        if porcentaje_functions > 75:
            colorf="green"
    
        with open ('C:/Users/Javier/Desktop/TFG/Programa/ProyectoUnificado/NewPythonProject/src/README.md','a+') as h:
            h.write('\n')
            h.write('## Documentation')
            h.write('\n')
            h.write('Here we show what percentage of the repositorys classes and functions are documented:\n')
            h.write('| Tipo documento  | Porcentaje documentado |\n')
            h.write('| ------------- | ------------- |\n')
            h.write('| Classes  | [![Generic badge](https://img.shields.io/badge/CLASSES-'+str(round(porcentaje_classes,2))+'-'+colorc+'.svg)](https://shields.io/)  |\n')
            h.write('| Functions  | [![Generic badge](https://img.shields.io/badge/FUNCTIONS-'+str(round(porcentaje_functions,2))+'-'+colorf+'.svg)](https://shields.io/)|\n')
    pass        
