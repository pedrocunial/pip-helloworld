from setuptools import setup


setup(
    name='my_hello_pedrocunial',
    version='0.1',
    packages=['my_hello'],
    scripts=['scripts/hello.py'],
    install_requires=[
        'pipenv',
    ],
)
