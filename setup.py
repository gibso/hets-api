from setuptools import find_packages, setup

setup(
    name='hetsapi',
    version='0.0.1',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'flask', 'flask_api', 'pytest'
    ],
)