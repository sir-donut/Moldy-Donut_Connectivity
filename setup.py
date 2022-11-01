from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'SSH connectivity focused on Network Devices'
LONG_DESCRIPTION = 'SSH connectivity focused on Network Devices'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="moldy-donut_connectivity", 
        version=VERSION,
        author="Logan Glaeser, Eric Nuno",
        author_email="glaeserl16@gmail.com, ericnuno@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=["netmiko",], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)