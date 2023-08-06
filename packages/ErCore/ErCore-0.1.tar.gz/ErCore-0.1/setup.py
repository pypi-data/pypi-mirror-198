from setuptools import setup

setup(
    name='ErCore',
    version='0.1',
    packages=['ErCore'],
    author='Eragod',
    description='This is a core for my package',
    entry_points={
        'console_scripts': [
            'ErCore = ErCore.cli:make_project_command'
        ]
    }
)
