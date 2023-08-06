import os
import json
import dataclasses
import setuptools
import pkg_resources
from typing import Optional


def get_version(dirpath: str):
    version_path = f"{dirpath}/version.py"
    exec(compile(open(version_path, encoding="utf-8").read(), version_path, "exec"))
    return locals()["__version__"]


def get_requirements(dirpath: str):
    requirements_path = os.path.join(dirpath, "requirements.txt")
    requirements = pkg_resources.parse_requirements(open(requirements_path))
    return list(map(str, requirements))


@dataclasses.dataclass(frozen=False, order=True)
class PackageSetup:
    github_username: str
    name: Optional[str] = None
    py_modules: Optional[list[str]] = None
    version: Optional[str] = None
    description: Optional[str] = None
    long_description: Optional[str] = None
    package_setup_path: Optional[str] = None
    dirpath: Optional[str] = None
    entry_points: dict = {}
    url: Optional[str] = None
    license: str = "MIT"
    python_version: str = "3.8"
    packages: Optional[list[str]] = None
    python_requires: Optional[str] = None
    include_package_data: bool = True
    install_requires: Optional[list[str]] = None
    long_description_content_type: str = "text/markdown"
    extras_require: dict = {"dev": ["pytest", "black", "flake8", "isort"]}

    def __postinit__(self):
        assert (
            self.dirpath is not None or self.package_setup_path is not None
        ), "unable to locate package origin"

        if self.dirpath is None or not self.dirpath:
            self.dirpath = os.path.dirname(self.package_setup_path)

        if self.name is None or not self.name:
            self.name = (
                self.dirpath[self.dirpath.rindex("/") + 1 :]
                if "/" in self.dirpath
                else self.dirpath
            )

        if self.url is None or not self.url:
            self.url = f"https://github.com/{self.github_username}/{self.name}.git"

        if self.python_requires is None or not self.python_requires:
            self.python_requires = f">={self.python_version}"

        self.version = get_version(self.dirpath)

        if self.install_requires is None or not self.install_requires:
            self.install_requires = get_requirements(self.dirpath)

        if self.description is None or not self.description:
            self.description = open(
                f"{self.dirpath}/README.md", encoding="utf-8"
            ).read()

        if self.long_description is None or not self.long_description:
            self.long_description = self.description

        if self.py_modules is None or not self.py_modules:
            self.py_modules = [self.name]

        if self.packages is None or not self.packages:
            self.packages = setuptools.find_packages(exclude=["tests*"])

    def dict(self):
        return {key: getattr(self, key) for key in self.__dataclass_fields__.keys()}

    def kwargs(self):
        return {key: value for key, value in self.dict().items() if value is not None}

    def json(self, indent: int = 0):
        return json.dumps(self.dict(), indent=indent)

    def setup(self):
        setuptools.setup(**self.kwargs())
