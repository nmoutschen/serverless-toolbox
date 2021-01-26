from sys import version_info

import boto3
import botocore

def handler(event, context):
    version = "{}.{}".format(
        version_info.major,
        version_info.minor
    )

    return {
        "version": version,
        "boto3": boto3.__version__,
        "botocore": botocore.__version__
    }