
# Class: Study

A logical grouping of related experiments investigating a research question. In the relational model, Study is lightweight - all relationships are via association tables.

URI: [lambda:Study](http://w3id.org/lambda/Study)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Dataset]++-%20studies%200..*>[Study&#124;keywords:string%20*;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[StudyExperimentAssociation]-%20study_id%201..1>[Study],[StudySampleAssociation]-%20study_id%201..1>[Study],[StudyWorkflowAssociation]-%20study_id%201..1>[Study],[NamedThing]^-[Study],[StudyWorkflowAssociation],[StudySampleAssociation],[StudyExperimentAssociation],[NamedThing],[Dataset])](https://yuml.me/diagram/nofunky;dir:TB/class/[Dataset]++-%20studies%200..*>[Study&#124;keywords:string%20*;id(i):uriorcurie;title(i):string%20%3F;description(i):string%20%3F],[StudyExperimentAssociation]-%20study_id%201..1>[Study],[StudySampleAssociation]-%20study_id%201..1>[Study],[StudyWorkflowAssociation]-%20study_id%201..1>[Study],[NamedThing]^-[Study],[StudyWorkflowAssociation],[StudySampleAssociation],[StudyExperimentAssociation],[NamedThing],[Dataset])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A named thing

## Referenced by Class

 *  **None** *[➞studies](dataset__studies.md)*  <sub>0..\*</sub>  **[Study](Study.md)**
 *  **None** *[➞study_id](studyExperimentAssociation__study_id.md)*  <sub>1..1</sub>  **[Study](Study.md)**
 *  **None** *[➞study_id](studySampleAssociation__study_id.md)*  <sub>1..1</sub>  **[Study](Study.md)**
 *  **None** *[➞study_id](studyWorkflowAssociation__study_id.md)*  <sub>1..1</sub>  **[Study](Study.md)**

## Attributes


### Own

 * [➞keywords](study__keywords.md)  <sub>0..\*</sub>
     * Description: Keywords or tags describing the study for search and categorization
     * Range: [String](types/String.md)

### Inherited from NamedThing:

 * [➞id](namedThing__id.md)  <sub>1..1</sub>
     * Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞title](namedThing__title.md)  <sub>0..1</sub>
     * Description: A human-readable name or title for this entity
     * Range: [String](types/String.md)
 * [➞description](namedThing__description.md)  <sub>0..1</sub>
     * Description: A detailed textual description of this entity
     * Range: [String](types/String.md)
