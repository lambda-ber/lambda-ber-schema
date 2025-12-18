

# Slot: database_name 


_Name of the external database_





URI: [lambdaber:database_name](https://w3id.org/lambda-ber-schema/database_name)
Alias: database_name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DatabaseCrossReference](DatabaseCrossReference.md) | Cross-references to external databases |  no  |






## Properties

* Range: [DatabaseNameEnum](DatabaseNameEnum.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/lambda-ber-schema/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambdaber:database_name |
| native | lambdaber:database_name |




## LinkML Source

<details>
```yaml
name: database_name
description: Name of the external database
from_schema: https://w3id.org/lambda-ber-schema/
rank: 1000
alias: database_name
owner: DatabaseCrossReference
domain_of:
- DatabaseCrossReference
range: DatabaseNameEnum
required: true

```
</details>