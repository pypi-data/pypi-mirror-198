import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="netskope", 
    version="0.0.1",
    author="John Neerdael",
    author_email="jneerdael@netskope.com",
    description="Netskope API Wrapper Module",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    project_urls={
        'Documentation': 'https://python-netskope.readthedocs.io/en/latest/',
        'Source': 'https://github.com/neerdael-nl/python-netskope',
        'Tracker': 'https://github.com/neerdael-nl/python-netskope/issues'
        },
    url="https://github.com/neerdael-nl/python-netskope",
    packages=['netskope'],
    license='BSD-2-Clause',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[ 'requests', 'pyyaml' ],
    package_data={'netskope':['documentation/*', 'README.rst', 'LICENSE', 'config.ini', 'CHANGELOG.rst']},
    # data_files=['CHANGELOG.rst','README.rst','LICENSE'],
    include_package_data=True
) 
