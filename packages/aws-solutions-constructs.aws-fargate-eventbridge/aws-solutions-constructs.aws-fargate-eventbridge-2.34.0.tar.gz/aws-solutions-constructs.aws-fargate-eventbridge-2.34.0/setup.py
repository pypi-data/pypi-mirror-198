import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "aws-solutions-constructs.aws-fargate-eventbridge",
    "version": "2.34.0",
    "description": "CDK Constructs for AWS Fargate to Amazon Eventbridge integration",
    "license": "Apache-2.0",
    "url": "https://github.com/awslabs/aws-solutions-constructs.git",
    "long_description_content_type": "text/markdown",
    "author": "Amazon Web Services",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/awslabs/aws-solutions-constructs.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "aws_solutions_constructs.aws_fargate_eventbridge",
        "aws_solutions_constructs.aws_fargate_eventbridge._jsii"
    ],
    "package_data": {
        "aws_solutions_constructs.aws_fargate_eventbridge._jsii": [
            "aws-fargate-eventbridge@2.34.0.jsii.tgz"
        ],
        "aws_solutions_constructs.aws_fargate_eventbridge": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.7",
    "install_requires": [
        "aws-cdk-lib>=2.68.0, <3.0.0",
        "aws-solutions-constructs.core==2.34.0",
        "constructs>=10.0.0, <11.0.0",
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
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
