from setuptools import setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

with open("README.md") as f:
    long_description = f.read()

setup(
    name='regext',
    packages=['src'],
    version='0.0.1',
    description='Simple regex assistant with OpenAI API and prompt engineering',
    author='Sulthan Abiyyu',
    license='MIT',
    install_requires=requirements,
    long_description=long_description,
)
