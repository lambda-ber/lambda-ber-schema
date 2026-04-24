# Enum: ProcessingStatusEnum 




_Processing status_



URI: [lambda:ProcessingStatusEnum](http://w3id.org/lambda/ProcessingStatusEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| collected | None | Data has been collected but not yet processed |
| raw | None | Raw data |
| preprocessing | None | Being preprocessed |
| processing | None | Being processed |
| completed | None | Processing completed |
| failed | None | Processing failed |




## Slots

| Name | Description |
| ---  | --- |
| [processing_status](processing_status.md) | Current processing status |





## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/






## LinkML Source

<details>
```yaml
name: ProcessingStatusEnum
description: Processing status
from_schema: http://w3id.org/lambda/
rank: 1000
permissible_values:
  collected:
    text: collected
    description: Data has been collected but not yet processed
  raw:
    text: raw
    description: Raw data
  preprocessing:
    text: preprocessing
    description: Being preprocessed
  processing:
    text: processing
    description: Being processed
  completed:
    text: completed
    description: Processing completed
  failed:
    text: failed
    description: Processing failed

```
</details>