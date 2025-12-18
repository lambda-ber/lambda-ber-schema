# Enum: ProcessingStatusEnum 




_Processing status_



URI: [lambdaber:ProcessingStatusEnum](https://w3id.org/lambda-ber-schema/ProcessingStatusEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
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


* from schema: https://w3id.org/lambda-ber-schema/






## LinkML Source

<details>
```yaml
name: ProcessingStatusEnum
description: Processing status
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
permissible_values:
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