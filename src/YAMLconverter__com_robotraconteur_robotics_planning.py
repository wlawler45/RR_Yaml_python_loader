#!/usr/bin/env python
import yaml
import numpy
import python_enums
import YAMLconverter__com_robotraconteur_geometry
import YAMLconverter__com_robotraconteur_robotics_robot
import YAMLconverter__com_robotraconteur_robotics_trajectory
import YAMLconverter__com_robotraconteur_geometry_shapes
import YAMLconverter__com_robotraconteur_identifier
def yaml_loader_com_robotraconteur_robotics_planning_EnvState(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.robotics.planning.EnvState")
	if(data.get('joints')!=None):
		output.joints=numpy.zeros(len(data['joints']),dtype=numpy.double)
		for i in range(len(data['joints'])):
			output.joints[i]=data['joints'][i]
	return output

def yaml_loader_com_robotraconteur_robotics_planning_JointWaypoint(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.robotics.planning.JointWaypoint")
	if(data.get('joint_positions')!=None):
		output.joint_positions=numpy.zeros(len(data['joint_positions']),dtype=numpy.double)
		for i in range(len(data['joint_positions'])):
			output.joint_positions[i]=data['joint_positions'][i]
	if(data.get('coeffs')!=None):
		output.coeffs=numpy.zeros(len(data['coeffs']),dtype=numpy.double)
		for i in range(len(data['coeffs'])):
			output.coeffs[i]=data['coeffs'][i]
	if(data.get('is_critical')!=None):
		output.is_critical=data['is_critical']
	else:
		print("No value found for is_critical\n")
	return output

def yaml_loader_com_robotraconteur_robotics_planning_CartesianWaypoint(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.robotics.planning.CartesianWaypoint")
	if(data.get('cartesion_position')!=None):
		output.cartesion_position = YAMLconverter__com_robotraconteur_geometry.yaml_loader_com_robotraconteur_geometry_Pose(RRN,data['cartesion_position'])
	if(data.get('coeffs')!=None):
		output.coeffs=numpy.zeros(len(data['coeffs']),dtype=numpy.double)
		for i in range(len(data['coeffs'])):
			output.coeffs[i]=data['coeffs'][i]
	if(data.get('is_critical')!=None):
		output.is_critical=data['is_critical']
	else:
		print("No value found for is_critical\n")
	return output

def yaml_loader_com_robotraconteur_robotics_planning_JointTolerancedWaypoint(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.robotics.planning.JointTolerancedWaypoint")
	if(data.get('joint_positions')!=None):
		output.joint_positions=numpy.zeros(len(data['joint_positions']),dtype=numpy.double)
		for i in range(len(data['joint_positions'])):
			output.joint_positions[i]=data['joint_positions'][i]
	if(data.get('lower_tolerance')!=None):
		output.lower_tolerance=numpy.zeros(len(data['lower_tolerance']),dtype=numpy.double)
		for i in range(len(data['lower_tolerance'])):
			output.lower_tolerance[i]=data['lower_tolerance'][i]
	if(data.get('upper_tolerance')!=None):
		output.upper_tolerance=numpy.zeros(len(data['upper_tolerance']),dtype=numpy.double)
		for i in range(len(data['upper_tolerance'])):
			output.upper_tolerance[i]=data['upper_tolerance'][i]
	if(data.get('coeffs')!=None):
		output.coeffs=numpy.zeros(len(data['coeffs']),dtype=numpy.double)
		for i in range(len(data['coeffs'])):
			output.coeffs[i]=data['coeffs'][i]
	if(data.get('is_critical')!=None):
		output.is_critical=data['is_critical']
	else:
		print("No value found for is_critical\n")
	return output

def yaml_loader_com_robotraconteur_robotics_planning_PlanningRequest(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.robotics.planning.PlanningRequest")
	if(data.get('device')!=None):
		output.device = YAMLconverter__com_robotraconteur_identifier.yaml_loader_com_robotraconteur_identifier_Identifier(RRN,data['device'])
	if(data.get('planner_algorithm')!=None):
		output.planner_algorithm = YAMLconverter__com_robotraconteur_identifier.yaml_loader_com_robotraconteur_identifier_Identifier(RRN,data['planner_algorithm'])
	if(data.get('filter_algorithm')!=None):
		output.filter_algorithm = YAMLconverter__com_robotraconteur_identifier.yaml_loader_com_robotraconteur_identifier_Identifier(RRN,data['filter_algorithm'])
	if(data.get('workspace_bounds')!=None):
		output.workspace_bounds = YAMLconverter__com_robotraconteur_geometry.yaml_loader_com_robotraconteur_geometry_Box(RRN,data['workspace_bounds'])
	if(data.get('collision_check')!=None):
		output.collision_check=data['collision_check']
	else:
		print("No value found for collision_check\n")
	if(data.get('collision_safety_margin')!=None):
		output.collision_safety_margin=data['collision_safety_margin']
	else:
		print("No value found for collision_safety_margin\n")
	return output

def yaml_loader_com_robotraconteur_robotics_planning_PlanningResponse(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.robotics.planning.PlanningResponse")
	if(data.get('status_code')!=None):
		output.status_code=python_enums.string_to_enum_PlannerStatusCode	if(data.get('joint_trajectory')!=None):
		output.joint_trajectory = YAMLconverter__com_robotraconteur_robotics_trajectory.yaml_loader_com_robotraconteur_robotics_trajectory_JointTrajectory(RRN,data['joint_trajectory'])
	return output

def yaml_loader_com_robotraconteur_robotics_planning_ContactResult(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.robotics.planning.ContactResult")
	if(data.get('distance')!=None):
		output.distance=data['distance']
	else:
		print("No value found for distance\n")
	if(data.get('shape1_type_id')!=None):
		output.shape1_type_id=data['shape1_type_id']
	else:
		print("No value found for shape1_type_id\n")
	if(data.get('shape2_type_id')!=None):
		output.shape2_type_id=data['shape2_type_id']
	else:
		print("No value found for shape2_type_id\n")
	if(data.get('shape1_name')!=None):
		output.shape1_name=data['shape1_name']
	else:
		print("No value found for shape1_name\n")
	if(data.get('shape2_name')!=None):
		output.shape2_name=data['shape2_name']
	else:
		print("No value found for shape2_name\n")
	if(data.get('shape1_subid')!=None):
		output.shape1_subid=data['shape1_subid']
	else:
		print("No value found for shape1_subid\n")
	if(data.get('shape2_subid')!=None):
		output.shape2_subid=data['shape2_subid']
	else:
		print("No value found for shape2_subid\n")
	if(data.get('shape1_nearest_point')!=None):
		output.shape1_nearest_point = YAMLconverter__com_robotraconteur_geometry.yaml_loader_com_robotraconteur_geometry_Vector3(RRN,data['shape1_nearest_point'])
	if(data.get('shape2_nearest_point')!=None):
		output.shape2_nearest_point = YAMLconverter__com_robotraconteur_geometry.yaml_loader_com_robotraconteur_geometry_Vector3(RRN,data['shape2_nearest_point'])
	if(data.get('normal')!=None):
		output.normal = YAMLconverter__com_robotraconteur_geometry.yaml_loader_com_robotraconteur_geometry_Vector3(RRN,data['normal'])
	if(data.get('shape1_cc_nearest_points')!=None):
		output.shape1_cc_nearest_points = YAMLconverter__com_robotraconteur_geometry.yaml_loader_com_robotraconteur_geometry_Vector3(RRN,data['shape1_cc_nearest_points'])
	if(data.get('shape2_cc_nearest_points')!=None):
		output.shape2_cc_nearest_points = YAMLconverter__com_robotraconteur_geometry.yaml_loader_com_robotraconteur_geometry_Vector3(RRN,data['shape2_cc_nearest_points'])
	if(data.get('cc_time')!=None):
		output.cc_time=data['cc_time']
	else:
		print("No value found for cc_time\n")
	if(data.get('cc_type')!=None):
		output.cc_type=data['cc_type']
	else:
		print("No value found for cc_type\n")
	return output

def yaml_loader_com_robotraconteur_robotics_planning_InvKinResult(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.robotics.planning.InvKinResult")
	if(data.get('joints')!=None):
		output.joints=numpy.zeros(len(data['joints']),dtype=numpy.double)
		for i in range(len(data['joints'])):
			output.joints[i]=data['joints'][i]
	return output

#TODO: Fix the following structures or namedarrays: 
# com.robotraconteur.robotics.planning.InvKinResult 

