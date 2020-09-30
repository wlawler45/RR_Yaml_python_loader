#!/usr/bin/env python
import yaml
import numpy
import python_enums
import YAMLconverter__com_robotraconteur_identifier
import YAMLconverter__com_robotraconteur_geometry
import YAMLconverter__com_robotraconteur_geometryi
import YAMLconverter__com_robotraconteur_device
def yaml_loader_com_robotraconteur_imaging_camerainfo_PlumbBobDistortionInfo(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.imaging.camerainfo.PlumbBobDistortionInfo")
	if(data.get('k1')!=None):
		output.k1=data['k1']
	else:
		print("No value found for k1\n")
	if(data.get('k2')!=None):
		output.k2=data['k2']
	else:
		print("No value found for k2\n")
	if(data.get('p1')!=None):
		output.p1=data['p1']
	else:
		print("No value found for p1\n")
	if(data.get('p2')!=None):
		output.p2=data['p2']
	else:
		print("No value found for p2\n")
	if(data.get('k3')!=None):
		output.k3=data['k3']
	else:
		print("No value found for k3\n")
	return output

def yaml_loader_com_robotraconteur_imaging_camerainfo_CameraCalibration(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.imaging.camerainfo.CameraCalibration")
	if(data.get('image_size')!=None):
		output.image_size = YAMLconverter__com_robotraconteur_geometryi.yaml_loader_com_robotraconteur_geometryi_Size2D(RRN,data['image_size'])
	if(data.get('K')!=None):
		array=numpy.zeros(len(data['K']),dtype=numpy.double)
		for i in range(len(data['K'])):
			array[i]=data['K'][i]
		array=array.reshape(3,3)
		output.K=array
	else:
		print("No value found for K\n")
	if(data.get('parent_device')!=None):
		output.parent_device = YAMLconverter__com_robotraconteur_identifier.yaml_loader_com_robotraconteur_identifier_Identifier(RRN,data['parent_device'])
	if(data.get('camera_pose')!=None):
		output.camera_pose = YAMLconverter__com_robotraconteur_geometry.yaml_loader_com_robotraconteur_geometry_NamedPose(RRN,data['camera_pose'])
	return output

def yaml_loader_com_robotraconteur_imaging_camerainfo_CameraInfo(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.imaging.camerainfo.CameraInfo")
	if(data.get('device_info')!=None):
		output.device_info = YAMLconverter__com_robotraconteur_device.yaml_loader_com_robotraconteur_device_DeviceInfo(RRN,data['device_info'])
	if(data.get('calibration')!=None):
		output.calibration = yaml_loader_com_robotraconteur_imaging_camerainfo_CameraCalibration(RRN,data['calibration'])
	return output

def yaml_loader_com_robotraconteur_imaging_camerainfo_MultiCameraInfo(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.imaging.camerainfo.MultiCameraInfo")
	if(data.get('device_info')!=None):
		output.device_info = YAMLconverter__com_robotraconteur_device.yaml_loader_com_robotraconteur_device_DeviceInfo(RRN,data['device_info'])
	if(data.get('camera_info_all')!=None):
		mylist=[]
		for i in range(len(data['camera_info_all'])):
			mylist.append(yaml_loader_com_robotraconteur_imaging_camerainfo_CameraInfo(RRN,data['camera_info_all'][i]))
		output.camera_info_all=mylist
	return output

#TODO: Fix the following structures or namedarrays: 
# com.robotraconteur.imaging.camerainfo.MultiCameraInfo 

