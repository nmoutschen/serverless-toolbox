STACK_NAME ?= "st-$(shell basename $(PWD))"
S3_BUCKET ?= $(shell ../bin/get-artifact-bucket)
ID ?= "test"

deploy:
	sam deploy --stack-name $(STACK_NAME) --s3-bucket $(S3_BUCKET) --capabilities CAPABILITY_IAM

store:
	aws dynamodb put-item --table-name $(shell aws cloudformation describe-stacks --stack-name $(STACK_NAME) --query 'Stacks[0].Outputs[?OutputKey==`TableName`].OutputValue' --output text) --item '{"id": {"S": "$(ID)"}, "message": {"S": "$(MESSAGE)"}}'

run:
	@./run.sh $(STACK_NAME) $(ID)

delete:
	aws cloudformation delete-stack --stack-name $(STACK_NAME)
