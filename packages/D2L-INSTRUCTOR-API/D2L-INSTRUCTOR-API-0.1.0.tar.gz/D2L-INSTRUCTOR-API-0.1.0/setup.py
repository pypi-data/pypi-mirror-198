from distutils.core import setup

setup(
    name='D2L-INSTRUCTOR-API',
    version='0.1.0',
    author='Erin Sawyer, Jiaye Xie, Jonah Werner, Olivia Qiu, Pranay Pentaparthy',
    author_email='qiuolivi@msu.edu',
    packages=['D2L'],
    url='http://pypi.python.org/pypi/D2LInstructorAPI/',
    license='LICENSE.txt',
    description='D2L Instructor Data Cleaning API',
    long_description=open('README.md').read(),
    install_requires=[
        "pandas >= 1.1.1",
    ],
)