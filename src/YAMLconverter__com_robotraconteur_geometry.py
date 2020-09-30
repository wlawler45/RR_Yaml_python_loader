#!/usr/bin/env python
import yaml
import numpy
import python_enums
import YAMLconverter__com_robotraconteur_identifier
def yaml_loader_com_robotraconteur_geometry_Vector2(RRN,data):
	output_type=RRN.GetNamedArrayDType("com.robotraconteur.geometry.Vector2")
	output=numpy.zeros((1,),dtype=output_type)
	output[0]['x']=data['x']
	output[0]['y']=data['y']
	return output

def yaml_loader_com_robotraconteur_geometry_Vector3(RRN,data):
	output_type=RRN.GetNamedArrayDType("com.robotraconteur.geometry.Vector3")
	output=numpy.zeros((1,),dtype=output_type)
	output[0]['x']=data['x']
	output[0]['y']=data['y']
	output[0]['z']=data['z']
	return output

def yaml_loader_com_robotraconteur_geometry_Vector6(RRN,data):
	output_type=RRN.GetNamedArrayDType("com.robotraconteur.geometry.Vector6")
	output=numpy.zeros((1,),dtype=output_type)
	output[0]['alpha']=data['alpha']
	output[0]['beta']=data['beta']
	output[0]['gamma']=data['gamma']
	output[0]['x']=data['x']
	output[0]['y']=data['y']
	output[0]['z']=data['z']
	return output

def yaml_loader_com_robotraconteur_geometry_Point2D(RRN,data):
	output_type=RRN.GetNamedArrayDType("com.robotraconteur.geometry.Point2D")
	output=numpy.zeros((1,),dtype=output_type)
	output[0]['x']=data['x']
	output[0]['y']=data['y']
	return output

def yaml_loader_com_robotraconteur_geometry_Point(RRN,data):
	output_type=RRN.GetNamedArrayDType("com.robotraconteur.geometry.Point")
	output=numpy.zeros((1,),dtype=output_type)
	output[0]['x']=data['x']
	output[0]['y']=data['y']
	output[0]['z']=data['z']
	return output

def yaml_loader_com_robotraconteur_geometry_Size2D(RRN,data):
	output_type=RRN.GetNamedArrayDType("com.robotraconteur.geometry.Size2D")
	output=numpy.zeros((1,),dtype=output_type)
	output[0]['width']=data['width']
	output[0]['height']=data['height']
	return output

def yaml_loader_com_robotraconteur_geometry_Size(RRN,data):
	output_type=RRN.GetNamedArrayDType("com.robotraconteur.geometry.Size")
	output=numpy.zeros((1,),dtype=output_type)
	output[0]['width']=data['width']
	output[0]['height']=data['height']
	output[0]['depth']=data['depth']
	return output

def yaml_loader_com_robotraconteur_geometry_Rect(RRN,data):
	output_type=RRN.GetNamedArrayDType("com.robotraconteur.geometry.Rect")
	output=numpy.zeros((1,),dtype=output_type)
	output[0]['origin'] = yaml_loader_com_robotraconteur_geometry_Point2D(RRN,data['origin'])
	output[0]['size'] = yaml_loader_com_robotraconteur_geometry_Size2D(RRN,data['size'])
	return output

def yaml_loader_com_robotraconteur_geometry_Box(RRN,data):
	output_type=RRN.GetNamedArrayDType("com.robotraconteur.geometry.Box")
	output=numpy.zeros((1,),dtype=output_type)
	output[0]['origin'] = yaml_loader_com_robotraconteur_geometry_Point(RRN,data['origin'])
	output[0]['size'] = yaml_loader_com_robotraconteur_geometry_Size(RRN,data['size'])
	return output

def yaml_loader_com_robotraconteur_geometry_Quaternion(RRN,data):
	output_type=RRN.GetNamedArrayDType("com.robotraconteur.geometry.Quaternion")
	output=numpy.zeros((1,),dtype=output_type)
	output[0]['w']=data['w']
	output[0]['x']=data['x']
	output[0]['y']=data['y']
	output[0]['z']=data['z']
	return output

def yaml_loader_com_robotraconteur_geometry_Plane(RRN,data):
	output_type=RRN.GetNamedArrayDType("com.robotraconteur.geometry.Plane")
	output=numpy.zeros((1,),dtype=output_type)
	output[0]['normal'] = yaml_loader_com_robotraconteur_geometry_Vector3(RRN,data['normal'])
	output[0]['a']=data['a']
	return output

