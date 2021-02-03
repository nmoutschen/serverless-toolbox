Lambda Python Inspector
=======================

This tool contains a Lambda function that will inspect the Lambda execution environment. This will run multiple checks and return a JSON object containing the following information:

* __environ__: Key-value pairs for the environment variables
* __pythonVersion__: Current python version
* __moduleVersions__: Versions of the boto3 and botocore Python modules
* __writeableFiles__: Array of all writeable files and folders in the execution environment

## Usage

```bash
# Deploy the Lambda function
make

# Run a single invoke and display its result
make run

# Delete the Lambda function
make delete
```