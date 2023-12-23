# coding: utf-8
import os
import sys

from setuptools import setup

__author__ = "Chetan Jain <chetan@omkar.cloud>"


install_requires = [
    "javascript",
]
extras_require = {}
with open("README.md") as readme_file:
    long_description = readme_file.read()


# 'setup.py publish' shortcut.
if sys.argv[-1] == "publish":
    os.system("python3 setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    sys.exit()
elif sys.argv[-1] == "clean":
    import shutil

    if os.path.isdir("build"):
        shutil.rmtree("build")
    if os.path.isdir("dist"):
        shutil.rmtree("dist")
    if os.path.isdir("botasaurus_proxy_authentication.egg-info"):
        shutil.rmtree("botasaurus_proxy_authentication.egg-info")


setup(
    name="botasaurus_proxy_authentication",
    version="1.0.0",
    author='Chetan Jain',
    author_email='chetan@omkar.cloud',
    description="Proxy Server with support for SSL, proxy authentication and upstream proxy.",
    license="MIT",
    keywords="proxy authentication, seleniumwire proxy authentication",
    url="https://github.com/omkarcloud/botasaurus_proxy_authentication",
    packages=["botasaurus_proxy_authentication"],
    long_description_content_type="text/markdown",
    long_description=long_description,
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development :: Testing",
        "Topic :: System :: Installation/Setup",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    install_requires=install_requires,
    extras_require=extras_require,
)
