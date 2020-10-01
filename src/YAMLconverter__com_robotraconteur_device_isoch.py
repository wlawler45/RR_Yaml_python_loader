#!/usr/bin/env python
import yaml
import numpy
import python_enums
import YAMLconverter__com_robotraconteur_datetime
def yaml_loader_com_robotraconteur_device_isoch_IsochInfo(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.device.isoch.IsochInfo")
	if(data.get('update_rate')!=None):
		output.update_rate=data['update_rate']
	else:
		print("No value found for update_rate\n")
	if(data.get('max_downsample')!=None):
		output.max_downsample=data['max_downsample']
	else:
		print("No value found for max_downsample\n")
	return output


