from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()
with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="PacoteDeProcessamento",
    version="0.0.1",
    author="Luis",
    description="Meu Pacote de Processamento simples",
    long_description=page_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
)