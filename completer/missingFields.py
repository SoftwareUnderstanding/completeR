import json
import os

class missingFields:
    def missing(self,direct_out,json_in):
        with open(json_in) as json_file:
            with open (direct_out+'/README.md','a+') as h:
                file = open(direct_out+"/Missing.md", "w")
                h.write('\n')
                h.write('## Missing fields')
                h.write('\n')
                h.write('Consider adding the following sections in your readme: \n')
                h.write("```\n")
                data = json.load(json_file)
                for fields in data["missing"]:
                    h.write(''+fields+'\n')
                    file.write(fields+"\n\n")
                h.write("```\n")
                file.close()
    pass
