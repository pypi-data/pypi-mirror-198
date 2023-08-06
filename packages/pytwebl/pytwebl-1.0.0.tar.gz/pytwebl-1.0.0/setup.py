import pathlib
from setuptools import setup, find_packages


NAME = 'pytwebl'
# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
LONG_DESC = (HERE / "README.md").read_text()

VERSION = '1.0.0'

setup(
    name=NAME,
    version=VERSION,
    description="Creates template for web-development from shell, includes : html, css and js.",
    long_description=LONG_DESC,
    long_description_content_type='text/markdown',
    url="https://github.com/SoumadeepChoudhury/pytwebl",
    author="Ahens | An Initiative to Initial (Soumadeep Choudhury)",
    author_email="ahensinitiative@gmail.com",
    maintainer="Manmay Chakraborty",
    maintainer_email="manmaycoder@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': ['pytwebl=pytwebl.main:main'],
    },
)
