import setuptools

setuptools.setup(

    name="housing_logeshwaran",

    version="v0.3",

    author="logeshwaran",

    packages=setuptools.find_packages(where='src'),
    package_dir={'': 'src'},

    python_requires='>=3.6',

)
