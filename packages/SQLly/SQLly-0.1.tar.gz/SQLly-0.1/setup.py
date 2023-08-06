from setuptools import setup, find_packages

setup(
    name='SQLly',
    version='0.1',
    description='A Python library for working with SQL/noSQL databases',
    author='Bektaş Kara',
    author_email='bektaskara4@gmail.com',
    packages=find_packages(),
    install_requires=[
        'mysql.connector',
        'psycopg2',
        'sqlite3',
        'colorama'
    ]
)