from setuptools import setup, find_packages
import os

setup(
    name="onprem-shai",
    version="0.1.2",
    packages=find_packages(),
    install_requires=["click", "openai", "inquirer", "termcolor"],
    entry_points={
        "console_scripts": [
            "shai=shai.cli:cli",
        ],
    },
    author="Islam Almersawi",
    author_email="almersawi48@gmail.com",
    description="CLI tool to get command suggestions from OpenAI or local LLM and interactively select them.",
    long_description=(open("README.md").read() if os.path.exists("README.md") else ""),
    long_description_content_type="text/markdown",
    url="https://github.com/almersawi/shai",
    license="MIT",
)
