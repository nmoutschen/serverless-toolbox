"""
Custom rule to ensure Lambda functions use the mandatory layers
"""


import functools
import re
from cfnlint.rules import CloudFormationLintRule, RuleMatch


MANDATORY_LAYERS = [
    # Customize this to set the list of mandatory layers
    re.compile(r"arn:aws:lambda:[^:]+:580247275435:layer:LambdaInsightsExtension:2")
]


def check_layer(layer_name):
    return 


class LambdaLayersRule(CloudFormationLintRule):
    id = "E9001"
    shortdesc = "Lambda Mandatory Layers"
    description = "Ensure that Lambda functions use the mandatory layers"
    tags = ["lambda"]

    _message = "Lambda function {} is missing one or more mandatory layer(s)"

    def match(self, cfn):
        """
        Match against Lambda functions not using the mandatory layers
        """

        matches = []

        # Scan through Lambda functions
        for key, value in cfn.get_resources(["AWS::Lambda::Function"]).items():
            layers = value.get("Properties", {}).get("Layers", [])

            # Check if all mandatory layers are present
            has_all_layers = functools.reduce(
                lambda x, y: x and y,
                [
                    functools.reduce(
                        lambda x, y: x or y,
                        [bool(ml.match(l)) for l in layers]
                    )
                    for ml in MANDATORY_LAYERS
                ]
            )

            if not has_all_layers:
                matches.append(RuleMatch(
                    ["Resources", key],
                    self._message.format(key)
                ))

        return matches
