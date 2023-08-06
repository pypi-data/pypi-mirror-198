from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='securedb',
    version='2.0.2',
    description='securedb is a fast and lightweight Python framework to easily interact with JSON-based encrypted databases.',
    py_modules=["securedb"],
    package_dir={'': 'src'},
    extras_require={
        "dev": [
            "cryptography"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Filippo Romani",
    author_email="mail@filipporomani.it",
    url="https://github.com/filipporomani/securedb"
)