import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cdk-http-pinger",
    "version": "0.1.222",
    "description": "HTTP Pinger for AWS CDK",
    "license": "Apache-2.0",
    "url": "https://github.com/pahud/cdk-http-pinger.git",
    "long_description_content_type": "text/markdown",
    "author": "Pahud Hsieh<pahudnet@gmail.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/pahud/cdk-http-pinger.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdk_http_pinger",
        "cdk_http_pinger._jsii"
    ],
    "package_data": {
        "cdk_http_pinger._jsii": [
            "cdk-http-pinger@0.1.222.jsii.tgz"
        ],
        "cdk_http_pinger": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.7",
    "install_requires": [
        "aws-cdk-lib>=2.1.0, <3.0.0",
        "constructs>=10.0.5, <11.0.0",
        "jsii>=1.78.1, <2.0.0",
        "publication>=0.0.3",
        "typeguard~=2.13.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
