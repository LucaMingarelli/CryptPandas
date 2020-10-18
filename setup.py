import setuptools
import cryptpandas as crp 

with open("README.md", "r") as f:
    long_description = f.read()
with open("LICENSE.txt", "r") as f:
    licence = f.read()
    
setuptools.setup(
    name="connectors",
    version=crp.__version__, 
    author=crp.__author__,
    author_email=crp.__email__,
    description=crp.__about__,
    url=crp.__url__,
    license=licence,
    long_description=long_description,
    long_description_content_type="markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)