"""
Custom rule to ensure AppSync GraphQL APIs have tracing enabled
"""


from cfnlint.rules import CloudFormationLintRule, RuleMatch


class AppSyncTracingRule(CloudFormationLintRule):
    id = "E9300"
    shortdesc = "AppSync Tracing"
    description = "Ensure that AppSync GraphQL APIs have tracing enabled"
    tags = ["appsync"]

    _message = "AppSync GraphQL API {} does not have X-Ray enabled"

    def match(self, cfn):
        """
        Matching against AppSync GraphQL APIs without tracing enabled
        """

        matches = []

        for key, value in cfn.get_resources(["AWS::AppSync::GraphQLApi"]).items():
            tracing = value.get("Properties", {}).get("XrayEnabled", False)

            if not tracing:
                matches.append(RuleMatch(
                    ["Resources", key],
                    self._message.format(key)
                ))

        return matches
