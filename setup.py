import setuptools

# reading README.md file
# important for publishing project as package on PyPy
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# package version
__version__ = "0.0.0"

# required variables for local package setup
REPO_NAME = "NLP_TextSummarizer"
AUTHOR_USER_NAME = "sg13041995"
SRC_REPO = "TextSummarizer"
AUTHOR_EMAIL = "subhankar.github.130495@gmail.com"

# local package setup
# look for constructor file in each local folders and install it as package
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Python package for Text Summarizer NLP application",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)