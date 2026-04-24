

# Slot: database_name 


_Name of the external database_





URI: [lambda:database_name](http://w3id.org/lambda/database_name)
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


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:database_name |
| native | lambda:database_name |




## LinkML Source

<details>
```yaml
name: database_name
description: Name of the external database
from_schema: http://w3id.org/lambda/
rank: 1000
alias: database_name
owner: DatabaseCrossReference
domain_of:
- DatabaseCrossReference
range: DatabaseNameEnum
required: true

```
</details>