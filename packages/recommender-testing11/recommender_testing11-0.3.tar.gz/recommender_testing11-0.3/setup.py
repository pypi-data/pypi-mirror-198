from setuptools import setup
setup(
    name='recommender_testing11',
    version=0.3,
    description='simple random movie recommender',
    author='Arjun',
    author_email='arjun@spiced-academy.com',
    url='https://github.com/scikit-learn/scikit-learn/tree/main/sklearn/datasets',
    packages=['recommender'],
    license='Open Source',
    package_data={'recommender':['data/movies.txt']},
    install_requires = ['numpy'] # list of diff lib to preinstal
)
# import pandas as pd
# print(pd.__path__)
# print('/Users/arjunharidas/miniforge3/lib/python3.9/site-packages')

