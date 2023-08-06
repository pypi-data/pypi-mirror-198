from setuptools import setup, find_packages

setup(name='Team11_AssistantBot',
      version='0.0.1',
      description='Assistant helps to manage the address book, notes, organizes file in folder',
      url='https://github.com/osandrey/GoIt_Team_11_Project/tree/testmyadressbook',
      author='Dima, Inna, Serhiy, Andrey',
      author_email='dima63475@gmail.com',
      include_package_data=True,
      license='MIT',
      packages=find_packages(),
      install_requires=[
                      "color-it",
                      "prompt_toolkit",
                      "functools",
                      "typing",
                      "prettytable"
                      ],
      entry_points={'console_scripts': ['assist = Team11_AssistantBot.main']})