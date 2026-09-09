

# Slot: full_name 


_Full formal name of the person, as they write it in publications_





URI: [lambda:full_name](http://w3id.org/lambda/full_name)
Alias: full_name

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | A person involved in producing, processing or publishing data - a principal i... |  no  |






## Properties

* Range: [String](String.md)




## Comments

* Overlaps the inherited `title`, deliberately but not redundantly. `title` is the display label every NamedThing carries and is what a listing shows ("Clyde Smith"); `full_name` is the formal name a citation needs ("Clyde A. Smith"). They are equal often enough that a consumer reading only one is usually fine, so record `title` whenever `full_name` is known - a Person with a formal name and no display label is awkward for every UI that treats NamedThing uniformly.
* Where the two would be identical, carrying only `title` is correct and `full_name` adds nothing.

## Identifier and Mapping Information






### Schema Source


* from schema: http://w3id.org/lambda/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | lambda:full_name |
| native | lambda:full_name |
| close | lambda:title |




## LinkML Source

<details>
```yaml
name: full_name
description: Full formal name of the person, as they write it in publications
comments:
- Overlaps the inherited `title`, deliberately but not redundantly. `title` is the
  display label every NamedThing carries and is what a listing shows ("Clyde Smith");
  `full_name` is the formal name a citation needs ("Clyde A. Smith"). They are equal
  often enough that a consumer reading only one is usually fine, so record `title`
  whenever `full_name` is known - a Person with a formal name and no display label
  is awkward for every UI that treats NamedThing uniformly.
- Where the two would be identical, carrying only `title` is correct and `full_name`
  adds nothing.
from_schema: http://w3id.org/lambda/
close_mappings:
- lambda:title
rank: 1000
alias: full_name
owner: Person
domain_of:
- Person
range: string

```
</details>