import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "AWS-Bedrock-And-Langchain"
AUTHOR_USER_NAME = "shamshad ahmed"
SRC_REPO = "AWS_Bedrock"
AUTHOR_EMAIL = "smshad0001@gmail.com"


setuptools.setup(
    name=AWS_Bedrock,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="End To End Advanced RAG App Using AWS Bedrock And Langchain",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/iamsamkhan/AWS-Bedrock-And-Langchain.git/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/iamsamkhan/AWS-Bedrock-And-Langchain.git/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "AWS_Bedrock"},
    packages=setuptools.find_packages(where="AWS_Bedrock")
)