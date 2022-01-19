from setuptools import find_packages, setup

setup(
    name='caccia_server',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask', 'firebase-admin', 'jsonschema'
    ],
)