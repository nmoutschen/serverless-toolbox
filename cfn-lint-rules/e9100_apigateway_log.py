"""
Custom rule to ensure API Gateway REST APIs have logging enabled
"""


from cfnlint.rules import CloudFormationLintRule, RuleMatch


class ApiGatewayLogRule(CloudFormationLintRule):
    id = "E9100"
    shortdesc = "API Gateway REST API Logs"
    description = "Ensure that API Gateway REST APIs have logging enabled"
    tags = ["apigateway"]

    _message = "API Gateway stage {} is missing access log settings"

    def match(self, cfn):
        """
        Match against API Gateway stages without log settings
        """

        matches = []

        # Scan through API Gateway logs
        for key, value in cfn.get_resources(["AWS::ApiGateway::Stage", "AWS::ApiGatewayV2::Stage"]).items():
            log_settings = value.get("Properties", {}).get("AccessLogSettings", {}).get("DestinationArn")

            if not log_settings:
                matches.append(RuleMatch(
                    ["Resources", key],
                    self._message.format(key)
                ))

        return matches
