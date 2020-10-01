#!/usr/bin/env python
import yaml
import numpy
import python_enums
import YAMLconverter__com_robotraconteur_sensor
import YAMLconverter__com_robotraconteur_geometry
import YAMLconverter__com_robotraconteur_device
def yaml_loader_com_robotraconteur_imu_ImuState(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.imu.ImuState")
	if(data.get('angular_velocity')!=None):
		output.angular_velocity = YAMLconverter__com_robotraconteur_geometry.yaml_loader_com_robotraconteur_geometry_Vector3(RRN,data['angular_velocity'])
	if(data.get('linear_acceleration')!=None):
		output.linear_acceleration = YAMLconverter__com_robotraconteur_geometry.yaml_loader_com_robotraconteur_geometry_Vector3(RRN,data['linear_acceleration'])
	if(data.get('orientation')!=None):
		output.orientation = YAMLconverter__com_robotraconteur_geometry.yaml_loader_com_robotraconteur_geometry_Quaternion(RRN,data['orientation'])
	return output


