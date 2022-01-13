import somef.cli

from os import mkdir
import controlDocumentation
import exportRequirements
import license
import missingFields
import notebooks
import dockerImage
import software
import shutil
from code_inspector.cli import main as code_inspector_main
from somef.cli import run_cli

a = controlDocumentation.controlDocumentation()
b = exportRequirements.exportRequirements()
c = license.license()
d = missingFields.missingFields()
e = notebooks.notebooks()
f = dockerImage.dockerImage()
g = software.software()

import click


@click.command()
@click.option('--direct_in', '-i', type=str, required=True, help="Theres the path of the directory to inspect")
@click.option('--direct_out', '-o', type=str, required=True,
              help="Theres the path of the directory save auxiliary documents(Requiremets.txt, Missing.md, Readme.md (modified)")
@click.option('--replace_readme', '-r', type=bool, is_flag=True, default=False,
              help="Replace the README file of the repository")
def main(direct_in, direct_out, replace_readme):
    mkdir(direct_out + "/somef")
    somef.cli.run_cli(threshold=0.8, ignore_classifiers=False, repo_url=None, doc_src=direct_in + "/README.md", in_file=None, output=direct_out+"/somef/out_somef_basic.json", graph_out=None,
                      graph_format="turtle",codemeta_out=None,pretty=False,missing=False)


    somef.cli.run_cli(threshold=0.8, ignore_classifiers=False, repo_url=None, doc_src=direct_in + "/README.md", in_file=None, output=direct_out+"/somef/out_somef", graph_out=None,
                      graph_format="turtle",codemeta_out=None,pretty=False,missing=True)

    try:
        mkdir(direct_out + "/basic")
        code_inspector_main(["-i", direct_in, "-o", direct_out + "/basic"])
    except SystemExit:
        pass

    try:
        mkdir(direct_out + "/softwareInfo")
        code_inspector_main(["-i", direct_in, "-o", direct_out + "/softwareInfo", "-si"])
    except SystemExit:
        pass
    try:
        mkdir(direct_out + "/requirements")
        code_inspector_main(["-i", direct_in, "-o", direct_out + "/requirements", "-r"])
    except SystemExit:
        pass
    # code_inspector_main(input_path=direct_in, fig=False, output_dir=direct_out + "/code_inspector/basic", ignore_dir_pattern=False, ignore_file_pattern=False,requirements= False,html_output= False,call_list= False,
    #                    control_flow=False, directory_tree=False, software_invocation=False)
    #code_inspector_main(direct_in, False, direct_out + "/code_inspector/requirements", False, False, True, False, False,
    #                    False, False, False)

    shutil.copy(direct_in + "/README.md", direct_out + "/README.md")
    a.control(direct_out + "/basic/directory_info.json", direct_out)
    b.exportReq(direct_in, direct_out, direct_out + "/requirements/directory_info.json")
    c.license(direct_out,direct_out+"/somef/out_somef_basic.json")
    d.missing(direct_out,direct_out+"/somef/out_somef_missing.json")
    e.note(direct_out,direct_out+"/somef/out_somef_basic.json")
    f.docker(direct_in, direct_out,direct_out+"/somef/out_somef_basic.json")
    g.software(direct_out,direct_out + "/softwareInfo/directory_info.json")
    if replace_readme:
        print("Si se activa")
        # os.remove(direct_in+"/README.md")
        shutil.copy(direct_out + "/README.md", direct_in + "/README.md")


if __name__ == "__main__":
    main()
