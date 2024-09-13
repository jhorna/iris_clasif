from setuptools import setup, find_packages

setup(
    name='iris_classification',
    version='0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'pytest',
    ],
)
