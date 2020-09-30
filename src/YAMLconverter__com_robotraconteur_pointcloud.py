#!/usr/bin/env python
import yaml
import numpy
import python_enums
import YAMLconverter__com_robotraconteur_geometry
import YAMLconverter__com_robotraconteur_geometryf
import YAMLconverter__com_robotraconteur_image
def yaml_loader_com_robotraconteur_pointcloud_PointCloud2Point(RRN,data):
	output_type=RRN.GetNamedArrayDType("com.robotraconteur.pointcloud.PointCloud2Point")
	output=numpy.zeros((1,),dtype=output_type)
	output[0]['point']= YAMLconverter__com_robotraconteur_geometry.yaml_loader_com_robotraconteur_geometry_Point(RRN,data['point'])
	output[0]['intensity']=data['intensity']
	output[0]['normal']= YAMLconverter__com_robotraconteur_geometry.yaml_loader_com_robotraconteur_geometry_Vector3(RRN,data['normal'])
	output[0]['rgb']= YAMLconverter__com_robotraconteur_image.yaml_loader_com_robotraconteur_image_PixelRGBFloatPacked(RRN,data['rgb'])
	array=numpy.zeros(len(data[moment_invariants]),dtype=numpy.double)
	for i in range(len(data['moment_invariants'])):
		array[i]=data['moment_invariants'][i]
	output[0]['moment_invariants']=array
	output[0]['channel']=data['channel']
	return output

def yaml_loader_com_robotraconteur_pointcloud_PointCloud2Pointf(RRN,data):
	output_type=RRN.GetNamedArrayDType("com.robotraconteur.pointcloud.PointCloud2Pointf")
	output=numpy.zeros((1,),dtype=output_type)
	output[0]['point']= YAMLconverter__com_robotraconteur_geometryf_Point.yaml_loader_com_robotraconteur_geometryf_Point(RRN,data['point'])
	output[0]['intensity']=data['intensity']
	output[0]['normal']= YAMLconverter__com_robotraconteur_geometryf_Vector3.yaml_loader_com_robotraconteur_geometryf_Vector3(RRN,data['normal'])
	output[0]['rgb']= YAMLconverter__com_robotraconteur_image.yaml_loader_com_robotraconteur_image_PixelRGBFloatPackedf(RRN,data['rgb'])
	array=numpy.zeros(len(data['moment_invariants']),dtype=numpy.single)
	for i in range(len(data['moment_invariants'])):
		array[i]=data['moment_invariants'][i]
	output[0]['moment_invariants']=array
	output[0]['channel']=data['channel']
	return output

