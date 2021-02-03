"""
Custom rule to ensure that Lambda functions only use authorized runtimes
"""


from cfnlint.rules import CloudFormationLintRule, RuleMatch


AUTHORIZED_RUNTIMES = [
    # Customize this to set the list of authorized runtimes
    "python3.8",
    "nodejs12.x",
    "provided.al2"
]


class LambdaRuntimeRule(CloudFormationLintRule):
    id = "E9000"
    shortdesc = "Authorized Lambda Runtimes"
    description = "Emsire that Lambda functions only use authorized runtimes"
    tags = ["lambda"]

    _message = "Lambda function {} is using runtime {} instead of one of the authorized runtimes ({})"

    def match(self, cfn):
        """
        Match against Lambda functions not using authorized runtimes
        """

        matches = []

        # Scan through Lambda functions
        for key, value in cfn.get_resources(["AWS::Lambda::Function"]).items():
            runtime = value.get("Properties", {}).get("Runtime", None)
            if runtime not in AUTHORIZED_RUNTIMES:
                matches.append(RuleMatch(
                    ["Resources", key],
                    self._message.format(key, runtime, ", ".join(AUTHORIZED_RUNTIMES))
                ))

        return matches
