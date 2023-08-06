import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mayagpt",
    version="1.0.3",
    author= 'Mahmoud Ellithy',
    author_email='cmy.mahmoud@hotmail.com',
    project_urls={
        "Homepage": "https://github.com/MahmoudGFX/mayagpt",
    },
    packages=setuptools.find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    license="MIT",  # Replace "MIT" with the appropriate SPDX identifier for your license
    install_requires=["setuptools", "wheel", "PySide2", "openai", "requests"],
)
    