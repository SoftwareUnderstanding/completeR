import ControlDocumentation
import ExportRequirements
import License
import MissingFields
import Notebooks
import DockerImage
import Software
import shutil

a = ControlDocumentation.ControlDocumentation()
b = ExportRequirements.ExportRequirements()
c = License.License()
d = MissingFields.MissingFields()
e = Notebooks.Notebooks()
f = DockerImage.DockerImage()
g = Software.Software()



import click
@click.command()
@click.option('--direct_in','-i', type=str,required=True,help="Theres the path of the directory to inspect")
@click.option('--direct_out','-o', type=str,required=True,help="Theres the path of the directory save auxiliary documents(Requiremets.txt, Missing.md, Readme.md (modified)")
@click.option('--replace_readme','-r', type=bool, is_flag=True, default=False,help="Replace the README file of the repository")

def main(direct_in,direct_out,replace_readme):
    shutil.copy(direct_in+"/README.md", direct_out+"/README.md")
    a.control(direct_out)
    b.exportReq(direct_in,direct_out)
    c.License(direct_out)
    d.Missing(direct_out)
    e.Note(direct_out)
    f.Docker(direct_in,direct_out)
    g.Software(direct_out)
    if replace_readme:
        print("Si se activa")
        #os.remove(direct_in+"/README.md")
        shutil.copy(direct_out+"/README.md", direct_in+"/README.md")

if __name__ == "__main__":
    main()
