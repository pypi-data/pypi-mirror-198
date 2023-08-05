from setuptools import setup, find_packages

VERSION = '0.9.8' 
DESCRIPTION = 'ShiftAI - smart energy management for Home Assistant with load shifting recommendations.'
LONG_DESCRIPTION = "ShiftAI is a Python package for implementing recommendation systems for load shifting in Home Assistant. It includes multiple agents that work collaboratively to analyze and optimize energy usage patterns in households, providing real-time suggestions for load shifting and reducing energy consumption. The package is customizable and user-friendly, making it an ideal choice for homeowners looking to adopt smart energy management practices."
# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="ShiftAI", 
        version=VERSION,
        author="SIS RS 6",
        author_email="<sonyaarom@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(exclude=[]),
        include_package_data=True,
        install_requires=["interpret==0.3.0",
                   "lime==0.2.0.1",
                   "matplotlib==3.6.2",
                   "meteostat==1.6.5",
                   "numpy==1.24.1",
                   "pandas==1.5.2",
                   "pytz==2022.7",
                   "scikit_learn==1.2.0",
                   "shap==0.41.0",
                   "statsmodels==0.13.5",
                   "tqdm==4.64.1",
                   "xgboost==1.7.2",
                   "helperagent"
                   ], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['recsys', 'home assistant'],
        classifiers= [
            "Intended Audience :: Science/Research",
            "Programming Language :: Python"


        ]
)




