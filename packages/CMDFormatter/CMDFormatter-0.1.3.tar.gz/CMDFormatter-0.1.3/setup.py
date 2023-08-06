from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.1.3'
DESCRIPTION = 'Package to style and format cmd print'
LONG_DESCRIPTION = 'A package that allows to print into the terminal in a more styled and formatted new formmat\n use write function in order to get benefit of enhanced print function. attribute of write functions are:-\n text = Text to be printed in the console\n color = specify the color of text to be printed\n colorList = provide the list of color to be used while printing the text \n cyclic = provide False if trying  to print all text in same color provide true if trying to provide multiple colors to the text file\n durationInMilis: provide the duration in milisecond the time gap between the two characters of text.\n totalTime: parameter to provide the time in which function must print all the colors.\n end : the end same as print end parameter.\n '

# Setting up
setup(
    name="CMDFormatter",
    version=VERSION,
    author="NeuralNine (Florian Dedov)",
    author_email="<vishalkrsinghmsk@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'cmd', 'terminal', 'styling', 'user-experience', 'powershell'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
