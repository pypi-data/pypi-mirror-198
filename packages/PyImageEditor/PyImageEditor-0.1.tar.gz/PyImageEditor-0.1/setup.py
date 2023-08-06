from setuptools import setup, find_packages

VERSION = '0.1' 
DESCRIPTION = 'PIE'
LONG_DESCRIPTION = 'A simple function interface over the PIL image editing in python'

# Setting up
setup(
        name="PyImageEditor", 
        version=VERSION,
        author="Kiwuthegamer",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['Pillow'],
        
        keywords = ['Images', 'PIL', 'Editing'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)