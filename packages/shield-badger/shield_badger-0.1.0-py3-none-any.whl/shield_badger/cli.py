# -*- coding: utf-8 -*-
"""Generate shield.io badges for a git repository."""
import json
import logging
import os
from typing import Optional

import click
import tomllib

from shield_badger import __version__, settings, utils

CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}


@click.group(context_settings=CONTEXT_SETTINGS, invoke_without_command=True)
@click.argument("path", default=settings.CWD, type=click.Path(exists=True))
@click.option("-v", "--verbose", count=True, help="More verbose output.")
@click.option(
    "-V",
    "--version",
    is_flag=True,
    default=False,
    help="Show program's version number and exit.",
)
def main(path: str = settings.CWD, version: bool = False, verbose: int = 0) -> None:
    """Generate shield.io badges for a git repository and inject them into the README."""
    if version:
        print(f"badge-inject ({__version__})")
    match verbose:
        case 1:
            log_level = "INFO"
        case 2:
            log_level = "DEBUG"
        case _:
            log_level = settings.LOG_LEVEL
    logging.basicConfig(level=log_level)
    logging.info("Log level: %s", log_level)
    logging.debug("Repo path: %s", path)


class BadgeGenerator:
    """Methods to help find info for badges and generate them"""

    def __init__(self, path: str = settings.CWD):
        self.path = path
        self.badges: list = []

    @staticmethod
    def contains_badge_hooks(file_path: str) -> bool:
        """Checks wether or not a file contains the start/end badge hooks"""
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        return settings.START_BADGE_HOOK in content and settings.END_BADGE_HOOK in content

    def prepend_readme_with_badges(self) -> None:
        """Prepends README.md with badges.

        Only necessary on first run when injection site is not yet defined.
        """
        badge_str = " ".join(self.badges)
        with open("filename", "r", encoding="utf-8") as original:
            data = original.read()
        with open("filename", "w", encoding="utf-8") as modified:
            modified.write(f"{settings.START_BADGE_HOOK}\n{badge_str}\n{settings.END_BADGE_HOOK}\n\n" + data)

    def inject_readme_with_badges(self, path: Optional[str] = None) -> None:
        """Inject badges into readme at injection site

        Injection site is denoted by the following readme comment tags:
        shield_badger.settings.START_BADGE_HOOK
        shield_badger.settings.END_BADGE_HOOK

        Old badge content in between these comment tags is cleared and
        replaced with badges stores in the self.badge attribute of this class.
        """
        path = path if path else f"{self.path}/README.md"
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()

        start_pos = content.find(settings.START_BADGE_HOOK)
        end_pos = content.find(settings.END_BADGE_HOOK)

        if start_pos != -1 and end_pos != -1:
            badge_content = " ".join(self.badges)
            updated_content = f"{content[:start_pos + len(settings.START_BADGE_HOOK)]}\n" \
                f"{badge_content}\n" \
                f"{content[end_pos:]}"
        else:
            print(f"Badge hooks not found in the file: '{path}'")

        with open(path, "w", encoding="utf-8") as file:
            file.write(updated_content)

    @staticmethod
    def generate_badge(
        left_txt: str, right_txt: str, color: str, name: Optional[str] = None, logo: Optional[str] = None, url: str = ""
    ) -> str:
        """Generate markdown formatted shield.io badge

        Args:
            left_txt (str): Text for the left side of the badge
            right_txt (str): Text for the right side of the badge
            color (str): Background color for the right side of the badge
            name (Optional[str], optional): Name to give the badge. Defaults to left_txt.
            logo (Optional[str], optional): Icon to add to the left side of the badge.
                                            Supported logos can be found at https://simpleicons.org/. Defaults to None.
            url (str, optional): Hyperlink to attach to the badge. Defaults to ''.

        Returns:
            str: Markdown formatted shields.io badge ready for use in a README.md
        """
        name = name if name else left_txt
        badge = f"[![{name}](https://img.shields.io/badge/{left_txt}-{right_txt}-{color}"
        if logo:
            badge = f"{badge}?logo={logo})]"
        else:
            badge = f"{badge})]"
        badge = f"{badge}({url})"
        return badge

    def get_python_version(self) -> Optional[str]:
        """Get python version from pyproject.yaml if it exists in the repo

        Returns:
            Optional[str]: Returns python version if it can be deciphered.
        """
        pyproject_path = f"{self.path}/pyproject.toml"
        file_exists = os.path.exists(pyproject_path)
        if not file_exists:
            return None
        with open(pyproject_path, "rb") as file:
            data = tomllib.load(file)
            python_version = list(utils.get_recursively(data, "python"))
            return python_version[0] if len(python_version) > 0 else None

    def get_license_info(self, file_path: str = "") -> Optional[str]:
        """Search for lincense info in a variety of standard project metadata manifests"""
        if file_path == "":
            pyproject = os.path.join(self.path, "pyproject.toml")
            npm_package = os.path.join(self.path, "package.json")
            if os.path.isfile(pyproject):
                file_path = pyproject
            elif os.path.isfile(npm_package):
                file_path = npm_package

        if os.path.isfile(file_path):
            with open(file_path, "rb") as file:
                _, extension = os.path.splitext(file_path)
                if extension == ".toml":
                    data = tomllib.load(file)
                    license_info = list(utils.get_recursively(data, "license"))
                elif extension == ".json":
                    data = json.load(file)
                    license_info = list(utils.get_recursively(data, "license"))
                else:
                    license_info = None
        else:
            license_info = None

        license_info = license_info[0] if (license_info and len(license_info) > 0) else None
        return license_info

    def load_badges(self) -> None:
        """Collect all available badge info and load into self.badges attribute"""
        python_version = self.get_python_version()
        if python_version:
            self.badges.append(self.generate_badge("python", python_version, "blue", logo="python"))
