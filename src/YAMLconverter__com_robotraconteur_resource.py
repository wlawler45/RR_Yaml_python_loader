#!/usr/bin/env python
import yaml
import numpy
import python_enums
import YAMLconverter__com_robotraconteur_uuid
import YAMLconverter__com_robotraconteur_datetime
import YAMLconverter__com_robotraconteur_identifier
def yaml_loader_com_robotraconteur_resource_ResourceIdentifier(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.resource.ResourceIdentifier")
	if(data.get('bucket')!=None):
		output.bucket = YAMLconverter__com_robotraconteur_identifier.yaml_loader_com_robotraconteur_identifier_Identifier(RRN,data['bucket'])
	if(data.get('key')!=None):
		output.key=data['key']
	else:
		print("No value found for key\n")
	return output

def yaml_loader_com_robotraconteur_resource_BucketInfo(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.resource.BucketInfo")
	if(data.get('identifier')!=None):
		output.identifier = YAMLconverter__com_robotraconteur_identifier.yaml_loader_com_robotraconteur_identifier_Identifier(RRN,data['identifier'])
	if(data.get('keys')!=None):
		mylist=[]
		for i in range(len(data['keys'])):
			mylist.append(data['keys'][i])
		output.keys=mylist
	if(data.get('description')!=None):
		output.description=data['description']
	else:
		print("No value found for description\n")
	return output

def yaml_loader_com_robotraconteur_resource_ResourceInfo(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.resource.ResourceInfo")
	if(data.get('identifier')!=None):
		output.identifier = yaml_loader_com_robotraconteur_resource_ResourceIdentifier(RRN,data['identifier'])
	if(data.get('key')!=None):
		output.key=data['key']
	else:
		print("No value found for key\n")
	if(data.get('total_size')!=None):
		output.total_size=data['total_size']
	else:
		print("No value found for total_size\n")
	if(data.get('description')!=None):
		output.description=data['description']
	else:
		print("No value found for description\n")
	return output

def yaml_loader_com_robotraconteur_resource_Resource(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.resource.Resource")
	if(data.get('info')!=None):
		output.info = yaml_loader_com_robotraconteur_resource_ResourceInfo(RRN,data['info'])
	if(data.get('data')!=None):
		output.data=numpy.zeros(len(data['data']),dtype=numpy.uint8)
		for i in range(len(data['data'])):
			output.data[i]=data['data'][i]
	return output

def yaml_loader_com_robotraconteur_resource_ResourcePart(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.resource.ResourcePart")
	if(data.get('info')!=None):
		output.info = yaml_loader_com_robotraconteur_resource_ResourceInfo(RRN,data['info'])
	if(data.get('data_offset')!=None):
		output.data_offset=data['data_offset']
	else:
		print("No value found for data_offset\n")
	if(data.get('data')!=None):
		output.data=numpy.zeros(len(data['data']),dtype=numpy.uint8)
		for i in range(len(data['data'])):
			output.data[i]=data['data'][i]
	return output


