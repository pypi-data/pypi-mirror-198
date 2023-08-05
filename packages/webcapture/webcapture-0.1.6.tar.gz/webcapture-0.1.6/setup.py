import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="webcapture",
    version="0.1.6",
    author="Collinsss",
    description="A package for capturing website screenshots using Pyppeteer.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/collinsss/webcapture",
    project_urls={
        "Bug Tracker": "https://github.com/collinsss/webcapture/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "asyncio>=3.4.3",
        "pyppeteer>=0.2.2",
        "beautifulsoup4>=4.9.3",
        "requests>=2.25.1"
    ]
)
