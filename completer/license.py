import json

class license:
    def license(self,direct_out,json_in):
        with open(json_in) as json_file:
            data = json.load(json_file)
            for directory, files in data.items():
                if directory == "license":
                    with open (direct_out+'/README.md','a+') as h:
                        h.write('## License\n')
#                       h.write('You can try the following examples in Binder:\n')
                        for a,b in files.items():
                            if a == "excerpt":
#                            for iter in b:
                                #print(b['name']) 
                                nameLicen = b['name']
                                licen = b['url']
                                #print(nameLicen.replace(" ",""))
                                h.write ("The licese used is "+ nameLicen +": ")
                                h.write ("[![License](https://img.shields.io/badge/LICENSE-"+nameLicen.replace(" ","")+"-blue.svg)]("+licen+")\n")
    pass
