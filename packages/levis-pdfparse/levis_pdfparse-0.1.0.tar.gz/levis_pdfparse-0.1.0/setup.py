#! /usr/bin/env python
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

if __name__ == "__main__":
    setup(
        name='levis_pdfparse',
        version='0.1.0',
        description=' Python parser for scientific PDF based on GROBID.',
        long_description=long_description,
        long_description_content_type="text/markdown",
        url='https://github.com/lynner-haode/pdf_parser',
        author='Levis',
        author_email='lynner.haode@gmail.com',
        license='(c) MIT License 2023 Levis',
        install_requires=['lxml', 'requests', 'spacy', 'pandas', 'textstat'],
        packages=find_packages(),
        keywords=[
            "SCI",
            "PDF parser",
            "GROBID",
            "Python PDF parser"
        ],
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        package_data={
            'scipdf': ['pdf/pdffigures2/*.jar']
        },
        scripts=['serve_grobid.sh'],
    )
