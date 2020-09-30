#!/usr/bin/env python
import yaml
import numpy
import python_enums
import YAMLconverter__com_robotraconteur_uuid
def yaml_loader_com_robotraconteur_identifier_Identifier(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.identifier.Identifier")
	if(data.get('name')!=None):
		output.name=data['name']
	else:
		print("No value found for name\n")
	if(data.get('uuid')!=None):
		output.uuid = YAMLconverter__com_robotraconteur_uuid.yaml_loader_com_robotraconteur_uuid_UUID(RRN,data['uuid'])
	return output


