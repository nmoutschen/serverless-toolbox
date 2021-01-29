Amazon CloudWatch Logs Insights queries
=======================================

## Billed duration in GB-s

Calculated the total billed duration in GB-s over 5 minutes interval periods.

```
filter @type = "REPORT"
| stats sum(@billedDuration)/1000 * avg(@memorySize)/1024000000 as billedGBs by @log, bin(5m)
```

## Latest 20 errors or warnings

Displays the last 20 error or warning log entries.

__Note:__ this requires using structured logging. See [this section of the Serverless Lens](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/centralized-and-structured-logging.html) for more information about structured logging.

```
fields @timestamp, @message
| filter level in ["ERR", "ERROR", "WARN", "WARNING"]
| sort @timestamp desc
| limit 20
```

## Number of error messages

Counts the number of error messages over 5 minutes interval periods.

__Note:__ this requires using structured logging. See [this section of the Serverless Lens](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/centralized-and-structured-logging.html) for more information about structured logging.

```
filter level in ["ERR", "ERROR"]
| stats count() as numErrors by bin(5m)
```

## Percentage of cold starts

Calculates the percentage of cold start over 5 minutes interval periods.

```
filter @type = "REPORT"
| stats count(@initDuration)/count(@duration)*100 as coldStartPercentage by @log, bin(5m)
```