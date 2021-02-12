'''
Setup file based on sample script made available at 
https://packaging.python.org/tutorials/packaging-projects/#configuring-metadata
Accessed February 10, 2021
'''

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="datahub_metrics_ingest",
    version="0.0.1",
    author="ITS DataHub",
    author_email="data.itsjpo@dot.gov",
    description="A package for ingesting Socrata and ROSA P Metrics.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/usdot-its-jpo-data-portal/datahub-metrics-ingest",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)