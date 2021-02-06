"""
Custom rule to ensre Step Function State Machines have logging enabled
"""


from cfnlint.rules import CloudFormationLintRule, RuleMatch


class StepFunctionsLogRule(CloudFormationLintRule):
    id = "E9200"
    shortdesc = "Step Functions Logs"
    description = "Ensure that Step Functions State Machines have logging enabled"
    tags = ["stepfunctions"]

    _message_logging_config = "Step Functions state machine {} is missing logging configuration"
    _message_log_level = "The logging level for Step Functions state machine {} is set to OFF"

    def match(self, cfn):
        """
        Matching against Step Functions state machines without logging configuration
        """

        matches = []

        # Scan through Step Functions state machines
        for key, value in cfn.get_resources(["AWS::StepFunctions::StateMachine"]).items():
            logging_config = value.get("Properties", {}).get("LoggingConfiguration", {})
            log_level = logging_config.get("Level", "OFF")

            if not logging_config:
                # LoggingConfiguration is not present
                matches.append(RuleMatch(
                    ["Resources", key],
                    self._message_logging_config.format(key)
                ))
            elif log_level == "OFF":
                # LoggingConfiguration is presentm but the Level is set to
                # 'OFF' or omitted
                matches.append(RuleMatch(
                    ["Resources", key],
                    self._message_log_level.format(key)
                ))

        return matches
