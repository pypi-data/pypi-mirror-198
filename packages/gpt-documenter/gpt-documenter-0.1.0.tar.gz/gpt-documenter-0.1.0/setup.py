from setuptools import setup, find_packages

setup(
    name='gpt-documenter',
    version='0.1.0',
    description='Python function documentator using ChatGPT.',
    author='Agustín Céspedes',
    author_email='agustinces17@gmail.com',
    packages=find_packages(),
    install_requires=[
        'langchain',
        'openai',
    ],
)