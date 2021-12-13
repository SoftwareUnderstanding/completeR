import ControlDocumentation
import ExportRequirements
import License
import MissingFields
import Notebooks
import DockerImage
import Software


a = ControlDocumentation.ControlDocumentation()
b = ExportRequirements.ExportRequirements()
c = License.License()
d = MissingFields.MissingFields()
e = Notebooks.Notebooks()
f = DockerImage.DockerImage()
g = Software.Software()

a.control()
b.exportReq()
c.License()
d.Missing()
e.Note()
f.Docker()
g.Software()
