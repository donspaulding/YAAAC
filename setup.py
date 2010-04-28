from setuptools import setup, find_packages
setup(
    name = "YAAAC",
    version = "0.2.0",
    packages = find_packages(),

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires = ['suds'],

    # metadata for upload to PyPI
    author = "Don Spaulding",
    author_email = "donspauldingii@gmail.com",
    description = "YAAAC is Yet Another Adwords Api Cliente",
    license = "BSD",
    keywords = "suds google client api SOAP ",
    url = "http://github.com/donspaulding/yaaac/",   # project home page, if any
)

