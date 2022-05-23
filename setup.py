"""
    Butler REST API Documentation

           Welcome to Butler API Documentation and Explorer       Butler API is built on and conforms to Open API 3.0 spec.       This enables you to automatically generate language specific clients for       languages/frameworks listed here: https://openapi-generator.tech/docs/generators/#client-generators         # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "butler"
VERSION = "10.0.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    description="Butler Python SDK",
    author="Butler Labs",
    author_email="support@butlerlabs.ai",
    url="butlerlabs.ai",
    keywords=["Butler", "AutoML", "OCR"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
           Welcome to Butler Python SDK # noqa: E501
    """
)
