import json
import os
class software:
    def software(self,direct_out,json_in):
        with open(json_in) as json_file:
            data = json.load(json_file)
            with open (direct_out+'/README.md','a+') as h:
                for directory, files in data.items():
                    
                    if directory == "software_invocation":
                        
                        for a in files:
                            if a["run"]:
                                h.write('\n')
                                h.write('## Installation \n')
                                h.write("```\n")
                                h.write('#Install\n')
                                h.write('pip install -e . \n')
                                h.write('To invoke the software, you need to use the following command call: \n')
                                for b in a["run"]:
                                    #print(b)
                                    h.write(''+b+' $PARAMS \n' )
                                    
                                    h.write('>**NOTE**: You can try the $PARAMS of the software\n')
                                break
                        h.write("```\n")
                        

                    if directory == "software_type":
                        type_soft = files


                h.write('\n')   
                h.write('## Software Type')
                h.write('\n')
                h.write('This software is a '+type_soft+': \n')
                h.write ("![Software_type](https://img.shields.io/badge/Type-"+type_soft+"-blue.svg)\n")
    pass

