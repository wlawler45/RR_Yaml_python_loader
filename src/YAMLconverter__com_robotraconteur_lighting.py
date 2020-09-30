#!/usr/bin/env python
import yaml
import numpy
import python_enums
import YAMLconverter__com_robotraconteur_color
import YAMLconverter__com_robotraconteur_device
def yaml_loader_com_robotraconteur_lighting_LightInfo(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.lighting.LightInfo")
	if(data.get('device_info')!=None):
		output.device_info = YAMLconverter__com_robotraconteur_device.yaml_loader_com_robotraconteur_device_DeviceInfo(RRN,data['device_info'])
	if(data.get('max_lumens')!=None):
		output.max_lumens=data['max_lumens']
	else:
		print("No value found for max_lumens\n")
	return output


