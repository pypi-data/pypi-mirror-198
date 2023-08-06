import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "fantasy-hockey-notifier-cdk",
    "version": "2.0.62",
    "description": "AWS CDK construct to send notifications for adds, drops, and trades in an ESPN Fantasy Hockey league",
    "license": "MIT",
    "url": "https://github.com/ftalburt/fantasy-hockey-notifier-cdk.git#readme",
    "long_description_content_type": "text/markdown",
    "author": "Forrest Talburt",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/ftalburt/fantasy-hockey-notifier-cdk.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "fantasy_hockey_notifier_cdk",
        "fantasy_hockey_notifier_cdk._jsii"
    ],
    "package_data": {
        "fantasy_hockey_notifier_cdk._jsii": [
            "fantasy-hockey-notifier-cdk@2.0.62.jsii.tgz"
        ],
        "fantasy_hockey_notifier_cdk": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.7",
    "install_requires": [
        "aws-cdk-lib>=2.30.0, <3.0.0",
        "cdk-iam-floyd>=0.494.0, <0.495.0",
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
