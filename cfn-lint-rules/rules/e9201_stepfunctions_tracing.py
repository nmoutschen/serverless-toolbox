"""
Custom rule to ensure Step Function State Machines have tracing enabled
"""


from cfnlint.rules import CloudFormationLintRule, RuleMatch


class StepFunctionsTracingRule(CloudFormationLintRule):
    id = "E9201"
    shortdesc = "Step Functions Tracing"
    description = "Ensure that Step Functions state machines have tracing enabled"
    tags = ["stepfunctions"]

    _message = "Step Functions state machine {} is missing tracing configuration"

    def match(self, cfn):
        """
        Matching against Step Functions state machines without tracing configuration
        """

        matches = []

        # Scan through Step Functions state machines
        for key, value in cfn.get_resources(["AWS::StepFunctions::StateMachine"]).items():
            tracing = value.get("Properties", {}).get("TracingConfiguration", {}).get("Enabled", False)

            if not tracing:
                matches.append(RuleMatch(
                    ["Resources", key],
                    self._message.format(key)
                ))

        return matches
