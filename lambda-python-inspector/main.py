import os
import sys
from typing import Dict, List, Tuple


import boto3
import botocore


def get_environ() -> Dict[str, str]:
    """
    Return the environment variables as key-value pairs
    """

    return {
        k: v for k, v in os.environ.items()
    }


def get_module_versions() -> Dict[str, str]:
    """
    Return the version of python modules
    """

    return {
        "boto3": boto3.__version__,
        "botocore": botocore.__version__
    }


def get_mounts() -> List[Tuple[str]]:
    """
    Return the list of mounts as (device, mountpoint) pairs
    """

    with open("/proc/mounts", "r") as mountfile:
        return [tuple(v.split(" ", 2)[:2]) for v in mountfile.readlines()]


def get_python_version() -> str:
    """
    Return the Python function version
    """

    return "{}.{}.{}".format(
        sys.version_info.major,
        sys.version_info.minor,
        sys.version_info.micro
    )


def get_writeable_files() -> List[str]:
    """
    Return a list of writeable files and folders
    """

    EXCLUDE_DIRS = ["dev", "proc", "sys"]
    UID = os.getuid()
    GIDS = os.getgroups()

    def check_file(filename):
        file_stat = os.stat(filename)

        # World write permission
        if file_stat.st_mode & 0o002 != 0:
            return True

        # Group write permission
        if file_stat.st_gid in GIDS and file_stat.st_mode & 0o020 != 0:
            return True

        # User write permission
        if file_stat.st_uid == UID and file_stat.st_mode & 0o200 != 0:
            return True

        return False

    retval = []

    for root, dirs, files in os.walk("/"):
        if root == "/":
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

        # Checking folders
        for d in dirs:
            dir = os.path.join(root, d)
            try:
                if check_file(dir):
                    retval.append(dir)
            except:
                pass

        # Checking files
        for f in files:
            file = os.path.join(root, f)
            try:
                if check_file(file):
                    retval.append(file)
            except:
                pass

    return retval


def handler(event, context):
    """
    Lambda function handler
    """

    retval = {
        "environ": get_environ(),
        "pythonVersion": get_python_version(),
        "moduleVersions": get_module_versions(),
        "mounts": get_mounts(),
        "writeableFiles": get_writeable_files(),
    }

    return retval