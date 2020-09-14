import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="microfilter",
    version="0.0.1",
    description="Filtering TRACE",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/microprediction/microfilter",
    author="microprediction",
    author_email="pcotton@intechinvestments.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["microfilter"],
    test_suite='pytest',
    tests_require=['pytest', 'microconventions', 'fakeredis'],
    include_package_data=True,
    install_requires=["pandas","numpy","pytest","python-dateutil"],
    entry_points={
        "console_scripts": [
            "microfilter=microfilter.__main__:main",
        ]
    },
)
