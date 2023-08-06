from setuptools import setup

VERSION = '0.9.9.8' 
DESCRIPTION = 'ShiftAI - smart energy management for Home Assistant with load shifting recommendations.'

with open('README.md','r') as fh:
    LONG_DESCRIPTION = fh.read()

setup(
    name = 'ShiftAI',
    version= VERSION,
    description=DESCRIPTION,
    py_modules=["shiftai"],
    install_requires = [
        'pandas',
        'numpy',
        'matplotlib',
        'tqdm',
        'datetime',
        'xgboost',
        'scikit-learn',
        'statsmodels',
        'interpret',
        'shap',
        'entsoe-py',
        'beautifulsoup4==4.11.2',
        'helperagent == 5.0.0'
        ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"],
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    extras_require={
        "dev":[
            "pytest",
        ],
    },
)


