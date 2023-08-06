import os
import setuptools
from mysutils.file import remove_files

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


class CleanCommand(setuptools.Command):
    """ Custom clean command to tidy up the project root. """
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        remove_files('build', 'dist', '*.pyc', '*.tgz', '*.egg-info', ignore_errors=True, recursive=True)


class PrepublishCommand(setuptools.Command):
    """ Custom prepublish command. """
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system('python setup.py clean')
        os.system('python setup.py sdist bdist_wheel')


setuptools.setup(
    cmdclass={
        'clean': CleanCommand,
        'prepublish': PrepublishCommand,
    },
    name='tempgit',
    version='0.1.0',
    url='https://github.com/jmgomezsoriano/tempgit',
    license='LGPL2',
    author='José Manuel Gómez Soriano',
    author_email='jmgomez.soriano@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    description='Some temporal operations over git repositories using, mainly, ssh private keys.',
    packages=setuptools.find_packages(exclude=["test"]),
    package_dir={'tempgit': 'tempgit'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9,<4',
    install_requires=['GitPython~=3.1.29', 'mysmallutils>=2.0.2,<2.1']
)
