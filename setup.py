import os
import re
from setuptools import setup
import subprocess
import sys
from setuptools.command.install import install

__author__ = "Chetan Jain <chetan@omkar.cloud>"


install_requires = [
    "javascript",
]
extras_require = {}


def get_description():
    try:
        with open("README.md", encoding="utf-8") as readme_file:
            long_description = readme_file.read()
        return long_description
    except:
        return None


def install_npm_package(package_name):
    """Install an npm package using a Python module, suppressing the output and handling errors."""

    try:
        subprocess.run([sys.executable, "-m", "javascript", "--install", package_name], 
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE
                           )

    except Exception as e:
        pass

    # This really loads it up.
    try:
        from javascript import require

        pkg = require(package_name)
    except Exception as e:
        pass


def extract_number(s):
    if isinstance(s, str):
        # Use regular expression to find all numbers in the text
        numbers = re.findall(r"\b\d+(?:\.\d+)?\b", s)
        # Convert the extracted strings to floats or integers
        ls = [float(num) if "." in num else int(num) for num in numbers]

        return ls[0] if ls else None

    if isinstance(s, int) or isinstance(s, float):
        return s


def check_node():
    try:
        NODE_BIN = os.environ.get("NODE_BIN") or (
            getattr(os.environ, "NODE_BIN")
            if hasattr(os.environ, "NODE_BIN")
            else "node"
        )
        node_version = subprocess.check_output(
            [NODE_BIN, "-v"], universal_newlines=True
        ).replace("v", "")
        major_version = int(extract_number(node_version))

        MIN_VER = 16
        if major_version < MIN_VER:
            print(
                f"Your Node.js version is {major_version}, which is less than {MIN_VER}. To use the stealth and auth proxy features of Botasaurus, you need Node.js 18, Kindly install it by visiting https://nodejs.org/"
            )
            sys.exit(1)
    except Exception as e:
        print(
            "You do not have node installed on your system, Kindly install it by visiting https://nodejs.org/"
        )
        sys.exit(1)


def pre_install():
    check_node()


def post_install():
    install_npm_package("proxy-chain")


class PostInstallCommand(install):
    """Post-installation for installation mode."""


    def run(self):
        # Run the standard install
        super().run()

        print("Installing needed npm packages")
        post_install()


pre_install()

setup(
    name="botasaurus_proxy_authentication",
    version="1.0.8",
    author="Chetan Jain",
    author_email="chetan@omkar.cloud",
    description="Proxy Server with support for SSL, proxy authentication and upstream proxy.",
    license="MIT",
    keywords=["seleniumwire proxy authentication", "proxy authentication"],
    url="https://github.com/omkarcloud/botasaurus-proxy-authentication",
    packages=["botasaurus_proxy_authentication"],
    long_description_content_type="text/markdown",
    long_description=get_description(),
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
