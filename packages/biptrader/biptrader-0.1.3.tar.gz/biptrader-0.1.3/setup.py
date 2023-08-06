from setuptools import setup

setup(
    name='biptrader',
    version='0.1.3',
    url='https://github.com/adramazany/biptrader',
    license='MIT',
    author='Adel Ramezani',
    author_email='adramazany@gmail.com',
    description='cryptocurrency trading helper library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords='cryptocurrency kucoin technical-analysis',
    install_requires=[
        'ccxt==3.0.20',
        'jproperties==2.1.1',
        'pandas==1.5.3',
        'pytz==2022.1',
        'SQLAlchemy==2.0.6',
    ],
    packages=[
        'tests',
        'biptrader',
    ],
)
