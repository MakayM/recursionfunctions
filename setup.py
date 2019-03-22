from setuptools import setup, find_packages

setup(
    name='recursionfunctions',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Python functions for recursion and sorting',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<MakayM>/<recursionfunctions>',
    author='<Makhotso Pulumo>',
    author_email='<makhotsopulumo@gmail.com>'
)
