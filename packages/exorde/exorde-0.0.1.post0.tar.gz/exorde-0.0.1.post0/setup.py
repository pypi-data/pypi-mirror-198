from setuptools import setup, find_packages

setup(
    name='exorde',
    version='0.0.1r',
    packages=find_packages(include=['exorde']),
    license='MIT',
    entry_points={
        'console_scripts': [
            'exorde = exorde.command:run',
        ],
    },
    install_requires=[]
)
