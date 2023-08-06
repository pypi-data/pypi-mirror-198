import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="D2L-INSTRUCTOR-API",
    version="0.1.1",
    author="Erin Sawyer, Jiaye Xie, Jonah Werner, Olivia Qiu, Pranay Pentaparthy",
    author_email="qiuolivi@msu.edu",
    description="D2L Instructor Data Cleaning API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your_username/D2L-Instructor-API",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)