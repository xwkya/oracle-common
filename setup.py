from setuptools import setup, find_packages

print("Packages: ", find_packages())
print(find_packages())

setup(
    name="oraclecommon",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "SQLAlchemy",
        "azure-identity",
        "pyodbc",
        "python-dotenv",
        "tqdm",
    ],
)