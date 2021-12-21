
## Documentation
Here we show what percentage of the repositorys classes and functions are documented:
| Type ||
| ------------- | ------------- |
| Classes  | [![Generic badge](https://img.shields.io/badge/CLASSES-5.03%25-red.svg)](https://shields.io/)  |
| Functions  | [![Generic badge](https://img.shields.io/badge/FUNCTIONS-15.61%25-red.svg)](https://shields.io/)|

## Requirements
The necessary requirements for the project would be those that we have here attached [Requirements.txt](requirements.txt)

For the instalation of requirements:
```
pip install -r requirements.txt
```
>**NOTE:** The following differences in requirements have been found: 
json2html
,setuptools
,graphviz
,requests


>Check your document in case they need to be added.


## License
The licese used is MIT License: [![License](https://img.shields.io/badge/LICENSE-MITLicense-blue.svg)](https://api.github.com/licenses/mit)

## Missing fields
Consider adding the following sections in your readme: [Missing.md](Missing.md)

## Notebooks
You can try the following examples in Binder:
| Name  | Binder |
| ------------- | ------------- |
| TFidf-Logistic.ipynb | ![Binder](https://mybinder.org/badge_logo.svg)|
| initial_baseline.ipynb | ![Binder](https://mybinder.org/badge_logo.svg)|
| TFidf-NB.ipynb | ![Binder](https://mybinder.org/badge_logo.svg)|
| Classifier%20Pipelines.ipynb | ![Binder](https://mybinder.org/badge_logo.svg)|
| Wordnet.ipynb | ![Binder](https://mybinder.org/badge_logo.svg)|
| SOMEF%20Usage%20Example.ipynb | ![Binder](https://mybinder.org/badge_logo.svg)|

## Dockerfile
Path of the Dockerfile:
```
cd C:/Users/Javier/Desktop/TFG/somef 
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

To invoke the software, you need to use the following command call:
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
