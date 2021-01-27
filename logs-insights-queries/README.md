Amazon CloudWatch Logs Insights queries
=======================================

## Billed duration in GB-s

Calculated the total billed duration in GB-s over 5 minutes interval periods.

```
filter @type = "REPORT"
| stats sum(@billedDuration)/1000 * avg(@memorySize)/1024000000 as billedGBs by @log, bin(5m)
```

## Percentage of cold starts

Calculates the percentage of cold start over 5 minutes interval periods.

```
filter @type = "REPORT"
| stats count(@initDuration)/count(@duration)*100 as coldStartPercentage by @log, bin(5m)
```