def yaml_loader_com_robotraconteur_pointcloud_PointCloud(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.pointcloud.PointCloud")
	if(data.get('width')!=None):
		output.width=data['width']
	else:
		print("No value found for width\n")
	if(data.get('height')!=None):
		output.height=data['height']
	else:
		print("No value found for height\n")
	if(data.get('is_dense')!=None):
		output.is_dense=data['is_dense']
	else:
		print("No value found for is_dense\n")
	if(data.get('points')!=None):
		dtype=RRN.GetNamedArrayDType("com.robotraconteur.geometry.Point")
		myarray=numpy.zeros((len(data['points'],),dtype=dtype)
		for i in range(len(data['points'])):
			myarray[i] = YAMLconverter__com_robotraconteur_geometry.yaml_loader_com_robotraconteur_geometry_Point(RRN,data['points'][i])
		output.points=myarray
	return output

def yaml_loader_com_robotraconteur_pointcloud_PointCloudPart(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.pointcloud.PointCloudPart")
	if(data.get('width')!=None):
		output.width=data['width']
	else:
		print("No value found for width\n")
	if(data.get('height')!=None):
		output.height=data['height']
	else:
		print("No value found for height\n")
	if(data.get('is_dense')!=None):
		output.is_dense=data['is_dense']
	else:
		print("No value found for is_dense\n")
	if(data.get('points_offset')!=None):
		output.points_offset=data['points_offset']
	else:
		print("No value found for points_offset\n")
	if(data.get('points_total_len')!=None):
		output.points_total_len=data['points_total_len']
	else:
		print("No value found for points_total_len\n")
	if(data.get('points')!=None):
		dtype=RRN.GetNamedArrayDType("com.robotraconteur.geometry.Point")
		myarray=numpy.zeros((len(data['points'],),dtype=dtype)
		for i in range(len(data['points'])):
			myarray[i] = YAMLconverter__com_robotraconteur_geometry.yaml_loader_com_robotraconteur_geometry_Point(RRN,data['points'][i])
		output.points=myarray
	return output

def yaml_loader_com_robotraconteur_pointcloud_PointCloudf(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.pointcloud.PointCloudf")
	if(data.get('width')!=None):
		output.width=data['width']
	else:
		print("No value found for width\n")
	if(data.get('height')!=None):
		output.height=data['height']
	else:
		print("No value found for height\n")
	if(data.get('is_dense')!=None):
		output.is_dense=data['is_dense']
	else:
		print("No value found for is_dense\n")
	if(data.get('points')!=None):
		dtype=RRN.GetNamedArrayDType("com.robotraconteur.geometryf.Point")
		myarray=numpy.zeros((len(data['points'],),dtype=dtype)
		for i in range(len(data['points'])):
			myarray[i] = YAMLconverter__com_robotraconteur_geometryf_Point.yaml_loader_com_robotraconteur_geometryf_Point(RRN,data['points'][i])
		output.points=myarray
	return output

def yaml_loader_com_robotraconteur_pointcloud_PointCloudPartf(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.pointcloud.PointCloudPartf")
	if(data.get('width')!=None):
		output.width=data['width']
	else:
		print("No value found for width\n")
	if(data.get('height')!=None):
		output.height=data['height']
	else:
		print("No value found for height\n")
	if(data.get('is_dense')!=None):
		output.is_dense=data['is_dense']
	else:
		print("No value found for is_dense\n")
	if(data.get('points_offset')!=None):
		output.points_offset=data['points_offset']
	else:
		print("No value found for points_offset\n")
	if(data.get('points_total_len')!=None):
		output.points_total_len=data['points_total_len']
	else:
		print("No value found for points_total_len\n")
	if(data.get('points')!=None):
		dtype=RRN.GetNamedArrayDType("com.robotraconteur.geometryf.Point")
		myarray=numpy.zeros((len(data['points'],),dtype=dtype)
		for i in range(len(data['points'])):
			myarray[i] = YAMLconverter__com_robotraconteur_geometryf_Point.yaml_loader_com_robotraconteur_geometryf_Point(RRN,data['points'][i])
		output.points=myarray
	return output

def yaml_loader_com_robotraconteur_pointcloud_PointCloud2(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.pointcloud.PointCloud2")
	if(data.get('width')!=None):
		output.width=data['width']
	else:
		print("No value found for width\n")
	if(data.get('height')!=None):
		output.height=data['height']
	else:
		print("No value found for height\n")
	if(data.get('is_dense')!=None):
		output.is_dense=data['is_dense']
	else:
		print("No value found for is_dense\n")
	if(data.get('points')!=None):
		dtype=RRN.GetNamedArrayDType("com.robotraconteur.pointcloud.PointCloud2Point")
		myarray=numpy.zeros((len(data['points'],),dtype=dtype)
		for i in range(len(data['points'])):
			myarray[i]=yaml_loader_com_robotraconteur_pointcloud_PointCloud2Point(RRN,data['points'][i])
		output.points=myarray
	return output

def yaml_loader_com_robotraconteur_pointcloud_PointCloud2Part(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.pointcloud.PointCloud2Part")
	if(data.get('width')!=None):
		output.width=data['width']
	else:
		print("No value found for width\n")
	if(data.get('height')!=None):
		output.height=data['height']
	else:
		print("No value found for height\n")
	if(data.get('is_dense')!=None):
		output.is_dense=data['is_dense']
	else:
		print("No value found for is_dense\n")
	if(data.get('points_offset')!=None):
		output.points_offset=data['points_offset']
	else:
		print("No value found for points_offset\n")
	if(data.get('points_total_len')!=None):
		output.points_total_len=data['points_total_len']
	else:
		print("No value found for points_total_len\n")
	if(data.get('points')!=None):
		dtype=RRN.GetNamedArrayDType("com.robotraconteur.pointcloud.PointCloud2Point")
		myarray=numpy.zeros((len(data['points'],),dtype=dtype)
		for i in range(len(data['points'])):
			myarray[i]=yaml_loader_com_robotraconteur_pointcloud_PointCloud2Point(RRN,data['points'][i])
		output.points=myarray
	return output

def yaml_loader_com_robotraconteur_pointcloud_PointCloud2f(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.pointcloud.PointCloud2f")
	if(data.get('width')!=None):
		output.width=data['width']
	else:
		print("No value found for width\n")
	if(data.get('height')!=None):
		output.height=data['height']
	else:
		print("No value found for height\n")
	if(data.get('is_dense')!=None):
		output.is_dense=data['is_dense']
	else:
		print("No value found for is_dense\n")
	if(data.get('points')!=None):
		dtype=RRN.GetNamedArrayDType("com.robotraconteur.pointcloud.PointCloud2Pointf")
		myarray=numpy.zeros((len(data['points'],),dtype=dtype)
		for i in range(len(data['points'])):
			myarray[i]=yaml_loader_com_robotraconteur_pointcloud_PointCloud2Pointf(RRN,data['points'][i])
		output.points=myarray
	return output

def yaml_loader_com_robotraconteur_pointcloud_PointCloud2Partf(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.pointcloud.PointCloud2Partf")
	if(data.get('width')!=None):
		output.width=data['width']
	else:
		print("No value found for width\n")
	if(data.get('height')!=None):
		output.height=data['height']
	else:
		print("No value found for height\n")
	if(data.get('is_dense')!=None):
		output.is_dense=data['is_dense']
	else:
		print("No value found for is_dense\n")
	if(data.get('points_offset')!=None):
		output.points_offset=data['points_offset']
	else:
		print("No value found for points_offset\n")
	if(data.get('points_total_len')!=None):
		output.points_total_len=data['points_total_len']
	else:
		print("No value found for points_total_len\n")
	if(data.get('points')!=None):
		dtype=RRN.GetNamedArrayDType("com.robotraconteur.pointcloud.PointCloud2Pointf")
		myarray=numpy.zeros((len(data['points'],),dtype=dtype)
		for i in range(len(data['points'])):
			myarray[i]=yaml_loader_com_robotraconteur_pointcloud_PointCloud2Pointf(RRN,data['points'][i])
		output.points=myarray
	return output

def yaml_loader_com_robotraconteur_pointcloud_FreeformPointCloud(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.pointcloud.FreeformPointCloud")
	if(data.get('width')!=None):
		output.width=data['width']
	else:
		print("No value found for width\n")
	if(data.get('height')!=None):
		output.height=data['height']
	else:
		print("No value found for height\n")
	if(data.get('encoding')!=None):
		output.encoding=data['encoding']
	else:
		print("No value found for encoding\n")
	if(data.get('is_dense')!=None):
		output.is_dense=data['is_dense']
	else:
		print("No value found for is_dense\n")
	return output

def yaml_loader_com_robotraconteur_pointcloud_FreeformPointCloudPart(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.pointcloud.FreeformPointCloudPart")
	if(data.get('width')!=None):
		output.width=data['width']
	else:
		print("No value found for width\n")
	if(data.get('height')!=None):
		output.height=data['height']
	else:
		print("No value found for height\n")
	if(data.get('encoding')!=None):
		output.encoding=data['encoding']
	else:
		print("No value found for encoding\n")
	if(data.get('is_dense')!=None):
		output.is_dense=data['is_dense']
	else:
		print("No value found for is_dense\n")
	if(data.get('points_offset')!=None):
		output.points_offset=data['points_offset']
	else:
		print("No value found for points_offset\n")
	if(data.get('points_total_len')!=None):
		output.points_total_len=data['points_total_len']
	else:
		print("No value found for points_total_len\n")
	return output

#TODO: Fix the following structures or namedarrays: 
# com.robotraconteur.pointcloud.FreeformPointCloudPart 

