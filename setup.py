import setuptools

setuptools.setup(
    name="jenkins-handler",
    version="1.0.0",
    author="Tomer Cohen",
    author_email="tomerthetester@gmael.com",
    description="A Wrapper for Jenkins API",
    long_description_content_type="text/markdown",
    url="https://github.com/TomerCohen95/JenkinsHandler",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
