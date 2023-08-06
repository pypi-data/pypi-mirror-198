from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="django-evercookie",
    version="0.1.0",
    author="Aryan Hamedani",
    author_email="aryn.hmd@gmail.com",
    description="A reusable Django app that integrates evercookie functionality",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AryanHamedani/django-evercookie",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    python_requires=">=3.8",
    install_requires=[
        "Django>=4.0",
    ],
)