def yaml_loader_com_robotraconteur_geometry_Transform(RRN,data):
	output_type=RRN.GetNamedArrayDType("com.robotraconteur.geometry.Transform")
	output=numpy.zeros((1,),dtype=output_type)
	output[0]['rotation'] = yaml_loader_com_robotraconteur_geometry_Quaternion(RRN,data['rotation'])
	output[0]['translation'] = yaml_loader_com_robotraconteur_geometry_Vector3(RRN,data['translation'])
	return output

def yaml_loader_com_robotraconteur_geometry_Pose(RRN,data):
	output_type=RRN.GetNamedArrayDType("com.robotraconteur.geometry.Pose")
	output=numpy.zeros((1,),dtype=output_type)
	output[0]['orientation'] = yaml_loader_com_robotraconteur_geometry_Quaternion(RRN,data['orientation'])
	output[0]['position'] = yaml_loader_com_robotraconteur_geometry_Point(RRN,data['position'])
	return output

def yaml_loader_com_robotraconteur_geometry_Pose2D(RRN,data):
	output_type=RRN.GetNamedArrayDType("com.robotraconteur.geometry.Pose2D")
	output=numpy.zeros((1,),dtype=output_type)
	output[0]['orientation']=data['orientation']
	output[0]['position'] = yaml_loader_com_robotraconteur_geometry_Point2D(RRN,data['position'])
	return output

def yaml_loader_com_robotraconteur_geometry_SpatialVelocity(RRN,data):
	output_type=RRN.GetNamedArrayDType("com.robotraconteur.geometry.SpatialVelocity")
	output=numpy.zeros((1,),dtype=output_type)
	output[0]['angular'] = yaml_loader_com_robotraconteur_geometry_Vector3(RRN,data['angular'])
	output[0]['linear'] = yaml_loader_com_robotraconteur_geometry_Vector3(RRN,data['linear'])
	return output

def yaml_loader_com_robotraconteur_geometry_SpatialAcceleration(RRN,data):
	output_type=RRN.GetNamedArrayDType("com.robotraconteur.geometry.SpatialAcceleration")
	output=numpy.zeros((1,),dtype=output_type)
	output[0]['angular'] = yaml_loader_com_robotraconteur_geometry_Vector3(RRN,data['angular'])
	output[0]['linear'] = yaml_loader_com_robotraconteur_geometry_Vector3(RRN,data['linear'])
	return output

def yaml_loader_com_robotraconteur_geometry_Wrench(RRN,data):
	output_type=RRN.GetNamedArrayDType("com.robotraconteur.geometry.Wrench")
	output=numpy.zeros((1,),dtype=output_type)
	output[0]['torque'] = yaml_loader_com_robotraconteur_geometry_Vector3(RRN,data['torque'])
	output[0]['force'] = yaml_loader_com_robotraconteur_geometry_Vector3(RRN,data['force'])
	return output

def yaml_loader_com_robotraconteur_geometry_SpatialInertia(RRN,data):
	output_type=RRN.GetNamedArrayDType("com.robotraconteur.geometry.SpatialInertia")
	output=numpy.zeros((1,),dtype=output_type)
	output[0]['m']=data['m']
	output[0]['com'] = yaml_loader_com_robotraconteur_geometry_Vector3(RRN,data['com'])
	output[0]['ixx']=data['ixx']
	output[0]['ixy']=data['ixy']
	output[0]['ixz']=data['ixz']
	output[0]['iyy']=data['iyy']
	output[0]['iyz']=data['iyz']
	output[0]['izz']=data['izz']
	return output

