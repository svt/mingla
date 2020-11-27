import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    install_requires = fh.read()

setuptools.setup(
    name="mingla",
    version="0.9.0",
    author="Stefan Berggren",
    author_email="stefan.berggren@svt.se",
    description=" Mingla is a Slack bot written to stimulate random conversations between colleagues during remote work.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/svt/mingla",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=install_requires,
    entry_points={
        'console_scripts': ['mingla=mingla.main:main']
    },
)
