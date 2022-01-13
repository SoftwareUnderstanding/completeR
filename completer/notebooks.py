import json


class notebooks:
    def note(self, direct_out, json_in):
        with open(json_in) as json_file:
            data = json.load(json_file)
            i = 0

            for directory, files in data.items():
                # if directory == "executable_example":
                # with open (direct_out+'/README.md','a+') as h:
                # h.write('## Notebooks\n')
                # h.write('You can try the following examples in Binder:\n')
                # h.write('| Name  | Binder |\n')
                # h.write('| ------------- | ------------- |\n')
                #  for a,b in files.items():
                #       if a == "excerpt":
                #            for iter in b:
                #                 i=i+1
                #                  cadena = iter.split("/")
                #                   nombre = cadena.pop()
                # h.write ('| '+ nombre +' | [![Binder](https://mybinder.org/badge_logo.svg)]|'\n)
                # h.write('| ' + nombre + ' | ![Binder](https://mybinder.org/badge_logo.svg)|\n')
                # h.write (" "+ str(i) + ". "+ nombre +": " )
                # h.write ("[![Binder](https://mybinder.org/badge_logo.svg)]("+iter+")\n")
                #        h.write('\n')

                if directory == "hasExecutableNotebook":
                    with open(direct_out + '/README.md', 'a+') as h:
                        h.write('## Notebooks\n')
                        h.write('You can try the following examples in Binder:\n')
                        h.write('| Name  | Binder |\n')
                        h.write('| ------------- | ------------- |\n')
                        for a, b in files.items():
                            if a == "excerpt":
                                for iter in b:
                                    i = i + 1
                                cadena = iter.split("/")
                                nombre = cadena.pop()
                                #print(b)
                                # h.write ('| '+ nombre +' | [![Binder](https://mybinder.org/badge_logo.svg)]|'\n)
                                h.write('| ' + nombre + ' | [' + nombre + '](' + nombre + ')|\n')
                            # h.write (" "+ str(i) + ". "+ nombre +": " )
                            # h.write ("[![Binder](https://mybinder.org/badge_logo.svg)]("+iter+")\n")
                        h.write('\n')


pass
