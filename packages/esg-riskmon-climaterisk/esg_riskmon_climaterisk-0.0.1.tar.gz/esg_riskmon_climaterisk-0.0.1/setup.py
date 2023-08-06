from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='esg_riskmon_climaterisk',
    version='0.0.1',
    author='Ginni Berti-Mei',
    author_email='ginevra.berti.mei@nbim.no',
    description='Package for Climate Risk Analytics.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/NBIM/climate_risk',
    packages=find_packages(),
    license='MIT',
    download_url='https://github.com/NBIM/climate_risk/archive/refs/tags/v0.0.1.tar.gz',
    install_requires=[
        'snowflake-connector-python[secure-local-storage,pandas]==2.7.6', 'typing', 'numpy', 'pydantic',
        'datetime', 'scipy', 'pandas', 'collections', 'pyodbc', 'textwrap', 'seaborn', 'matplotlib'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11'
    ]
)
