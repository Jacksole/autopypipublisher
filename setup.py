
import setuptools

setuptools.setup(
    name='hitherecli',  
    version='0.1',
    author="Le Aundre Jackson Sr. ",
    author_email="leaundre.jackson87@gmail.com",
    description="Saying hi from the cli",
    long_description="Saying hi from the cli",
    url="https://github.com/Jacksole/autopypipublisher",
    packages=["hitherecli"],
    entry_points = {
        "console_scripts": ['hitherecli = hitherecli.hitherecli:main']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
