import setuptools
import cryptpandas as crp 

with open("README.md", 'r') as f:
    long_description = f.read()

    
setuptools.setup(
    name="CryptPandas",
    version=crp.__version__, 
    author=crp.__author__,
    author_email=crp.__email__,
    description=crp.__about__,
    url=crp.__url__,
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=['pandas', 'cryptography','pyarrow'],
    classifiers=["Programming Language :: Python :: 3",
                 "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent"],
    python_requires='>=3.6',
)