from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ['psycopg2','pandas','boto3','yandexcloud','yandex']

setup(
    name="telaolparse",
    version="0.0.4",
    author="Alexander Andreev",
    author_email="andreyeffalex@gmail.com",
    description="A library to parse Excel Files for TEL/AOL project",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/telaolparse/homepage/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
    ],
)
