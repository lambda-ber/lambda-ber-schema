
# Class: StudyExperimentAssociation

M:N link between Study and ExperimentRun

URI: [lambda:StudyExperimentAssociation](http://w3id.org/lambda/StudyExperimentAssociation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ExperimentRun]<experiment_id%201..1-%20[StudyExperimentAssociation],[Study]<study_id%201..1-%20[StudyExperimentAssociation],[Dataset]++-%20study_experiment_associations%200..*>[StudyExperimentAssociation],[Study],[ExperimentRun],[Dataset])](https://yuml.me/diagram/nofunky;dir:TB/class/[ExperimentRun]<experiment_id%201..1-%20[StudyExperimentAssociation],[Study]<study_id%201..1-%20[StudyExperimentAssociation],[Dataset]++-%20study_experiment_associations%200..*>[StudyExperimentAssociation],[Study],[ExperimentRun],[Dataset])

## Referenced by Class

 *  **None** *[➞study_experiment_associations](dataset__study_experiment_associations.md)*  <sub>0..\*</sub>  **[StudyExperimentAssociation](StudyExperimentAssociation.md)**

## Attributes


### Own

 * [➞study_id](studyExperimentAssociation__study_id.md)  <sub>1..1</sub>
     * Description: Reference to the study
     * Range: [Study](Study.md)
 * [➞experiment_id](studyExperimentAssociation__experiment_id.md)  <sub>1..1</sub>
     * Description: Reference to the experiment run
     * Range: [ExperimentRun](ExperimentRun.md)
