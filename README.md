
## Documentation
Here we show what percentage of the repositorys classes and functions are documented:
| Tipo documento  | Porcentaje documentado |
| ------------- | ------------- |
| Classes  | [![Generic badge](https://img.shields.io/badge/CLASSES-5.03-red.svg)](https://shields.io/)  |
| Functions  | [![Generic badge](https://img.shields.io/badge/FUNCTIONS-15.61-red.svg)](https://shields.io/)|

## Requirements
The necessary requirements for the project would be those that we have here attached [Requirements.txt](requirements.txt)

For the instalation of requirements:
```
pip install -r requirements.txt
```
>**NOTE:** The following differences in requirements have been found: setuptools, requests, json2html, graphviz.
>
>Check your document in case they need to be added.


## License
The licese used is MIT License: [![License](https://img.shields.io/badge/LICENSE-MITLicense-blue.svg)](https://api.github.com/licenses/mit)

## Missing fields
Consider adding the following sections in your readme: 
```
citation
acknowledgement
run
download
requirement
contact
description
contributor
usage
faq
support
identifier
hasExecutableNotebook
hasBuildFile
hasDocumentation
executable_example
```
## Notebooks
You can try the following examples in Binder:
 1. TFidf-Logistic.ipynb: [![Binder](https://mybinder.org/badge_logo.svg)](https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/experiments/TFidf-Logistic.ipynb)
 2. initial_baseline.ipynb: [![Binder](https://mybinder.org/badge_logo.svg)](https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/experiments/initial_baseline.ipynb)
 3. TFidf-NB.ipynb: [![Binder](https://mybinder.org/badge_logo.svg)](https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/experiments/TFidf-NB.ipynb)
 4. Classifier%20Pipelines.ipynb: [![Binder](https://mybinder.org/badge_logo.svg)](https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/experiments/Classifier%20Pipelines.ipynb)
 5. Wordnet.ipynb: [![Binder](https://mybinder.org/badge_logo.svg)](https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/experiments/header_analysis/Wordnet.ipynb)
 6. SOMEF%20Usage%20Example.ipynb: [![Binder](https://mybinder.org/badge_logo.svg)](https://raw.githubusercontent.com/KnowledgeCaptureAndDiscovery/somef/master/notebook/SOMEF%20Usage%20Example.ipynb)
## Dockerfile
Path of the Dockerfile:
```
C:/Users/Javier/Desktop/TFG/somef 
```
You can see the Dockerfile [here](Dockerfile.txt) 

First build the image using the Dockerfile in project folder:
```
docker build -t somef somefimage . 
```
Then, we can execute the aplication with:
```
docker run $FLAGS somefimage $PARAMS 
```
>**NOTE:** Please, replace $FLAGS and $PARAMS with the right invocation of the image


## Software Invocation

```
manimgl $PARAMS 
```
>**NOTE**: You can try the $PARAMS of the software

Or

```
manim-render $PARAMS 
```
>**NOTE**: You can try the $PARAMS of the software


## Software Type
This software is a package: 
![Software_type](https://img.shields.io/badge/Software-package-blue.svg)
