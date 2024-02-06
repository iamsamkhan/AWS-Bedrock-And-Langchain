import setuptools

# with open("README.md", "r", encoding="utf-8") as f:
#     long_description = f.read()
    
    
    
def _get_description():
    path = pathlib.Path(__file__).parent / 'README.md'
    with open(path, encoding='utf-8') as f:
        long_description = f.read()
    return long_description


def _get_requirements(path):
    with open(path) as f:
        data = f.readlines()
    return data


setup(
    name='AWS-Bedrock-And-Langchain',
    version='0.2.8',
    author='shamshad ahmed',
    url='https://github.com/iamsamkhan/AWS-Bedrock-And-Langchain.git',
    python_requires='>=3.10',
    install_requires=_get_requirements('requirements.txt'),
    packages=find_packages(exclude=('tests', )),
    include_package_data=True,
    entry_points={
        'AWS_Bedrock': [
            'AWS_Bedrock=main',
        ],
    },
    description='End To End Advanced RAG App Using AWS Bedrock And Langchain',
    long_description=__get_long_description(),
    long_description_content_type='text/markdown',
    url=f"https://github.com/iamsamkhan/AWS-Bedrock-And-Langchain.git/{author}/{name}",
    url=f"https://github.com/iamsamkhan/AWS-Bedrock-And-Langchain.git/{author}/{name}",
    project_urls={
         "Bug Tracker": f"https://github.com/iamsamkhan/AWS-Bedrock-And-Langchain.git/{author}/{name}/issues",
     },
     package_dir={"": "AWS_Bedrock"},
    packages=setuptools.find_packages(where="AWS_Bedrock")

)