#!/usr/bin/env python
import yaml
import numpy
import python_enums
import YAMLconverter__com_robotraconteur_device
import YAMLconverter__com_robotraconteur_geometry
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
	return output


