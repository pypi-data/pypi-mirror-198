from setuptools import setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

with open("README.md") as f:
    long_description = f.read()

setup(
    name='regext',
    packages=['regext'],
    version='0.0.4',
    description='Simple regex assistant with OpenAI API and prompt engineering',
    author='Sulthan Abiyyu',
    license='MIT',
    install_requires=requirements,
)
