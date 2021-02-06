"""
Custom rule to ensure Lambda functions with Event Source Mapping have a
DestinationConfig with OnFailure destination
"""


from cfnlint.rules import CloudFormationLintRule, RuleMatch


class LambdaESMDestinationRule(CloudFormationLintRule):
    id = "E9010"
    shortdesc = "Lambda EventSourceMapping OnFailure"
    description = "Ensure that Lambda Event Source Mapping have a DestinationConfig with OnFailure destination"
    tags = ["lambda"]

    _message = "Event Source Mapping {} does not have a DestinationConfig with OnFailure destination"

    def match(self, cfn):
        """
        Match EventSourceMapping that don't have a DestinationConfig with OnFailure
        """

        matches = []

        sources = cfn.get_resources("AWS::Lambda::EventSourceMapping")

        # Scan through Event Source Mappings
        for key, resource in sources.items():
            if resource.get("Properties", {}).get("DestinationConfig", {}).get("OnFailure", None) is None:
                matches.append(RuleMatch(
                    ["Resources", key],
                    self._message.format(key)
                ))

        return matches
