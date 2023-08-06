from setuptools import setup, find_packages
import codecs
import os

#change to dict
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)),'README.md'), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.10'
DESCRIPTION = "Kills python + all subprocesses, restarts with the same args, Windows only, works with pyinstaller"

# Setting up
setup(
    name="babyonemoretime",
    version=VERSION,
    license='MIT',
    url = 'https://github.com/hansalemaos/babyonemoretime',
    author="Johannes Fischer",
    author_email="<aulasparticularesdealemaosp@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    #packages=['mainprocess', 'psutil', 'touchtouch'],
    keywords=['restart', 'python', 'execl', 'osexecl'],
    classifiers=['Development Status :: 4 - Beta', 'Programming Language :: Python :: 3 :: Only', 'Programming Language :: Python :: 3.9', 'Topic :: Scientific/Engineering :: Visualization', 'Topic :: Software Development :: Libraries :: Python Modules', 'Topic :: Text Editors :: Text Processing', 'Topic :: Text Processing :: General', 'Topic :: Text Processing :: Indexing', 'Topic :: Text Processing :: Filters', 'Topic :: Utilities'],
    install_requires=['mainprocess', 'psutil', 'touchtouch'],
    include_package_data=True
)
#python setup.py sdist bdist_wheel
#twine upload dist/*