def yaml_loader_com_robotraconteur_geometry_NamedTransform(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.geometry.NamedTransform")
	if(data.get('parent_frame')!=None):
		output.parent_frame = YAMLconverter__com_robotraconteur_identifier.yaml_loader_com_robotraconteur_identifier_Identifier(RRN,data['parent_frame'])
	if(data.get('child_frame')!=None):
		output.child_frame = YAMLconverter__com_robotraconteur_identifier.yaml_loader_com_robotraconteur_identifier_Identifier(RRN,data['child_frame'])
	if(data.get('transform')!=None):
		output.transform = yaml_loader_com_robotraconteur_geometry_Transform(RRN,data['transform'])
	return output

def yaml_loader_com_robotraconteur_geometry_NamedPose(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.geometry.NamedPose")
	if(data.get('parent_frame')!=None):
		output.parent_frame = YAMLconverter__com_robotraconteur_identifier.yaml_loader_com_robotraconteur_identifier_Identifier(RRN,data['parent_frame'])
	if(data.get('frame')!=None):
		output.frame = YAMLconverter__com_robotraconteur_identifier.yaml_loader_com_robotraconteur_identifier_Identifier(RRN,data['frame'])
	if(data.get('pose')!=None):
		output.pose = yaml_loader_com_robotraconteur_geometry_Pose(RRN,data['pose'])
	return output

def yaml_loader_com_robotraconteur_geometry_PoseWithCovariance(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.geometry.PoseWithCovariance")
	if(data.get('pose')!=None):
		output.pose = yaml_loader_com_robotraconteur_geometry_Pose(RRN,data['pose'])
	if(data.get('covariance')!=None):
		array=numpy.zeros(len(data['covariance']),dtype=numpy.double)
		for i in range(len(data['covariance'])):
			array[i]=data['covariance'][i]
		array=array.reshape(6,6)
		output.covariance=array
	else:
		print("No value found for covariance\n")
	return output

def yaml_loader_com_robotraconteur_geometry_NamedPoseWithCovariance(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.geometry.NamedPoseWithCovariance")
	if(data.get('pose')!=None):
		output.pose = yaml_loader_com_robotraconteur_geometry_NamedPose(RRN,data['pose'])
	if(data.get('covariance')!=None):
		array=numpy.zeros(len(data['covariance']),dtype=numpy.double)
		for i in range(len(data['covariance'])):
			array[i]=data['covariance'][i]
		array=array.reshape(6,6)
		output.covariance=array
	else:
		print("No value found for covariance\n")
	return output

def yaml_loader_com_robotraconteur_geometry_NamedPose2D(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.geometry.NamedPose2D")
	if(data.get('parent_frame')!=None):
		output.parent_frame = YAMLconverter__com_robotraconteur_identifier.yaml_loader_com_robotraconteur_identifier_Identifier(RRN,data['parent_frame'])
	if(data.get('frame')!=None):
		output.frame = YAMLconverter__com_robotraconteur_identifier.yaml_loader_com_robotraconteur_identifier_Identifier(RRN,data['frame'])
	if(data.get('pose')!=None):
		output.pose = yaml_loader_com_robotraconteur_geometry_Pose2D(RRN,data['pose'])
	return output

def yaml_loader_com_robotraconteur_geometry_NamedSpatialVelocity(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.geometry.NamedSpatialVelocity")
	if(data.get('frame')!=None):
		output.frame = YAMLconverter__com_robotraconteur_identifier.yaml_loader_com_robotraconteur_identifier_Identifier(RRN,data['frame'])
	if(data.get('velocity')!=None):
		output.velocity = yaml_loader_com_robotraconteur_geometry_SpatialVelocity(RRN,data['velocity'])
	return output

def yaml_loader_com_robotraconteur_geometry_NamedSpatialAcceleration(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.geometry.NamedSpatialAcceleration")
	if(data.get('frame')!=None):
		output.frame = YAMLconverter__com_robotraconteur_identifier.yaml_loader_com_robotraconteur_identifier_Identifier(RRN,data['frame'])
	if(data.get('Acceleration')!=None):
		output.Acceleration = yaml_loader_com_robotraconteur_geometry_SpatialAcceleration(RRN,data['Acceleration'])
	return output

def yaml_loader_com_robotraconteur_geometry_NamedWrench(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.geometry.NamedWrench")
	if(data.get('frame')!=None):
		output.frame = YAMLconverter__com_robotraconteur_identifier.yaml_loader_com_robotraconteur_identifier_Identifier(RRN,data['frame'])
	if(data.get('wrench')!=None):
		output.wrench = yaml_loader_com_robotraconteur_geometry_Wrench(RRN,data['wrench'])
	return output

def yaml_loader_com_robotraconteur_geometry_NamedSpatialInertia(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.geometry.NamedSpatialInertia")
	if(data.get('frame')!=None):
		output.frame = YAMLconverter__com_robotraconteur_identifier.yaml_loader_com_robotraconteur_identifier_Identifier(RRN,data['frame'])
	if(data.get('inertia')!=None):
		output.inertia = yaml_loader_com_robotraconteur_geometry_SpatialInertia(RRN,data['inertia'])
	return output


