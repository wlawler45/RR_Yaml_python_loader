#!/usr/bin/env python
import yaml
import numpy
import python_enums
import YAMLconverter__com_robotraconteur_identifier
import YAMLconverter__com_robotraconteur_datatype
import YAMLconverter__com_robotraconteur_device
def yaml_loader_com_robotraconteur_param_ParameterInfo(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.param.ParameterInfo")
	if(data.get('parameter_identifier')!=None):
		output.parameter_identifier = YAMLconverter__com_robotraconteur_identifier.yaml_loader_com_robotraconteur_identifier_Identifier(RRN,data['parameter_identifier'])
	if(data.get('parameter_class')!=None):
		output.parameter_class = YAMLconverter__com_robotraconteur_device.yaml_loader_com_robotraconteur_device_DeviceClass(RRN,data['parameter_class'])
	if(data.get('data_type')!=None):
		output.data_type = YAMLconverter__com_robotraconteur_datatype.yaml_loader_com_robotraconteur_datatype_DataType(RRN,data['data_type'])
	if(data.get('user_description')!=None):
		output.user_description=data['user_description']
	else:
		print("No value found for user_description\n")
	return output

#TODO: Fix the following structures or namedarrays: 
# com.robotraconteur.param.ParameterInfo 

