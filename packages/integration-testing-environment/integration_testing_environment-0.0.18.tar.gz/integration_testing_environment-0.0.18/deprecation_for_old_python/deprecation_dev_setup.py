import setuptools

with open("../README.md", "r") as README:
    long_description = README.read()

setuptools.setup(
    name="integration_testing_environment_dev",
    version="0.0.18",
    author="JE-Chen",
    author_email="zenmailman@gmail.com",
    description="Integration testing environment for web gui api load testing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JE-Chen/Integration-testing-environment",
    packages=setuptools.find_packages(),
    install_requires=[
        "je-editor"
    ],
    extras_require={
        "another_extension": ["je-mail-thunder", "je-tk-plot"]
    },
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Win32 (MS Windows)",
        "Environment :: MacOS X",
        "Environment :: X11 Applications",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)

# python deprecation_dev_setup.py sdist bdist_wheel
# python -m twine upload dist/*
