from setuptools import setup, find_packages


def get_description():
    with open("README.md") as file:
        return file.read()


setup(
    name="NotionLab",
    version="1.0.1",
    keywords=["notion", "kit", "parser", "html", "markdown"],
    description="A kit for Notion based on Notion Python SDK.",
    long_description=get_description(),
    long_description_content_type="text/markdown",
    license="MIT Licence",

    url="https://github.com/ElaBosak233/NotionKit",
    author="ElaBosak233",
    author_email="ElaBosak233@163.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=[
        "notion-client"
    ]
)
