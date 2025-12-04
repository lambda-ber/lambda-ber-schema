
# Class: DatabaseCrossReference

Cross-references to external databases

URI: [lambdaber:DatabaseCrossReference](https://w3id.org/lambda-ber-schema/DatabaseCrossReference)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[AggregatedProteinView]++-%20cross_references%200..*>[DatabaseCrossReference&#124;database_name:DatabaseNameEnum;database_id:string;database_url:uri%20%3F;last_updated:string%20%3F;description(i):string%20%3F],[Sample]++-%20database_cross_references%200..*>[DatabaseCrossReference],[AttributeGroup]^-[DatabaseCrossReference],[Sample],[AttributeGroup],[AggregatedProteinView])](https://yuml.me/diagram/nofunky;dir:TB/class/[AggregatedProteinView]++-%20cross_references%200..*>[DatabaseCrossReference&#124;database_name:DatabaseNameEnum;database_id:string;database_url:uri%20%3F;last_updated:string%20%3F;description(i):string%20%3F],[Sample]++-%20database_cross_references%200..*>[DatabaseCrossReference],[AttributeGroup]^-[DatabaseCrossReference],[Sample],[AttributeGroup],[AggregatedProteinView])

## Parents

 *  is_a: [AttributeGroup](AttributeGroup.md) - A grouping of related data attributes that form a logical unit

## Referenced by Class

 *  **None** *[➞cross_references](aggregatedProteinView__cross_references.md)*  <sub>0..\*</sub>  **[DatabaseCrossReference](DatabaseCrossReference.md)**
 *  **None** *[➞database_cross_references](sample__database_cross_references.md)*  <sub>0..\*</sub>  **[DatabaseCrossReference](DatabaseCrossReference.md)**

## Attributes


### Own

 * [➞database_name](databaseCrossReference__database_name.md)  <sub>1..1</sub>
     * Description: Name of the external database
     * Range: [DatabaseNameEnum](DatabaseNameEnum.md)
 * [➞database_id](databaseCrossReference__database_id.md)  <sub>1..1</sub>
     * Description: Identifier in the external database
     * Range: [String](types/String.md)
 * [➞database_url](databaseCrossReference__database_url.md)  <sub>0..1</sub>
     * Description: URL to the database entry
     * Range: [Uri](types/Uri.md)
 * [➞last_updated](databaseCrossReference__last_updated.md)  <sub>0..1</sub>
     * Description: Date of last update
     * Range: [String](types/String.md)

### Inherited from AttributeGroup:

 * [➞description](attributeGroup__description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
