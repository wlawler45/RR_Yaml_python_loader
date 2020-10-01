#!/usr/bin/env python
import yaml
import numpy
import python_enums
import YAMLconverter__com_robotraconteur_geometry
import YAMLconverter__com_robotraconteur_identifier
import YAMLconverter__com_robotraconteur_color
import YAMLconverter__com_robotraconteur_resource
import YAMLconverter__com_robotraconteur_image
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

def yaml_loader_com_robotraconteur_geometry_shapes_Capsule(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.geometry.shapes.Capsule")
	if(data.get('height')!=None):
		output.height=data['height']
	else:
		print("No value found for height\n")
	if(data.get('radius')!=None):
		output.radius=data['radius']
	else:
		print("No value found for radius\n")
	return output

def yaml_loader_com_robotraconteur_geometry_shapes_Plane(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.geometry.shapes.Plane")
	if(data.get('a')!=None):
		output.a=data['a']
	else:
		print("No value found for a\n")
	if(data.get('b')!=None):
		output.b=data['b']
	else:
		print("No value found for b\n")
	if(data.get('c')!=None):
		output.c=data['c']
	else:
		print("No value found for c\n")
	if(data.get('d')!=None):
		output.d=data['d']
	else:
		print("No value found for d\n")
	return output

def yaml_loader_com_robotraconteur_geometry_shapes_MeshTexture(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.geometry.shapes.MeshTexture")
	if(data.get('image')!=None):
		output.image = YAMLconverter__com_robotraconteur_image.yaml_loader_com_robotraconteur_image_CompressedImage(RRN,data['image'])
	if(data.get('uvs')!=None):
		output.uvs = YAMLconverter__com_robotraconteur_geometry.yaml_loader_com_robotraconteur_geometry_Vector2(RRN,data['uvs'])
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
	if(data.get('normals')!=None):
		dtype=RRN.GetNamedArrayDType("com.robotraconteur.geometry.Vector3")
		myarray=numpy.zeros((len(data['normals'],),dtype=dtype)
		for i in range(len(data['normals'])):
			myarray[i] = YAMLconverter__com_robotraconteur_geometry.yaml_loader_com_robotraconteur_geometry_Vector3(RRN,data['normals'][i])
		output.normals=myarray
	if(data.get('colors')!=None):
		dtype=RRN.GetNamedArrayDType("com.robotraconteur.color.ColorRGB")
		myarray=numpy.zeros((len(data['colors'],),dtype=dtype)
		for i in range(len(data['colors'])):
			myarray[i] = YAMLconverter__com_robotraconteur_color.yaml_loader_com_robotraconteur_color_ColorRGB(RRN,data['colors'][i])
		output.colors=myarray
	if(data.get('textures')!=None):
		mylist=[]
		for i in range(len(data['textures'])):
			mylist.append(yaml_loader_com_robotraconteur_geometry_shapes_MeshTexture(RRN,data['textures'][i]))
		output.textures=mylist
	if(data.get('mesh_type')!=None):
		output.mesh_type=python_enums.string_to_enum_MeshType	return output

def yaml_loader_com_robotraconteur_geometry_shapes_Material(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.geometry.shapes.Material")
	if(data.get('albedo')!=None):
		output.albedo = YAMLconverter__com_robotraconteur_color.yaml_loader_com_robotraconteur_color_ColorRGB(RRN,data['albedo'])
	if(data.get('alpha')!=None):
		output.alpha=data['alpha']
	else:
		print("No value found for alpha\n")
	if(data.get('reflectivity')!=None):
		output.reflectivity = YAMLconverter__com_robotraconteur_color.yaml_loader_com_robotraconteur_color_ColorRGB(RRN,data['reflectivity'])
	if(data.get('roughness')!=None):
		output.roughness=data['roughness']
	else:
		print("No value found for roughness\n")
	if(data.get('emissivity')!=None):
		output.emissivity=data['emissivity']
	else:
		print("No value found for emissivity\n")
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
	if(data.get('shape_materials')!=None):
		mylist=[]
		for i in range(len(data['shape_materials'])):
			mylist.append(yaml_loader_com_robotraconteur_geometry_shapes_Material(RRN,data['shape_materials'][i]))
		output.shape_materials=mylist
	if(data.get('inertia')!=None):
		output.inertia = YAMLconverter__com_robotraconteur_geometry.yaml_loader_com_robotraconteur_geometry_SpatialInertia(RRN,data['inertia'])
	return output


