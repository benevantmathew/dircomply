from setuptools import setup, find_packages

setup(
    name="dircomply",                 # Name of your package
    version="0.1",                     # Version of your package
    description="A small package to compare the files between two project folders.",  # Short description
    long_description=open("readme.md").read(),  # Detailed description
    long_description_content_type="text/markdown",
    author="Benevant Mathew",
    license="MIT",                     # License type
    packages=find_packages(include=["dircomply"]),  # Include only 'dircomply' directory
    install_requires=[],               # Add dependencies here
    entry_points={
        "console_scripts": [
            "dircomply = dircomply.main:create_gui",  # entry point
        ],
    },    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",        
    ],
    python_requires=">=3.7",           # Specify minimum Python version
)
