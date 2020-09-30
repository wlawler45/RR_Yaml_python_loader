#!/usr/bin/env python
import yaml
import numpy
import python_enums
import YAMLconverter__com_robotraconteur_datetime
import YAMLconverter__com_robotraconteur_identifier
import YAMLconverter__com_robotraconteur_geometry
def yaml_loader_com_robotraconteur_sensordata_SensorDataHeader(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.sensordata.SensorDataHeader")
	if(data.get('seqno')!=None):
		output.seqno=data['seqno']
	else:
		print("No value found for seqno\n")
	if(data.get('source_info')!=None):
		output.source_info = yaml_loader_com_robotraconteur_sensordata_SensorDataSourceInfo(RRN,data['source_info'])
	return output

def yaml_loader_com_robotraconteur_sensordata_SensorDataSourceInfo(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.sensordata.SensorDataSourceInfo")
	if(data.get('source')!=None):
		output.source = YAMLconverter__com_robotraconteur_identifier.yaml_loader_com_robotraconteur_identifier_Identifier(RRN,data['source'])
	if(data.get('source_world_pose')!=None):
		output.source_world_pose = YAMLconverter__com_robotraconteur_geometry.yaml_loader_com_robotraconteur_geometry_Pose(RRN,data['source_world_pose'])
	if(data.get('source_config_nonce')!=None):
		output.source_config_nonce=data['source_config_nonce']
	else:
		print("No value found for source_config_nonce\n")
	return output


