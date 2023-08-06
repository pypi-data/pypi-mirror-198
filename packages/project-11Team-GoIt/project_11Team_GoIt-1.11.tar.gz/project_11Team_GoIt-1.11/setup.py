from setuptools import setup

setup(
    name='project_11Team_GoIt',
    version='1.11',
    description='AssistantBot include adressbook and notes',
    url='https://github.com/osandrey/GoIt_Team_11_Project/tree/testmyadressbook',
    author='Dima, Inna, Serhiy, Andrey',
    author_email='dima63475@gmail.com',
    license='UA',
    packages=["project_11Team_GoIt"],
    install_requires=['os',
                      "color-it",
                      "re",
                      "pickle",
                      "datetime",
                      "prompt_toolkit",
                      "functools",
                      "subprocess",
                      "collections",
                      "typing",
                      "prettytable",
                      ""
                        ],
    entry_points={'console_scripts': ['assist = project_11Team_GoIt.main']}
)