__author__ = 'Brian M Anderson'
# Created on 9/15/2020


from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='DicomRTTools',
    author='Brian Mark Anderson',
    email='bmanderson@mdanderson.org',
    version='0.0.2',
    description='Tools for reading dicom files, RT structures, and dose files, as well as tools for '
                'converting numpy prediction masks back to an RT structure',
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=['DicomRTTool'],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
    ],
    install_requires=required,
)
