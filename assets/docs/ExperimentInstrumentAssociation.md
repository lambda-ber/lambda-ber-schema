
# Class: ExperimentInstrumentAssociation

M:N link between ExperimentRun and Instrument

URI: [lambda:ExperimentInstrumentAssociation](http://w3id.org/lambda/ExperimentInstrumentAssociation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Instrument],[ExperimentRun],[Instrument]<instrument_id%201..1-%20[ExperimentInstrumentAssociation&#124;role:InstrumentRoleEnum%20%3F],[ExperimentRun]<experiment_id%201..1-%20[ExperimentInstrumentAssociation],[Dataset]++-%20experiment_instrument_associations%200..*>[ExperimentInstrumentAssociation],[Dataset])](https://yuml.me/diagram/nofunky;dir:TB/class/[Instrument],[ExperimentRun],[Instrument]<instrument_id%201..1-%20[ExperimentInstrumentAssociation&#124;role:InstrumentRoleEnum%20%3F],[ExperimentRun]<experiment_id%201..1-%20[ExperimentInstrumentAssociation],[Dataset]++-%20experiment_instrument_associations%200..*>[ExperimentInstrumentAssociation],[Dataset])

## Referenced by Class

 *  **None** *[➞experiment_instrument_associations](dataset__experiment_instrument_associations.md)*  <sub>0..\*</sub>  **[ExperimentInstrumentAssociation](ExperimentInstrumentAssociation.md)**

## Attributes


### Own

 * [➞experiment_id](experimentInstrumentAssociation__experiment_id.md)  <sub>1..1</sub>
     * Description: Reference to the experiment run
     * Range: [ExperimentRun](ExperimentRun.md)
 * [➞instrument_id](experimentInstrumentAssociation__instrument_id.md)  <sub>1..1</sub>
     * Description: Reference to the instrument
     * Range: [Instrument](Instrument.md)
 * [➞role](experimentInstrumentAssociation__role.md)  <sub>0..1</sub>
     * Description: Role of instrument in experiment
     * Range: [InstrumentRoleEnum](InstrumentRoleEnum.md)
