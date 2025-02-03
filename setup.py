from setuptools import setup, find_packages

setup(
    name="package",  # Name of your package
    version="0.1",  # Version number
    author="Ruturaj",  # Your name
    author_email="rajdixitrd7272@gmail.com",  # Your email
    description="A package with 4 functions to perform basic operations",  # Short description
    long_description=open("README.md").read(),  # Long description from README
    long_description_content_type="text/markdown",  # Type of long description
    url="https://github.com/ruturajdixit99/package.git",  # GitHub URL
    packages=find_packages(),  # Automatically find packages
    install_requires=[],  # List of dependencies (if any)
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Python version requirement
)