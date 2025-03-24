import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
__version__= "0.0.0"

REPO_NAME = "Text-summarizer"
AUTHOR_USER_NAME = "sps2604"
SRC_REPO = "textsummarizer"
AUTHOR_EMAIL ="shrishsoman26@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version= __version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A text summarizer using transformers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Documentation": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/blob/main/README.md",
        "Source Code": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
        "Issue Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir=("","src"),
    packages=setuptools.find_packages(where="src")

)