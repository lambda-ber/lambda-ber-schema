
# Class: StudySampleAssociation

M:N link between Study and Sample with role metadata

URI: [lambda:StudySampleAssociation](http://w3id.org/lambda/StudySampleAssociation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Sample]<sample_id%201..1-%20[StudySampleAssociation&#124;role:SampleRoleEnum%20%3F;date_added:date%20%3F],[Study]<study_id%201..1-%20[StudySampleAssociation],[Dataset]++-%20study_sample_associations%200..*>[StudySampleAssociation],[Study],[Sample],[Dataset])](https://yuml.me/diagram/nofunky;dir:TB/class/[Sample]<sample_id%201..1-%20[StudySampleAssociation&#124;role:SampleRoleEnum%20%3F;date_added:date%20%3F],[Study]<study_id%201..1-%20[StudySampleAssociation],[Dataset]++-%20study_sample_associations%200..*>[StudySampleAssociation],[Study],[Sample],[Dataset])

## Referenced by Class

 *  **None** *[➞study_sample_associations](dataset__study_sample_associations.md)*  <sub>0..\*</sub>  **[StudySampleAssociation](StudySampleAssociation.md)**

## Attributes


### Own

 * [➞study_id](studySampleAssociation__study_id.md)  <sub>1..1</sub>
     * Description: Reference to the study
     * Range: [Study](Study.md)
 * [➞sample_id](studySampleAssociation__sample_id.md)  <sub>1..1</sub>
     * Description: Reference to the sample
     * Range: [Sample](Sample.md)
 * [➞role](studySampleAssociation__role.md)  <sub>0..1</sub>
     * Description: Role of sample in study (e.g., target, control, reference)
     * Range: [SampleRoleEnum](SampleRoleEnum.md)
 * [➞date_added](studySampleAssociation__date_added.md)  <sub>0..1</sub>
     * Description: Date when sample was added to study
     * Range: [Date](types/Date.md)
