"""
Custom rule to ensure API Gateway REST APIs have tracing enabled
"""


from cfnlint.rules import CloudFormationLintRule, RuleMatch


class ApiGatewayTracingRule(CloudFormationLintRule):
    id = "E9101"
    shortdesc = "API Gateway REST API Tracing"
    description = "Ensure that API Gateway REST APIs have tracing enabled"
    tags = ["apigateway"]

    _message = "API Gateway Stage {} does not have tracing enabled"

    def match(self, cfn):
        """
        Match against API Gateway stages that don't have tracing enabled
        """

        matches = []

        # Scan through API Gateway logs
        for key, value in cfn.get_resources(["AWS::ApiGateway::Stage"]).items():
            tracing = value.get("Properties", {}).get("TracingEnabled", False)

        if not tracing:
            matches.append(RuleMatch(
                ["Resources", key],
                self._message.format(key)
            ))

        return matches
