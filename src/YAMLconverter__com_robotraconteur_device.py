#!/usr/bin/env python
import yaml
import numpy
import python_enums
import YAMLconverter__com_robotraconteur_identifier
import YAMLconverter__com_robotraconteur_resource
import YAMLconverter__com_robotraconteur_geometry
def yaml_loader_com_robotraconteur_device_DeviceOption(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.device.DeviceOption")
	if(data.get('option_identifier')!=None):
		output.option_identifier = YAMLconverter__com_robotraconteur_identifier.yaml_loader_com_robotraconteur_identifier_Identifier(RRN,data['option_identifier'])
	if(data.get('suboptions')!=None):
		mylist=[]
		for i in range(len(data['suboptions'])):
			mylist.append(yaml_loader_com_robotraconteur_device_DeviceSubOption(RRN,data['suboptions'][i]))
		output.suboptions=mylist
	return output

def yaml_loader_com_robotraconteur_device_DeviceSubOption(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.device.DeviceSubOption")
	if(data.get('suboption_name')!=None):
		output.suboption_name=data['suboption_name']
	else:
		print("No value found for suboption_name\n")
	if(data.get('suboption_level')!=None):
		output.suboption_level=data['suboption_level']
	else:
		print("No value found for suboption_level\n")
	return output

def yaml_loader_com_robotraconteur_device_DeviceCapability(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.device.DeviceCapability")
	if(data.get('capability_identifier')!=None):
		output.capability_identifier = YAMLconverter__com_robotraconteur_identifier.yaml_loader_com_robotraconteur_identifier_Identifier(RRN,data['capability_identifier'])
	if(data.get('subcapabilities')!=None):
		mylist=[]
		for i in range(len(data['subcapabilities'])):
			mylist.append(yaml_loader_com_robotraconteur_device_DeviceSubCapability(RRN,data['subcapabilities'][i]))
		output.subcapabilities=mylist
	return output

def yaml_loader_com_robotraconteur_device_DeviceSubCapability(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.device.DeviceSubCapability")
	if(data.get('subcapability_name')!=None):
		output.subcapability_name=data['subcapability_name']
	else:
		print("No value found for subcapability_name\n")
	if(data.get('subcapability_level')!=None):
		output.subcapability_level=data['subcapability_level']
	else:
		print("No value found for subcapability_level\n")
	return output

def yaml_loader_com_robotraconteur_device_DeviceClass(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.device.DeviceClass")
	if(data.get('class_identifier')!=None):
		output.class_identifier = YAMLconverter__com_robotraconteur_identifier.yaml_loader_com_robotraconteur_identifier_Identifier(RRN,data['class_identifier'])
	if(data.get('subclasses')!=None):
		mylist=[]
		for i in range(len(data['subclasses'])):
			mylist.append(data['subclasses'][i])
		output.subclasses=mylist
	return output

def yaml_loader_com_robotraconteur_device_DeviceInfo(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.device.DeviceInfo")
	if(data.get('device')!=None):
		output.device = YAMLconverter__com_robotraconteur_identifier.yaml_loader_com_robotraconteur_identifier_Identifier(RRN,data['device'])
	if(data.get('parent_device')!=None):
		output.parent_device = YAMLconverter__com_robotraconteur_identifier.yaml_loader_com_robotraconteur_identifier_Identifier(RRN,data['parent_device'])
	if(data.get('manufacturer')!=None):
		output.manufacturer = YAMLconverter__com_robotraconteur_identifier.yaml_loader_com_robotraconteur_identifier_Identifier(RRN,data['manufacturer'])
	if(data.get('model')!=None):
		output.model = YAMLconverter__com_robotraconteur_identifier.yaml_loader_com_robotraconteur_identifier_Identifier(RRN,data['model'])
	if(data.get('options')!=None):
		mylist=[]
		for i in range(len(data['options'])):
			mylist.append(yaml_loader_com_robotraconteur_device_DeviceOption(RRN,data['options'][i]))
		output.options=mylist
	if(data.get('capabilities')!=None):
		mylist=[]
		for i in range(len(data['capabilities'])):
			mylist.append(yaml_loader_com_robotraconteur_device_DeviceCapability(RRN,data['capabilities'][i]))
		output.capabilities=mylist
	if(data.get('serial_number')!=None):
		output.serial_number=data['serial_number']
	else:
		print("No value found for serial_number\n")
	if(data.get('device_classes')!=None):
		mylist=[]
		for i in range(len(data['device_classes'])):
			mylist.append(yaml_loader_com_robotraconteur_device_DeviceClass(RRN,data['device_classes'][i]))
		output.device_classes=mylist
	if(data.get('user_description')!=None):
		output.user_description=data['user_description']
	else:
		print("No value found for user_description\n")
	if(data.get('description_resource')!=None):
		output.description_resource = YAMLconverter__com_robotraconteur_resource.yaml_loader_com_robotraconteur_resource_ResourceIdentifier(RRN,data['description_resource'])
	if(data.get('implemented_types')!=None):
		mylist=[]
		for i in range(len(data['implemented_types'])):
			mylist.append(data['implemented_types'][i])
		output.implemented_types=mylist
	if(data.get('device_origin_pose')!=None):
		output.device_origin_pose = YAMLconverter__com_robotraconteur_geometry.yaml_loader_com_robotraconteur_geometry_NamedPose(RRN,data['device_origin_pose'])
	return output


