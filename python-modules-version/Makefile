STACK_NAME ?= "st-$(shell basename $(PWD))"
S3_BUCKET ?= $(shell ../bin/get-artifact-bucket)

deploy:
	sam deploy --stack-name $(STACK_NAME) --s3-bucket $(S3_BUCKET) --capabilities CAPABILITY_IAM

run:
	@../bin/invoke $$(aws cloudformation describe-stacks --stack-name $(STACK_NAME) --query 'Stacks[0].Outputs[?OutputKey==`Python38Function`].OutputValue' --output text)
	@../bin/invoke $$(aws cloudformation describe-stacks --stack-name $(STACK_NAME) --query 'Stacks[0].Outputs[?OutputKey==`Python37Function`].OutputValue' --output text)
	@../bin/invoke $$(aws cloudformation describe-stacks --stack-name $(STACK_NAME) --query 'Stacks[0].Outputs[?OutputKey==`Python36Function`].OutputValue' --output text)