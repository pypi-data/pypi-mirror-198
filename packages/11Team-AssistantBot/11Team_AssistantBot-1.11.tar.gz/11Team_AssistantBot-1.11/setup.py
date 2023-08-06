from setuptools import setup

setup(
    name='11Team_AssistantBot',
    version='1.11',
    description='AssistantBot include adressbook and notes',
    url='https://github.com/osandrey/GoIt_Team_11_Project/tree/testmyadressbook',
    author='Dima, Inna, Serhiy, Andrey',
    author_email='dima63475@gmail.com',
    license='UA',
    packages=["11Team_AssistantBot"],
    install_requires=[
                      "color-it",
                      "prompt_toolkit",
                      "functools",
                      "subprocess",
                      "typing",
                      "prettytable",
                      ""
                        ],
    entry_points={'console_scripts': ['assist = 11Team_AssistantBot.main']}
)