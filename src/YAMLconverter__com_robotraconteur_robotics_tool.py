#!/usr/bin/env python
import yaml
import numpy
import python_enums
import YAMLconverter__com_robotraconteur_device
import YAMLconverter__com_robotraconteur_geometry
import YAMLconverter__com_robotraconteur_sensor
import YAMLconverter__com_robotraconteur_robotics_joints
import YAMLconverter__com_robotraconteur_units
def yaml_loader_com_robotraconteur_robotics_tool_ToolInfo(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.robotics.tool.ToolInfo")
	if(data.get('device_info')!=None):
		output.device_info = YAMLconverter__com_robotraconteur_device.yaml_loader_com_robotraconteur_device_DeviceInfo(RRN,data['device_info'])
	if(data.get('tcp')!=None):
		output.tcp = YAMLconverter__com_robotraconteur_geometry.yaml_loader_com_robotraconteur_geometry_Transform(RRN,data['tcp'])
	if(data.get('inertia')!=None):
		output.inertia = YAMLconverter__com_robotraconteur_geometry.yaml_loader_com_robotraconteur_geometry_SpatialInertia(RRN,data['inertia'])
	if(data.get('actuation_time')!=None):
		output.actuation_time=data['actuation_time']
	else:
		print("No value found for actuation_time\n")
	if(data.get('command_min')!=None):
		output.command_min=data['command_min']
	else:
		print("No value found for command_min\n")
	if(data.get('command_max')!=None):
		output.command_max=data['command_max']
	else:
		print("No value found for command_max\n")
	if(data.get('sensor_min')!=None):
		output.sensor_min=numpy.zeros(len(data['sensor_min']),dtype=numpy.double)
		for i in range(len(data['sensor_min'])):
			output.sensor_min[i]=data['sensor_min'][i]
	if(data.get('sensor_max')!=None):
		output.sensor_max=numpy.zeros(len(data['sensor_max']),dtype=numpy.double)
		for i in range(len(data['sensor_max'])):
			output.sensor_max[i]=data['sensor_max'][i]
	if(data.get('sensor_units')!=None):
		mylist=[]
		for i in range(len(data['sensor_units'])):
			mylist.append(YAMLconverter__com_robotraconteur_units.yaml_loader_com_robotraconteur_units_SIUnit(RRN,data['sensor_units'][i]))
		output.sensor_units=mylist
	return output

def yaml_loader_com_robotraconteur_robotics_tool_ToolState(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.robotics.tool.ToolState")
	if(data.get('tool_status')!=None):
		output.tool_status=python_enums.string_to_enum_ToolStatus	if(data.get('position')!=None):
		output.position=data['position']
	else:
		print("No value found for position\n")
	if(data.get('command')!=None):
		output.command=data['command']
	else:
		print("No value found for command\n")
	if(data.get('sensor')!=None):
		output.sensor=numpy.zeros(len(data['sensor']),dtype=numpy.double)
		for i in range(len(data['sensor'])):
			output.sensor[i]=data['sensor'][i]
	return output


