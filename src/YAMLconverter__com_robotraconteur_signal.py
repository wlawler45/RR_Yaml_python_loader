#!/usr/bin/env python
import yaml
import numpy
import python_enums
import YAMLconverter__com_robotraconteur_identifier
import YAMLconverter__com_robotraconteur_datatype
import YAMLconverter__com_robotraconteur_device
import YAMLconverter__com_robotraconteur_units
import YAMLconverter__com_robotraconteur_device_isoch
def yaml_loader_com_robotraconteur_signal_SignalInfo(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.signal.SignalInfo")
	if(data.get('signal_identifier')!=None):
		output.signal_identifier = YAMLconverter__com_robotraconteur_identifier.yaml_loader_com_robotraconteur_identifier_Identifier(RRN,data['signal_identifier'])
	if(data.get('signal_class')!=None):
		output.signal_class = YAMLconverter__com_robotraconteur_device.yaml_loader_com_robotraconteur_device_DeviceClass(RRN,data['signal_class'])
	if(data.get('units')!=None):
		mylist=[]
		for i in range(len(data['units'])):
			mylist.append(YAMLconverter__com_robotraconteur_units.yaml_loader_com_robotraconteur_units_SIUnit(RRN,data['units'][i]))
		output.units=mylist
	if(data.get('data_type')!=None):
		output.data_type = YAMLconverter__com_robotraconteur_datatype.yaml_loader_com_robotraconteur_datatype_DataType(RRN,data['data_type'])
	if(data.get('signal_type')!=None):
		output.signal_type=python_enums.string_to_enum_SignalType	if(data.get('access_level')!=None):
		output.access_level=python_enums.string_to_enum_SignalAccessLevel	if(data.get('address')!=None):
		output.address=numpy.zeros(len(data['address']),dtype=numpy.uint32)
		for i in range(len(data['address'])):
			output.address[i]=data['address'][i]
	if(data.get('user_description')!=None):
		output.user_description=data['user_description']
	else:
		print("No value found for user_description\n")
	return output

def yaml_loader_com_robotraconteur_signal_SignalGroupInfo(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.signal.SignalGroupInfo")
	if(data.get('signal_group_identifier')!=None):
		output.signal_group_identifier = YAMLconverter__com_robotraconteur_identifier.yaml_loader_com_robotraconteur_identifier_Identifier(RRN,data['signal_group_identifier'])
	if(data.get('description')!=None):
		output.description=data['description']
	else:
		print("No value found for description\n")
	return output

#TODO: Fix the following structures or namedarrays: 
# com.robotraconteur.signal.SignalGroupInfo 

