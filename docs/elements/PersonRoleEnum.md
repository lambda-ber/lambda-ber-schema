# Enum: PersonRoleEnum 




_Capacity in which a person is attached to a study, experiment run or workflow run. One vocabulary rather than one per association, because these roles belong to the person's relationship to the work and travel across all three - a principal investigator who also collects the data holds two roles, not two differently-named ones._



URI: [lambda:PersonRoleEnum](http://w3id.org/lambda/PersonRoleEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| principal_investigator | None | Scientifically responsible for the work; the PI on the proposal |
| co_investigator | None | Shares scientific responsibility with the principal investigator |
| author | None | Credited author of the dataset or its associated publication |
| operator | None | Collected the data at the instrument |
| local_contact | None | Facility staff member supporting the collection session |
| analyst | None | Performed the computational processing or analysis |
| reviewer | None | Reviewed or validated the data or its processing |
| data_curator | None | Prepared, described or deposited the data |
| submitter | None | Submitted the data to a facility, archive or repository |
| contact | None | Point of contact for enquiries about the data |








## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/






## LinkML Source

<details>
```yaml
name: PersonRoleEnum
description: Capacity in which a person is attached to a study, experiment run or
  workflow run. One vocabulary rather than one per association, because these roles
  belong to the person's relationship to the work and travel across all three - a
  principal investigator who also collects the data holds two roles, not two differently-named
  ones.
from_schema: http://w3id.org/lambda/
rank: 1000
permissible_values:
  principal_investigator:
    text: principal_investigator
    description: Scientifically responsible for the work; the PI on the proposal
  co_investigator:
    text: co_investigator
    description: Shares scientific responsibility with the principal investigator
  author:
    text: author
    description: Credited author of the dataset or its associated publication
  operator:
    text: operator
    description: Collected the data at the instrument
  local_contact:
    text: local_contact
    description: Facility staff member supporting the collection session
  analyst:
    text: analyst
    description: Performed the computational processing or analysis
  reviewer:
    text: reviewer
    description: Reviewed or validated the data or its processing
  data_curator:
    text: data_curator
    description: Prepared, described or deposited the data
  submitter:
    text: submitter
    description: Submitted the data to a facility, archive or repository
  contact:
    text: contact
    description: Point of contact for enquiries about the data

```
</details>