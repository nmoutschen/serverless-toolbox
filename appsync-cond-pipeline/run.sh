#!/bin/bash

set -e

function finish {
    if [ -n "$API_KEY" ]; then
        aws appsync delete-api-key --api-id $API_ID --id $API_KEY
    fi
}

trap finish EXIT

# Retrieve values from CloudFormation
STACK_NAME=$1
ITEM_ID=${2:-test}
API_ID=$(aws cloudformation describe-stacks --stack-name $STACK_NAME --query 'Stacks[0].Outputs[?OutputKey==`ApiId`].OutputValue' --output text)
API_URL=$(aws cloudformation describe-stacks --stack-name $STACK_NAME --query 'Stacks[0].Outputs[?OutputKey==`ApiUrl`].OutputValue' --output text)

# Create an API Key
API_KEY=$(aws appsync create-api-key --api-id $API_ID --query 'apiKey.id' --output text)

# Make a query
curl -XPOST -H "Content-Type:application/graphql" -H "x-api-key:${API_KEY}" -d '{"query": "query { getValue (id: \"'${ITEM_ID}'\") { message }}"}' $API_URL ; echo
