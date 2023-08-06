from setuptools import setup, find_packages

setup(
    name="pysura",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "pysura=cli.app:cli"
        ]
    },
    # Add author info
    author="Tristen Harr",
    author_email="tristen@thegoodzapp.com",
    # Add description
    description="A Python library used to generate a backend for custom logic using Hasura as a Data-layer",
    url="https://github.com/tristengoodz/pysura"
)
