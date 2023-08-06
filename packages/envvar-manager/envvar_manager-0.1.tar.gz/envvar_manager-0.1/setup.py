from setuptools import setup, find_packages
from pip._internal.req import parse_requirements

# parse the requirements file and create a list of dependencies
install_reqs = parse_requirements('requirements.txt', session='hack')

# convert the dependencies to a list of strings
reqs = [str(ir.requirement) for ir in install_reqs]
print(reqs)

setup(
    name='envvar_manager',
    version='0.1',
    author="Omer Gindes",
    author_email="omer.gindes@gmail.com",
    packages=find_packages(),
    install_requires=reqs,
    entry_points={
        'console_scripts': [
            'envvar_manager=bin.cli:main',
        ],
    },
)
