#!/usr/bin/env python
import yaml
import numpy
import python_enums
import YAMLconverter__com_robotraconteur_units
import YAMLconverter__com_robotraconteur_identifier
def yaml_loader_com_robotraconteur_robotics_joints_JointLimits(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.robotics.joints.JointLimits")
	if(data.get('lower')!=None):
		output.lower=data['lower']
	else:
		print("No value found for lower\n")
	if(data.get('upper')!=None):
		output.upper=data['upper']
	else:
		print("No value found for upper\n")
	if(data.get('home')!=None):
		output.home=data['home']
	else:
		print("No value found for home\n")
	if(data.get('velocity')!=None):
		output.velocity=data['velocity']
	else:
		print("No value found for velocity\n")
	if(data.get('acceleration')!=None):
		output.acceleration=data['acceleration']
	else:
		print("No value found for acceleration\n")
	if(data.get('jerk')!=None):
		output.jerk=data['jerk']
	else:
		print("No value found for jerk\n")
	if(data.get('effort')!=None):
		output.effort=data['effort']
	else:
		print("No value found for effort\n")
	if(data.get('reduced_velocity')!=None):
		output.reduced_velocity=data['reduced_velocity']
	else:
		print("No value found for reduced_velocity\n")
	if(data.get('reduced_acceleration')!=None):
		output.reduced_acceleration=data['reduced_acceleration']
	else:
		print("No value found for reduced_acceleration\n")
	if(data.get('reduced_effort')!=None):
		output.reduced_effort=data['reduced_effort']
	else:
		print("No value found for reduced_effort\n")
	return output

def yaml_loader_com_robotraconteur_robotics_joints_JointInfo(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.robotics.joints.JointInfo")
	if(data.get('joint_identifier')!=None):
		output.joint_identifier = YAMLconverter__com_robotraconteur_identifier.yaml_loader_com_robotraconteur_identifier_Identifier(RRN,data['joint_identifier'])
	if(data.get('joint_type')!=None):
		output.joint_type=python_enums.string_to_enum_JointType	if(data.get('joint_limits')!=None):
		output.joint_limits = yaml_loader_com_robotraconteur_robotics_joints_JointLimits(RRN,data['joint_limits'])
	if(data.get('default_units')!=None):
		output.default_units=python_enums.string_to_enum_JointPositionUnits	if(data.get('default_effort_units')!=None):
		output.default_effort_units=python_enums.string_to_enum_JointEffortUnits	if(data.get('passive')!=None):
		output.passive=data['passive']
	else:
		print("No value found for passive\n")
	return output


