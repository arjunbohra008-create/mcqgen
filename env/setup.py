from setuptools import find_packages, setup

setup(
    name="mcqgen",
    version="0.1.0",
    author="arjun",
    author_email="arjunbohra008@gmail.com",
    install_requires=["openai", "langchain", "streamlit", "python-dotenv", "pypdf2"],
    packages=find_packages(),
)