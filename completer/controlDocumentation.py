import json


class controlDocumentation:
    def control(self, json_in, direct_out):
        with open(json_in) as json_file:
            colorf= ""
            colorc= ""
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
                        for doc, busca in file["classes"].items():
                            if "doc" in busca:
                                total_doc_classes += 1
                    if "functions" in file:
                        functions_in_file = len(file["functions"])
                        total_functions += functions_in_file
                        for doc, busca in file["functions"].items():
                            if "doc" in busca:
                                total_doc_functions += 1

        porcentaje_classes = (total_doc_classes / total_classes) * 100
        porcentaje_functions = (total_doc_functions / total_functions) * 100
        print(porcentaje_functions)
        print(porcentaje_classes)
        if porcentaje_classes < 25:
            colorc = "red"
        if porcentaje_classes > 25:
            colorc = "orange"
        if porcentaje_classes > 75:
            colorc = "green"
        if porcentaje_functions < 25:
            colorf = "red"
        if porcentaje_functions > 25:
            colorf = "orange"
        if porcentaje_functions > 75:
            colorf = "green"

        with open(direct_out + '/README.md', 'a+') as h:
            h.write('\n')
            h.write('## Documentation')
            h.write('\n')
            h.write('Here we show what percentage of the repositorys classes and functions are documented:\n')
            h.write('| Tipo documento  | Porcentaje documentado |\n')
            h.write('| ------------- | ------------- |\n')
            h.write('| Classes  | [![Generic badge](https://img.shields.io/badge/CLASSES-' + str(round(porcentaje_classes, 2)) + '%25-' + colorc + '.svg)](https://shields.io/)  |\n')
            h.write('| Functions  | [![Generic badge](https://img.shields.io/badge/FUNCTIONS-' + str(round(porcentaje_functions, 2)) + '%25-' + colorf + '.svg)](https://shields.io/) |\n')

    pass
