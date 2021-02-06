"""
Custom rule to ensure Lambda functions have tracing enabled
"""


from cfnlint.rules import CloudFormationLintRule, RuleMatch


class LambdaTracingRule(CloudFormationLintRule):
    id = "E9002"
    shortdesc = "Lambda Tracing"
    description = "Ensure that Lambda functions have tracing enabled"
    tags = ["lambda"]

    _message = "Lambda function {} does not have tracing set to active"

    def match(self, cfn):
        """
        Match against Lambda functions that don't have tracing enabled
        """

        matches = []

        # Scan through Lambda functions
        for key, value in cfn.get_resources(["AWS::Lambda::Function"]).items():
            tracing = value.get("Properties", {}).get("TracingConfig", {}).get("Mode", "")

            if tracing != "Active":
                matches.append(RuleMatch(
                    ["Resources", key],
                    self._message.format(key)
                ))

        return matches
