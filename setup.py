from setuptools import setup, find_packages
PACKAGES = find_packages()

opts = dict(name="mypackage",
            maintainer="Author Name",
            maintainer_email="maintainer@domain.com",
            description="Simple example of a Travis setup",
            long_description="Simple example of a Travis setup",
            url="http://github.com/jakevdp/travis-python-template",
            download_url="http://github.com/jakevdp/travis-python-template",
            license="MIT",
            packages=PACKAGES)


if __name__ == '__main__':
    setup(**opts)
