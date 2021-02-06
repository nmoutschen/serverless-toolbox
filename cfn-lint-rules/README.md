CloudFormation linting rules
============================

This contains custom rules for the [`cfn-lint`](https://github.com/aws-cloudformation/cfn-python-lint) tool.

## Usage

To use custom rules with `cfn-lint`, you will need to create a folder containing the python files relevant for you. From there, you can use the CLI with the `--append-rules` option.

```
export $TEMPLATE_FILE=template.yaml
export $RULES_FOLDER=some/folder/with/custom/rules/

cfn-lint $TEMPLATE_FILE --append-rules $RULES_FOLDER
```

## Remark

All rules in this folder have an id in the form __E9xxx__, meaning that failure to comply with a rule will result in an error. You should customize the rule IDs based on your requirements and preferences. See the [cfn-lint documentation on rules](https://github.com/aws-cloudformation/cfn-python-lint/blob/master/docs/rules.md) to learn more.

## Available rules

| Rule ID                            | Description                                                          |
|------------------------------------|----------------------------------------------------------------------|
| [E9000](./e9000_lambda_runtime.py) | Ensure Lambda functions only use authorized runtimes                 |
| [E9001](./e9001_lambda_layers.py)  | Ensure Lambda functions use mandatory layers                         |
| [E9002](./e9002_lambda_tracing.py) | Ensure Lambda functions have active tracing enabled                  |
| [E9010](./e9010_lambda_esm_destination.py) | Ensure Lambda EventSourceMappings have OnFailure destination |
| [E9100](./e9100_apigateway_log.py) | Ensure API Gateway REST APIs have logging enabled                    |
| [E9101](./e9101_apigateway_tracing.py) | Ensure API Gateway REST APIs have tracing enabled                |
