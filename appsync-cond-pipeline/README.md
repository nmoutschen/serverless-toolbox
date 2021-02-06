AWS AppSync Conditional Pipeline
================================

This is a simple application with a conditional resolver pipeline in AWS AppSync. It will first try to fetch an item from a DynamoDB table. If that item doesn't exist, it will then run a Lambda function to retrieve the correct result.

## Usage

```bash
# Deploy the CloudFormation template
make

# Store an item in DynamoDB
make store ID=hello MESSAGE="Hello from DynamoDB!"

# Make a query against the GraphQL API
# This will retrieve the item in DynamoDB
make run ID=hello
# Since there's no item with id 'hello2' in DynamoDB, this will run the Lambda
# function instead
make run ID=hello2

# Delete the stack
make delete
```
