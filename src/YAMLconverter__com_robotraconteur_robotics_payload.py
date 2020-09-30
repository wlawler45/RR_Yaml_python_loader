#!/usr/bin/env python
import yaml
import numpy
import python_enums
import YAMLconverter__com_robotraconteur_device
import YAMLconverter__com_robotraconteur_geometry
def yaml_loader_com_robotraconteur_robotics_payload_PayloadInfo(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.robotics.payload.PayloadInfo")
	if(data.get('device_info')!=None):
		output.device_info = YAMLconverter__com_robotraconteur_device.yaml_loader_com_robotraconteur_device_DeviceInfo(RRN,data['device_info'])
	if(data.get('inertia')!=None):
		output.inertia = YAMLconverter__com_robotraconteur_geometry.yaml_loader_com_robotraconteur_geometry_SpatialInertia(RRN,data['inertia'])
	return output


