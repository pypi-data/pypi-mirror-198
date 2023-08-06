import argparse
import datetime
import os
import re
from enum import Enum
import logging
logging.basicConfig(
  format="%(asctime)s - %(levelname)s - %(message)s",
  level=logging.INFO, # show info level logs
  datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)


class ReleaseType(Enum):
    PATCH = "patch"
    MINOR = "minor"
    MAJOR = "major"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--type",
        dest="release_type",
        default=ReleaseType.PATCH,
        type=ReleaseType,
        choices=list(ReleaseType),
        help="Type of release: patch, minor, or major",
    )
    parser.add_argument(
        "--changelog",
        dest="changelog_path",
        default=os.path.join(
            os.getcwd(), "CHANGELOG.md"
        ),
        type=str,
        help="Path to the changelog file",
    )
    parser.add_argument(
        "--v",
        dest="new_version",
        type=str,
        help="Set exact version. It will override the --type value",
    )
    args = parser.parse_args()

    try:
        with open(args.changelog_path, "r") as f:
            content = f.read()

        new_version = get_new_version(content, args.release_type, args.new_version)
        logger.info("Found new version: %s", new_version)
        content = update_changelog_text(content, new_version)
        content = update_changelog_links(content, new_version)

        with open(args.changelog_path, "w") as f:
            f.write(content)

        logger.info("DONE")
    except Exception as e:
        logger.error(e)

def get_new_version(content, release_type, set_value):
    if set_value:
        return set_value

    # Find the current version
    match = re.search(r"\[[Uu]nreleased\]: (.*)/v(.*)\.\.\.(.*)\n", content)
    if match:
        current_version = match.group(2)
        # HEAD = match.group(3)
    else:
        raise Exception("Could not find the current version in the changelog")

    # Determine the new version
    version_parts = current_version.split(".")
    if release_type == ReleaseType.PATCH:
        version_parts[2] = str(int(version_parts[2]) + 1)
    elif release_type == ReleaseType.MINOR:
        version_parts[1] = str(int(version_parts[1]) + 1)
        version_parts[2] = "0"
    elif release_type == ReleaseType.MAJOR:
        version_parts[0] = str(int(version_parts[0]) + 1)
        version_parts[1] = "0"
        version_parts[2] = "0"
    new_version = ".".join(version_parts)
    return new_version

def update_changelog_text(content, new_version):
    # Replace the Unreleased header with the new version header
    today = datetime.datetime.today().strftime("%Y-%m-%d")
    content = re.sub(r"(## \[[Uu]nreleased\])", f"\g<1>\n\n\n## [{new_version}] - {today}", content)
    return content

def update_changelog_links(content, new_version):
    """ Figure out the version from the url as before"""
    unreleased_link_pattern = re.compile(
        r"\[[Uu]nreleased\]:\s*(?P<compare_url>.+)v(?P<prev_version>\d+\.\d+\.\d+)\.\.\.HEAD"
    )
    unreleased_link_match = re.search(unreleased_link_pattern, content)

    if unreleased_link_match:
        compare_url = unreleased_link_match.group("compare_url")
        prev_version = unreleased_link_match.group("prev_version")

        update_changelog_line = f"[Unreleased]: {compare_url}v{new_version}...HEAD"
        insert_line = f"[{new_version}]: {compare_url}v{prev_version}...v{new_version}"

        content = content.replace(
            unreleased_link_match.group(0),
            f"{update_changelog_line}\n{insert_line}",
        )

    return content


if __name__ == "__main__":
    main()
