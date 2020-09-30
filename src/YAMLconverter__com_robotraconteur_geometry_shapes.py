#!/usr/bin/env python
import yaml
import numpy
import python_enums
import YAMLconverter__com_robotraconteur_geometry
import YAMLconverter__com_robotraconteur_identifier
import YAMLconverter__com_robotraconteur_color
import YAMLconverter__com_robotraconteur_resource
def yaml_loader_com_robotraconteur_geometry_shapes_MeshTriangle(RRN,data):
	output_type=RRN.GetNamedArrayDType("com.robotraconteur.geometry.shapes.MeshTriangle")
	output=numpy.zeros((1,),dtype=output_type)
	output[0]['v1']=data['v1']
	output[0]['v2']=data['v2']
	output[0]['v3']=data['v3']
	return output

def yaml_loader_com_robotraconteur_geometry_shapes_Box(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.geometry.shapes.Box")
	if(data.get('x')!=None):
		output.x=data['x']
	else:
		print("No value found for x\n")
	if(data.get('y')!=None):
		output.y=data['y']
	else:
		print("No value found for y\n")
	if(data.get('z')!=None):
		output.z=data['z']
	else:
		print("No value found for z\n")
	return output

def yaml_loader_com_robotraconteur_geometry_shapes_Sphere(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.geometry.shapes.Sphere")
	if(data.get('radius')!=None):
		output.radius=data['radius']
	else:
		print("No value found for radius\n")
	return output

def yaml_loader_com_robotraconteur_geometry_shapes_Cylinder(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.geometry.shapes.Cylinder")
	if(data.get('height')!=None):
		output.height=data['height']
	else:
		print("No value found for height\n")
	if(data.get('radius')!=None):
		output.radius=data['radius']
	else:
		print("No value found for radius\n")
	return output

def yaml_loader_com_robotraconteur_geometry_shapes_Cone(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.geometry.shapes.Cone")
	if(data.get('height')!=None):
		output.height=data['height']
	else:
		print("No value found for height\n")
	if(data.get('radius')!=None):
		output.radius=data['radius']
	else:
		print("No value found for radius\n")
	return output

def yaml_loader_com_robotraconteur_geometry_shapes_Mesh(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.geometry.shapes.Mesh")
	if(data.get('triangles')!=None):
		dtype=RRN.GetNamedArrayDType("com.robotraconteur.geometry.shapes.MeshTriangle")
		myarray=numpy.zeros((len(data['triangles'],),dtype=dtype)
		for i in range(len(data['triangles'])):
			myarray[i]=yaml_loader_com_robotraconteur_geometry_shapes_MeshTriangle(RRN,data['triangles'][i])
		output.triangles=myarray
	if(data.get('vertices')!=None):
		dtype=RRN.GetNamedArrayDType("com.robotraconteur.geometry.Point")
		myarray=numpy.zeros((len(data['vertices'],),dtype=dtype)
		for i in range(len(data['vertices'])):
			myarray[i] = YAMLconverter__com_robotraconteur_geometry.yaml_loader_com_robotraconteur_geometry_Point(RRN,data['vertices'][i])
		output.vertices=myarray
	return output

def yaml_loader_com_robotraconteur_geometry_shapes_MeshFromResource(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.geometry.shapes.MeshFromResource")
	if(data.get('mesh_resource')!=None):
		output.mesh_resource = YAMLconverter__com_robotraconteur_resource.yaml_loader_com_robotraconteur_resource_ResourceIdentifier(RRN,data['mesh_resource'])
	return output

def yaml_loader_com_robotraconteur_geometry_shapes_ShapeObject(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.geometry.shapes.ShapeObject")
	if(data.get('name')!=None):
		output.name = YAMLconverter__com_robotraconteur_identifier.yaml_loader_com_robotraconteur_identifier_Identifier(RRN,data['name'])
	if(data.get('shape_poses')!=None):
		mylist=[]
		for i in range(len(data['shape_poses'])):
			mylist.append(YAMLconverter__com_robotraconteur_geometry.yaml_loader_com_robotraconteur_geometry_Pose(RRN,data['shape_poses'][i]))
		output.shape_poses=mylist
	if(data.get('shape_colors')!=None):
		mylist=[]
		for i in range(len(data['shape_colors'])):
			mylist.append(YAMLconverter__com_robotraconteur_color.yaml_loader_com_robotraconteur_color_ColorRGBA(RRN,data['shape_colors'][i]))
		output.shape_colors=mylist
	if(data.get('inertia')!=None):
		output.inertia = YAMLconverter__com_robotraconteur_geometry.yaml_loader_com_robotraconteur_geometry_SpatialInertia(RRN,data['inertia'])
	return output


