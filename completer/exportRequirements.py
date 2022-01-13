import json
import os



class exportRequirements:
    def exportReq(self,direct_in,direct_out,json_in):
        existe = 0
        path = ''

        with open(json_in) as json_file:
            data = json.load(json_file)
            if existe == 0:
                file = open(direct_out + "/requirements.txt", "w")
                for directory, files in data.items():
                    # print (directory)
                    if directory == "requirements":
                        for a, b in files.items():

                            file.write(a + "\n")

                file.close()


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
                    with open(path + '/requirements.txt', 'r') as file1:
                        with open(json_in, 'r') as file2:
                            difference = set(file1).difference(file2)
                    break


                        



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