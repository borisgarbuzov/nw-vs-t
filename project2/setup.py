from setuptools import setup, setuptools

setup(
    name='nw-vs-t_pkg',
    version='0.0.1',
    description='Python package for nw-vs-t',
    author='statistics101',
    url='https://github.com/statistics101/nw-vs-t',
    packages=['src'],
    install_requires=[
        'numpy',
        'matplotlib',
        'pandas',
        'scikit-learn',
        'sphinx',
        'coverage',
        'joypy'
    ],
    python_requires='>=3.5'
)
