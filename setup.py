from setuptools import setup

setup(
    name="completer",
    version="1.0",
    description="Package that autocomplete README files",
    author="Javier de Toro, Daniel Garijo",
    author_email="",
    url="",
    packages=["completer"],
    scripts=[],
    install_requires = ['code_inspector @ git+ssh://git@github.com/SoftwareUnderstanding/code_inspector#egg=code_inspector',
                    'somef'],
    entry_points={"console_scripts": ["completer = completer.Completer:main"]},
)
