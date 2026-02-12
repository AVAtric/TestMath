from setuptools import setup, find_packages

setup(
    name="TestMath",
    version="0.1.0",
    description="A factorial calculator package with iterative and recursive implementations",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="TestMath Team",
    author_email="test@example.com",
    packages=find_packages(),
    install_requires=[
        "typer>=0.12.0",
    ],
    entry_points={
        "console_scripts": [
            "factorial=factorial.cli:app",
        ],
    },
    python_requires=">=3.12",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
    ],
)