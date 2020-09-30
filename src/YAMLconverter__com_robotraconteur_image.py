#!/usr/bin/env python
import yaml
import numpy
import python_enums
import YAMLconverter__com_robotraconteur_sensordata
import YAMLconverter__com_robotraconteur_identifier
import YAMLconverter__com_robotraconteur_resource
def yaml_loader_com_robotraconteur_image_PixelRGB(RRN,data):
	output_type=RRN.GetNamedArrayDType("com.robotraconteur.image.PixelRGB")
	output=numpy.zeros((1,),dtype=output_type)
	output[0]['r']=data['r']
	output[0]['g']=data['g']
	output[0]['b']=data['b']
	return output

def yaml_loader_com_robotraconteur_image_PixelRGBA(RRN,data):
	output_type=RRN.GetNamedArrayDType("com.robotraconteur.image.PixelRGBA")
	output=numpy.zeros((1,),dtype=output_type)
	output[0]['r']=data['r']
	output[0]['g']=data['g']
	output[0]['b']=data['b']
	output[0]['a']=data['a']
	return output

def yaml_loader_com_robotraconteur_image_PixelRGBFloatPacked(RRN,data):
	output_type=RRN.GetNamedArrayDType("com.robotraconteur.image.PixelRGBFloatPacked")
	output=numpy.zeros((1,),dtype=output_type)
	output[0]['rgb']=data['rgb']
	return output

def yaml_loader_com_robotraconteur_image_PixelRGBFloatPackedf(RRN,data):
	output_type=RRN.GetNamedArrayDType("com.robotraconteur.image.PixelRGBFloatPackedf")
	output=numpy.zeros((1,),dtype=output_type)
	output[0]['rgb']=data['rgb']
	return output

