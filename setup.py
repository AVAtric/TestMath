from setuptools import setup, find_packages

setup(
    name="advmath",
    version="0.2.0",
    description="Advanced Mathematics Package - Calculator with factorial, fibonacci, gcd, lcm, and prime functions",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Advmath Team",
    author_email="advmath@example.com",
    packages=find_packages(),
    install_requires=[
        "typer>=0.12.0",
    ],
    entry_points={
        "console_scripts": [
            "advmath=advmath.cli:app",
        ],
    },
    python_requires=">=3.12",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
)