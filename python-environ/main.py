import os

def handler(event, context):
    return {
        k: v for k, v in os.environ.items()
    }