def yaml_loader_com_robotraconteur_image_ImageInfo(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.image.ImageInfo")
	if(data.get('data_header')!=None):
		output.data_header = YAMLconverter__com_robotraconteur_sensordata.yaml_loader_com_robotraconteur_sensordata_SensorDataHeader(RRN,data['data_header'])
	if(data.get('height')!=None):
		output.height=data['height']
	else:
		print("No value found for height\n")
	if(data.get('width')!=None):
		output.width=data['width']
	else:
		print("No value found for width\n")
	if(data.get('step')!=None):
		output.step=data['step']
	else:
		print("No value found for step\n")
	if(data.get('encoding')!=None):
		output.encoding=python_enums.string_to_enum_ImageEncoding	return output

def yaml_loader_com_robotraconteur_image_FreeformImageInfo(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.image.FreeformImageInfo")
	if(data.get('image_info')!=None):
		output.image_info = yaml_loader_com_robotraconteur_image_ImageInfo(RRN,data['image_info'])
	if(data.get('encoding')!=None):
		output.encoding=data['encoding']
	else:
		print("No value found for encoding\n")
	return output

def yaml_loader_com_robotraconteur_image_Image(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.image.Image")
	if(data.get('image_info')!=None):
		output.image_info = yaml_loader_com_robotraconteur_image_ImageInfo(RRN,data['image_info'])
	if(data.get('data')!=None):
		output.data=numpy.zeros(len(data['data']),dtype=numpy.uint8)
		for i in range(len(data['data'])):
			output.data[i]=data['data'][i]
	return output

def yaml_loader_com_robotraconteur_image_CompressedImage(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.image.CompressedImage")
	if(data.get('image_info')!=None):
		output.image_info = yaml_loader_com_robotraconteur_image_ImageInfo(RRN,data['image_info'])
	if(data.get('data')!=None):
		output.data=numpy.zeros(len(data['data']),dtype=numpy.uint8)
		for i in range(len(data['data'])):
			output.data[i]=data['data'][i]
	return output

def yaml_loader_com_robotraconteur_image_FreeformImage(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.image.FreeformImage")
	if(data.get('image_info')!=None):
		output.image_info = yaml_loader_com_robotraconteur_image_FreeformImageInfo(RRN,data['image_info'])
	return output

def yaml_loader_com_robotraconteur_image_ImagePart(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.image.ImagePart")
	if(data.get('image_info')!=None):
		output.image_info = yaml_loader_com_robotraconteur_image_ImageInfo(RRN,data['image_info'])
	if(data.get('data_offset')!=None):
		output.data_offset=data['data_offset']
	else:
		print("No value found for data_offset\n")
	if(data.get('data_total_len')!=None):
		output.data_total_len=data['data_total_len']
	else:
		print("No value found for data_total_len\n")
	if(data.get('data_part')!=None):
		output.data_part=numpy.zeros(len(data['data_part']),dtype=numpy.uint8)
		for i in range(len(data['data_part'])):
			output.data_part[i]=data['data_part'][i]
	return output

def yaml_loader_com_robotraconteur_image_CompressedImagePart(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.image.CompressedImagePart")
	if(data.get('image_info')!=None):
		output.image_info = yaml_loader_com_robotraconteur_image_ImageInfo(RRN,data['image_info'])
	if(data.get('data_offset')!=None):
		output.data_offset=data['data_offset']
	else:
		print("No value found for data_offset\n")
	if(data.get('data_total_len')!=None):
		output.data_total_len=data['data_total_len']
	else:
		print("No value found for data_total_len\n")
	if(data.get('data_part')!=None):
		output.data_part=numpy.zeros(len(data['data_part']),dtype=numpy.uint8)
		for i in range(len(data['data_part'])):
			output.data_part[i]=data['data_part'][i]
	return output

def yaml_loader_com_robotraconteur_image_FreeformImagePart(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.image.FreeformImagePart")
	if(data.get('image_info')!=None):
		output.image_info = yaml_loader_com_robotraconteur_image_FreeformImageInfo(RRN,data['image_info'])
	if(data.get('data_offset')!=None):
		output.data_offset=data['data_offset']
	else:
		print("No value found for data_offset\n")
	if(data.get('data_total_len')!=None):
		output.data_total_len=data['data_total_len']
	else:
		print("No value found for data_total_len\n")
	return output

def yaml_loader_com_robotraconteur_image_DepthImage(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.image.DepthImage")
	if(data.get('depth_image')!=None):
		output.depth_image = yaml_loader_com_robotraconteur_image_Image(RRN,data['depth_image'])
	if(data.get('intensity_image')!=None):
		output.intensity_image = yaml_loader_com_robotraconteur_image_Image(RRN,data['intensity_image'])
	if(data.get('depth_ticks_per_meter')!=None):
		output.depth_ticks_per_meter=data['depth_ticks_per_meter']
	else:
		print("No value found for depth_ticks_per_meter\n")
	return output

def yaml_loader_com_robotraconteur_image_FreeformDepthImage(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.image.FreeformDepthImage")
	if(data.get('depth_image')!=None):
		output.depth_image = yaml_loader_com_robotraconteur_image_FreeformImage(RRN,data['depth_image'])
	if(data.get('intensity_image')!=None):
		output.intensity_image = yaml_loader_com_robotraconteur_image_FreeformImage(RRN,data['intensity_image'])
	if(data.get('depth_ticks_per_meter')!=None):
		output.depth_ticks_per_meter=data['depth_ticks_per_meter']
	else:
		print("No value found for depth_ticks_per_meter\n")
	return output

def yaml_loader_com_robotraconteur_image_ImageResource(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.image.ImageResource")
	if(data.get('image_resource')!=None):
		output.image_resource = YAMLconverter__com_robotraconteur_resource.yaml_loader_com_robotraconteur_resource_ResourceIdentifier(RRN,data['image_resource'])
	return output

#TODO: Fix the following structures or namedarrays: 
# com.robotraconteur.image.ImageResource 

