from setuptools import setup
from setuptools.command.install import install
import subprocess
import sys

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


class PostInstallCommand(install):
    """Post-installation for installation mode."""

    def install_npm_package(self, package_name):
        """Install an npm package using a Python module, suppressing the output and handling errors."""
        try:
            subprocess.run(
                [sys.executable, "-m", "javascript", "--install", package_name],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
        except Exception as e:
            # Log the error if needed
            pass
            # print(f"An error occurred while installing {package_name}: {e}")

        # This really loads it up.
        try:
            from javascript import require

            pkg = require(package_name)
        except Exception as e:
            pass

    def run(self):
        # Run the standard install
        super().run()

        print("Installing needed npm packages")
        # Install each npm package
        self.install_npm_package("proxy-chain")


setup(
    name="botasaurus_proxy_authentication",
    version="1.0.1",
    author="Chetan Jain",
    author_email="chetan@omkar.cloud",
    cmdclass={"install": PostInstallCommand},
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
