#!/usr/bin/env python
import yaml
import numpy
import python_enums
import YAMLconverter__com_robotraconteur_sensordata
import YAMLconverter__com_robotraconteur_identifier
import YAMLconverter__com_robotraconteur_resource
def yaml_loader_com_robotraconteur_octree_OcTreeInfo(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.octree.OcTreeInfo")
	if(data.get('data_header')!=None):
		output.data_header = YAMLconverter__com_robotraconteur_sensordata.yaml_loader_com_robotraconteur_sensordata_SensorDataHeader(RRN,data['data_header'])
	if(data.get('encoding')!=None):
		output.encoding=python_enums.string_to_enum_OcTreeEncoding	if(data.get('id')!=None):
		output.id=data['id']
	else:
		print("No value found for id\n")
	if(data.get('resolution')!=None):
		output.resolution=data['resolution']
	else:
		print("No value found for resolution\n")
	return output

def yaml_loader_com_robotraconteur_octree_OcTree(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.octree.OcTree")
	if(data.get('octree_info')!=None):
		output.octree_info = yaml_loader_com_robotraconteur_octree_OcTreeInfo(RRN,data['octree_info'])
	if(data.get('data')!=None):
		output.data=numpy.zeros(len(data['data']),dtype=numpy.uint8)
		for i in range(len(data['data'])):
			output.data[i]=data['data'][i]
	return output

def yaml_loader_com_robotraconteur_octree_OcTreePart(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.octree.OcTreePart")
	if(data.get('octree_info')!=None):
		output.octree_info = yaml_loader_com_robotraconteur_octree_OcTreeInfo(RRN,data['octree_info'])
	if(data.get('data_offset')!=None):
		output.data_offset=data['data_offset']
	else:
		print("No value found for data_offset\n")
	if(data.get('data_total_len')!=None):
		output.data_total_len=data['data_total_len']
	else:
		print("No value found for data_total_len\n")
	if(data.get('data')!=None):
		output.data=numpy.zeros(len(data['data']),dtype=numpy.uint8)
		for i in range(len(data['data'])):
			output.data[i]=data['data'][i]
	return output

def yaml_loader_com_robotraconteur_octree_OcTreeResource(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.octree.OcTreeResource")
	if(data.get('octree_resource')!=None):
		output.octree_resource = YAMLconverter__com_robotraconteur_resource.yaml_loader_com_robotraconteur_resource_ResourceIdentifier(RRN,data['octree_resource'])
	return output


