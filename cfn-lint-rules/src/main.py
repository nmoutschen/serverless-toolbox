import json
import os
import boto3
import cfnlint.core
from cfnlint.decode.cfn_json import CfnJSONDecoder


FAIL_ORDER = ["E", "W", "I"]
FAIL_LEVEL = FAIL_ORDER.index(os.environ.get("FAIL_LEVEL", "E"))
LAMBDA_TASK_ROOT = os.environ["LAMBDA_TASK_ROOT"]
RULES_FOLDER = f"{LAMBDA_TASK_ROOT}/rules"
RULES = cfnlint.core.get_rules([RULES_FOLDER], [], [])


region_name = boto3.Session().region_name
cloudformation = boto3.client("cloudformation")


def handler(event, context):
    """
    Lambda function handler
    """

    stack_name = event["stackName"]
    template = cloudformation.get_template(StackName=stack_name, TemplateStage="Processed")["TemplateBody"]
    template = json.loads(json.dumps(template), cls=CfnJSONDecoder)


    matches = cfnlint.core.run_checks(
        "template.json",
        template,
        RULES,
        [region_name]
    )

    matches = [
        {
            "id": match.rule.id,
            "message": match.message,
            "path": "/".join(match.path)
        }
        for match in matches
        if FAIL_ORDER.index(match.rule.id[0]) <= FAIL_LEVEL
    ]

    return matches
