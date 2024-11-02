import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.1"

REPO_NAME = "FIrstSearchEngine"
AUTHOR_USER_NAME = "Shoraj1551"
SRC_REPO = "FIrstSearchEngine"
AUTHOR_EMAIL = "shorajtomer@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version = __version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description= "Create a basic search engine from scratch",
    long_description=long_description,
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "bug_tracker" == f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)