#!/usr/bin/env python
import yaml
import numpy
import python_enums
import YAMLconverter__com_robotraconteur_device
import YAMLconverter__com_robotraconteur_param
import YAMLconverter__com_robotraconteur_units
import YAMLconverter__com_robotraconteur_datatype
def yaml_loader_com_robotraconteur_actuator_ActuatorInfo(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.actuator.ActuatorInfo")
	if(data.get('device_info')!=None):
		output.device_info = YAMLconverter__com_robotraconteur_device.yaml_loader_com_robotraconteur_device_DeviceInfo(RRN,data['device_info'])
	if(data.get('actuator_type')!=None):
		output.actuator_type=python_enums.string_to_enum_ActuatorTypeCode	if(data.get('command_units')!=None):
		mylist=[]
		for i in range(len(data['command_units'])):
			mylist.append(YAMLconverter__com_robotraconteur_units.yaml_loader_com_robotraconteur_units_SIUnit(RRN,data['command_units'][i]))
		output.command_units=mylist
	if(data.get('command_data_type')!=None):
		output.command_data_type = YAMLconverter__com_robotraconteur_datatype.yaml_loader_com_robotraconteur_datatype_DataType(RRN,data['command_data_type'])
	if(data.get('command_resolution')!=None):
		output.command_resolution=numpy.zeros(len(data['command_resolution']),dtype=numpy.double)
		for i in range(len(data['command_resolution'])):
			output.command_resolution[i]=data['command_resolution'][i]
	if(data.get('analog_output')!=None):
		output.analog_output=data['analog_output']
	else:
		print("No value found for analog_output\n")
	return output


