import setuptools

setuptools.setup(
    name="cdpi", 
    version="0.0.6",
    author="Technology_Robster",
    author_email="metube0113@gmail.com",
    description="Python Implementation of Causal Discovery",
    url="https://github.com/Ho-Jun-Moon/picd",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires = ['numpy', 'scipy', 'pandas', 'matplotlib'],
)   