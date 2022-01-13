# Completer
## Description
Completer, is a package that is responsible for traversing the PATH of a project and is responsible for collecting useful information from the project.
This information is compared with the README file that already exists in the repository and checks if any of the information is missing.

## Instalation Instructions
First of all, you have to go to the path of Completer:

```
cd completer
```

Then install the de package as follows:

```
pip install -e .
```

### Run

```
cd completer/completer
```

```
python completer.py --direct_in <DIRECTORY> --direct_out <DIRECTORY>
```

For showing help about the available options, run:

```
python completer.py --help
```

This comand, shows the next information:

```Usage: completer.py [OPTIONS]

Options:
  -i, --direct_in TEXT   Theres the path of the directory to inspect
                         [required]
  -o, --direct_out TEXT  Theres the path of the directory save auxiliary
                         documents(Requiremets.txt, Missing.md, Readme.md
                         (modified)  [required]
  -r, --replace_readme   Replace the README file of the repository
  --help                 Show this message and exit.
  
```



