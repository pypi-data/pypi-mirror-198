from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='PACOTES_DE_ACOES',
    version='0.0.1',
    license='MIT License',
    author='Clístenes Rodger e Marcos Eduardo',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='clistenes090@hotmail.com',
    keywords='moedas_acoes_2023',
    description=u'biblioteca com dados basicos sobre cotaçẽs de moedas e ações',
    packages=['moedas'],
    install_requires=['requests','yfinance','pandas','pandas_datareader','matplotlib.pyplot'],)