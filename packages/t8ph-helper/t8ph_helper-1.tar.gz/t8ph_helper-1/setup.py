from setuptools import setup, find_namespace_packages

setup(
    name="t8ph_helper",
    version="1",
    description="This is your console assistant by Python Powerhouse",
    author="Python Powerhouse",
    license="MIT",
    url="https://github.com/NovykovDaniil/python-core-project",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_namespace_packages(),
    include_package_data=True,
    include_dirs=True,
    install_requires=["pygame", "prettytable", "prompt-toolkit"],
    entry_points={
        "console_scripts": ["powerhouse-helper=t8ph_helper.main:run"]
    },
)