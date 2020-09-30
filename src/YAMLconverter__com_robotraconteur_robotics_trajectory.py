#!/usr/bin/env python
import yaml
import numpy
import python_enums
import YAMLconverter__com_robotraconteur_robotics_joints
import YAMLconverter__com_robotraconteur_identifier
import YAMLconverter__com_robotraconteur_action
def yaml_loader_com_robotraconteur_robotics_trajectory_JointTrajectoryWaypoint(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.robotics.trajectory.JointTrajectoryWaypoint")
	if(data.get('joint_position')!=None):
		output.joint_position=numpy.zeros(len(data['joint_position']),dtype=numpy.double)
		for i in range(len(data['joint_position'])):
			output.joint_position[i]=data['joint_position'][i]
	if(data.get('joint_velocity')!=None):
		output.joint_velocity=numpy.zeros(len(data['joint_velocity']),dtype=numpy.double)
		for i in range(len(data['joint_velocity'])):
			output.joint_velocity[i]=data['joint_velocity'][i]
	if(data.get('position_tolerance')!=None):
		output.position_tolerance=numpy.zeros(len(data['position_tolerance']),dtype=numpy.double)
		for i in range(len(data['position_tolerance'])):
			output.position_tolerance[i]=data['position_tolerance'][i]
	if(data.get('velocity_tolerance')!=None):
		output.velocity_tolerance=numpy.zeros(len(data['velocity_tolerance']),dtype=numpy.double)
		for i in range(len(data['velocity_tolerance'])):
			output.velocity_tolerance[i]=data['velocity_tolerance'][i]
	if(data.get('time_from_start')!=None):
		output.time_from_start=data['time_from_start']
	else:
		print("No value found for time_from_start\n")
	return output

def yaml_loader_com_robotraconteur_robotics_trajectory_JointTrajectory(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.robotics.trajectory.JointTrajectory")
	if(data.get('joint_names')!=None):
		mylist=[]
		for i in range(len(data['joint_names'])):
			mylist.append(data['joint_names'][i])
		output.joint_names=mylist
	if(data.get('joint_units')!=None):
		mylist=[]
		for i in range(len(data['joint_units'])):
			mylist.append(YAMLconverter__com_robotraconteur_robotics_joints.yaml_loader_com_robotraconteur_robotics_joints_JointPositionUnits(RRN,data['joint_units'][i]))
		output.joint_units=mylist
	if(data.get('waypoints')!=None):
		mylist=[]
		for i in range(len(data['waypoints'])):
			mylist.append(yaml_loader_com_robotraconteur_robotics_trajectory_JointTrajectoryWaypoint(RRN,data['waypoints'][i]))
		output.waypoints=mylist
	if(data.get('interpolation_mode')!=None):
		output.interpolation_mode=python_enums.string_to_enum_InterpolationMode	return output

def yaml_loader_com_robotraconteur_robotics_trajectory_TrajectoryStatus(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.robotics.trajectory.TrajectoryStatus")
	if(data.get('seqno')!=None):
		output.seqno=data['seqno']
	else:
		print("No value found for seqno\n")
	if(data.get('current_waypoint')!=None):
		output.current_waypoint=data['current_waypoint']
	else:
		print("No value found for current_waypoint\n")
	if(data.get('trajectory_time')!=None):
		output.trajectory_time=data['trajectory_time']
	else:
		print("No value found for trajectory_time\n")
	return output

def yaml_loader_com_robotraconteur_robotics_trajectory_AdvancedJointTrajectoryDeviceWaypoint(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.robotics.trajectory.AdvancedJointTrajectoryDeviceWaypoint")
	if(data.get('joint_position')!=None):
		output.joint_position=numpy.zeros(len(data['joint_position']),dtype=numpy.double)
		for i in range(len(data['joint_position'])):
			output.joint_position[i]=data['joint_position'][i]
	if(data.get('joint_velocity')!=None):
		output.joint_velocity=numpy.zeros(len(data['joint_velocity']),dtype=numpy.double)
		for i in range(len(data['joint_velocity'])):
			output.joint_velocity[i]=data['joint_velocity'][i]
	if(data.get('joint_acceleration')!=None):
		output.joint_acceleration=numpy.zeros(len(data['joint_acceleration']),dtype=numpy.double)
		for i in range(len(data['joint_acceleration'])):
			output.joint_acceleration[i]=data['joint_acceleration'][i]
	if(data.get('joint_jerk')!=None):
		output.joint_jerk=numpy.zeros(len(data['joint_jerk']),dtype=numpy.double)
		for i in range(len(data['joint_jerk'])):
			output.joint_jerk[i]=data['joint_jerk'][i]
	if(data.get('joint_effort')!=None):
		output.joint_effort=numpy.zeros(len(data['joint_effort']),dtype=numpy.double)
		for i in range(len(data['joint_effort'])):
			output.joint_effort[i]=data['joint_effort'][i]
	if(data.get('position_tolerance')!=None):
		output.position_tolerance=numpy.zeros(len(data['position_tolerance']),dtype=numpy.double)
		for i in range(len(data['position_tolerance'])):
			output.position_tolerance[i]=data['position_tolerance'][i]
	if(data.get('velocity_tolerance')!=None):
		output.velocity_tolerance=numpy.zeros(len(data['velocity_tolerance']),dtype=numpy.double)
		for i in range(len(data['velocity_tolerance'])):
			output.velocity_tolerance[i]=data['velocity_tolerance'][i]
	return output

def yaml_loader_com_robotraconteur_robotics_trajectory_AdvancedJointTrajectoryWaypoint(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.robotics.trajectory.AdvancedJointTrajectoryWaypoint")
	if(data.get('joints')!=None):
		mylist=[]
		for i in range(len(data['joints'])):
			mylist.append(yaml_loader_com_robotraconteur_robotics_trajectory_AdvancedJointTrajectoryDeviceWaypoint(RRN,data['joints'][i]))
		output.joints=mylist
	if(data.get('time_from_start')!=None):
		output.time_from_start=data['time_from_start']
	else:
		print("No value found for time_from_start\n")
	return output

def yaml_loader_com_robotraconteur_robotics_trajectory_AdvancedJointTrajectoryDevice(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.robotics.trajectory.AdvancedJointTrajectoryDevice")
	if(data.get('device')!=None):
		output.device = YAMLconverter__com_robotraconteur_identifier.yaml_loader_com_robotraconteur_identifier_Identifier(RRN,data['device'])
	if(data.get('joint_names')!=None):
		mylist=[]
		for i in range(len(data['joint_names'])):
			mylist.append(data['joint_names'][i])
		output.joint_names=mylist
	if(data.get('joint_units')!=None):
		mylist=[]
		for i in range(len(data['joint_units'])):
			mylist.append(YAMLconverter__com_robotraconteur_robotics_joints.yaml_loader_com_robotraconteur_robotics_joints_JointPositionUnits(RRN,data['joint_units'][i]))
		output.joint_units=mylist
	if(data.get('joint_effort_units')!=None):
		mylist=[]
		for i in range(len(data['joint_effort_units'])):
			mylist.append(YAMLconverter__com_robotraconteur_robotics_joints.yaml_loader_com_robotraconteur_robotics_joints_JointEffortUnits(RRN,data['joint_effort_units'][i]))
		output.joint_effort_units=mylist
	if(data.get('interpolation_mode')!=None):
		output.interpolation_mode=python_enums.string_to_enum_InterpolationMode	return output

def yaml_loader_com_robotraconteur_robotics_trajectory_AdvancedJointTrajectory(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.robotics.trajectory.AdvancedJointTrajectory")
	if(data.get('devices')!=None):
		mylist=[]
		for i in range(len(data['devices'])):
			mylist.append(yaml_loader_com_robotraconteur_robotics_trajectory_AdvancedJointTrajectoryDevice(RRN,data['devices'][i]))
		output.devices=mylist
	if(data.get('waypoints')!=None):
		mylist=[]
		for i in range(len(data['waypoints'])):
			mylist.append(yaml_loader_com_robotraconteur_robotics_trajectory_AdvancedJointTrajectoryWaypoint(RRN,data['waypoints'][i]))
		output.waypoints=mylist
	return output

def yaml_loader_com_robotraconteur_robotics_trajectory_FreeformJointTrajectoryWaypoint(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.robotics.trajectory.FreeformJointTrajectoryWaypoint")
	if(data.get('interpolation_mode')!=None):
		output.interpolation_mode=data['interpolation_mode']
	else:
		print("No value found for interpolation_mode\n")
	if(data.get('time_from_start')!=None):
		output.time_from_start=data['time_from_start']
	else:
		print("No value found for time_from_start\n")
	return output

def yaml_loader_com_robotraconteur_robotics_trajectory_FreeformJointTrajectory(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.robotics.trajectory.FreeformJointTrajectory")
	if(data.get('joint_names')!=None):
		mylist=[]
		for i in range(len(data['joint_names'])):
			mylist.append(data['joint_names'][i])
		output.joint_names=mylist
	if(data.get('joint_units')!=None):
		mylist=[]
		for i in range(len(data['joint_units'])):
			mylist.append(data['joint_units'][i])
		output.joint_units=mylist
	if(data.get('waypoints')!=None):
		mylist=[]
		for i in range(len(data['waypoints'])):
			mylist.append(yaml_loader_com_robotraconteur_robotics_trajectory_FreeformJointTrajectoryWaypoint(RRN,data['waypoints'][i]))
		output.waypoints=mylist
	return output


