from setuptools import setup, find_packages

name = "nextcloud-tasks-api"
package = name.replace("-", "_")
packages = [package] + [package + "." + _ for _ in find_packages(where=package)]
extra = "cli"
url = "https://www.hackitu.de/nextcloud_tasks_api/"

setup(
    name=name,
    version="0.1",
    description="Nextcloud Tasks API and CLI.",
    classifiers=["License :: OSI Approved :: GNU Affero General Public License v3"],
    author=url,
    author_email="@",
    url=url,

    packages=packages,
    install_requires=[
        "requests"
    ],
    extras_require={extra: [
        "questionary"
    ]},
    entry_points={"console_scripts": [
        "{}={}.{}.__main__:main".format(name, package, extra),
    ]},
)
