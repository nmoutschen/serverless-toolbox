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

| Rule ID                                          | Description                                                          |
|--------------------------------------------------|----------------------------------------------------------------------|
| [E9000](./rules/e9000_lambda_runtime.py)         | Ensure Lambda functions only use authorized runtimes                 |
| [E9001](./rules/e9001_lambda_layers.py)          | Ensure Lambda functions use mandatory layers                         |
| [E9002](./rules/e9002_lambda_tracing.py)         | Ensure Lambda functions have active tracing enabled                  |
| [E9010](./rules/e9010_lambda_esm_destination.py) | Ensure Lambda EventSourceMappings have OnFailure destination         |
| [E9100](./rules/e9100_apigateway_log.py)         | Ensure API Gateway REST and HTTP APIs have logging enabled           |
| [E9101](./rules/e9101_apigateway_tracing.py)     | Ensure API Gateway REST APIs have tracing enabled                    |
| [E9200](./rules/e9200_stepfunctions_log.py)      | Ensure Step Functions state machines have logging enabled            |
| [E9201](./rules/e9201_stepfunctions_tracing.py)  | Ensure Step Functions state machines have tracing enabled            |
| [E9300](./rules/e9300_appsync_tracing.py)        | Ensure AppSync GraphQL APIs have tracing enabled                     |
