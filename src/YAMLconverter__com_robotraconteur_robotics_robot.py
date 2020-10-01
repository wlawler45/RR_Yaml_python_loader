#!/usr/bin/env python
import yaml
import numpy
import python_enums
import YAMLconverter__com_robotraconteur_geometry
import YAMLconverter__com_robotraconteur_sensordata
import YAMLconverter__com_robotraconteur_device
import YAMLconverter__com_robotraconteur_signal
import YAMLconverter__com_robotraconteur_param
import YAMLconverter__com_robotraconteur_robotics_joints
import YAMLconverter__com_robotraconteur_robotics_tool
import YAMLconverter__com_robotraconteur_robotics_payload
import YAMLconverter__com_robotraconteur_robotics_trajectory
import YAMLconverter__com_robotraconteur_identifier
import YAMLconverter__com_robotraconteur_action
import YAMLconverter__com_robotraconteur_eventlog
import YAMLconverter__com_robotraconteur_device_isoch
def yaml_loader_com_robotraconteur_robotics_robot_RobotKinChainInfo(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.robotics.robot.RobotKinChainInfo")
	if(data.get('kin_chain_identifier')!=None):
		output.kin_chain_identifier = YAMLconverter__com_robotraconteur_identifier.yaml_loader_com_robotraconteur_identifier_Identifier(RRN,data['kin_chain_identifier'])
	if(data.get('H')!=None):
		dtype=RRN.GetNamedArrayDType("com.robotraconteur.geometry.Vector3")
		myarray=numpy.zeros((len(data['H'],),dtype=dtype)
		for i in range(len(data['H'])):
			myarray[i] = YAMLconverter__com_robotraconteur_geometry.yaml_loader_com_robotraconteur_geometry_Vector3(RRN,data['H'][i])
		output.H=myarray
	if(data.get('P')!=None):
		dtype=RRN.GetNamedArrayDType("com.robotraconteur.geometry.Vector3")
		myarray=numpy.zeros((len(data['P'],),dtype=dtype)
		for i in range(len(data['P'])):
			myarray[i] = YAMLconverter__com_robotraconteur_geometry.yaml_loader_com_robotraconteur_geometry_Vector3(RRN,data['P'][i])
		output.P=myarray
	if(data.get('link_inertias')!=None):
		dtype=RRN.GetNamedArrayDType("com.robotraconteur.geometry.SpatialInertia")
		myarray=numpy.zeros((len(data['link_inertias'],),dtype=dtype)
		for i in range(len(data['link_inertias'])):
			myarray[i] = YAMLconverter__com_robotraconteur_geometry.yaml_loader_com_robotraconteur_geometry_SpatialInertia(RRN,data['link_inertias'][i])
		output.link_inertias=myarray
	if(data.get('link_identifiers')!=None):
		mylist=[]
		for i in range(len(data['link_identifiers'])):
			mylist.append(YAMLconverter__com_robotraconteur_identifier.yaml_loader_com_robotraconteur_identifier_Identifier(RRN,data['link_identifiers'][i]))
		output.link_identifiers=mylist
	if(data.get('joint_numbers')!=None):
		output.joint_numbers=numpy.zeros(len(data['joint_numbers']),dtype=numpy.uint32)
		for i in range(len(data['joint_numbers'])):
			output.joint_numbers[i]=data['joint_numbers'][i]
	if(data.get('flange_pose')!=None):
		output.flange_pose = YAMLconverter__com_robotraconteur_geometry.yaml_loader_com_robotraconteur_geometry_Pose(RRN,data['flange_pose'])
	if(data.get('flange_identifier')!=None):
		output.flange_identifier = YAMLconverter__com_robotraconteur_identifier.yaml_loader_com_robotraconteur_identifier_Identifier(RRN,data['flange_identifier'])
	if(data.get('current_tool')!=None):
		output.current_tool = YAMLconverter__com_robotraconteur_robotics_tool.yaml_loader_com_robotraconteur_robotics_tool_ToolInfo(RRN,data['current_tool'])
	if(data.get('current_payload')!=None):
		output.current_payload = YAMLconverter__com_robotraconteur_robotics_payload.yaml_loader_com_robotraconteur_robotics_payload_PayloadInfo(RRN,data['current_payload'])
	if(data.get('tcp_max_velocity')!=None):
		output.tcp_max_velocity = YAMLconverter__com_robotraconteur_geometry.yaml_loader_com_robotraconteur_geometry_SpatialVelocity(RRN,data['tcp_max_velocity'])
	if(data.get('tcp_max_acceleration')!=None):
		output.tcp_max_acceleration = YAMLconverter__com_robotraconteur_geometry.yaml_loader_com_robotraconteur_geometry_SpatialAcceleration(RRN,data['tcp_max_acceleration'])
	if(data.get('tcp_reduced_max_velocity')!=None):
		output.tcp_reduced_max_velocity = YAMLconverter__com_robotraconteur_geometry.yaml_loader_com_robotraconteur_geometry_SpatialVelocity(RRN,data['tcp_reduced_max_velocity'])
	if(data.get('tcp_reduced_max_acceleration')!=None):
		output.tcp_reduced_max_acceleration = YAMLconverter__com_robotraconteur_geometry.yaml_loader_com_robotraconteur_geometry_SpatialAcceleration(RRN,data['tcp_reduced_max_acceleration'])
	if(data.get('description')!=None):
		output.description=data['description']
	else:
		print("No value found for description\n")
	return output

def yaml_loader_com_robotraconteur_robotics_robot_RobotInfo(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.robotics.robot.RobotInfo")
	if(data.get('device_info')!=None):
		output.device_info = YAMLconverter__com_robotraconteur_device.yaml_loader_com_robotraconteur_device_DeviceInfo(RRN,data['device_info'])
	if(data.get('robot_type')!=None):
		output.robot_type=python_enums.string_to_enum_RobotTypeCode	if(data.get('joint_info')!=None):
		mylist=[]
		for i in range(len(data['joint_info'])):
			mylist.append(YAMLconverter__com_robotraconteur_robotics_joints.yaml_loader_com_robotraconteur_robotics_joints_JointInfo(RRN,data['joint_info'][i]))
		output.joint_info=mylist
	if(data.get('chains')!=None):
		mylist=[]
		for i in range(len(data['chains'])):
			mylist.append(yaml_loader_com_robotraconteur_robotics_robot_RobotKinChainInfo(RRN,data['chains'][i]))
		output.chains=mylist
	if(data.get('robot_capabilities')!=None):
		output.robot_capabilities=data['robot_capabilities']
	else:
		print("No value found for robot_capabilities\n")
	if(data.get('signal_info')!=None):
		mylist=[]
		for i in range(len(data['signal_info'])):
			mylist.append(YAMLconverter__com_robotraconteur_signal.yaml_loader_com_robotraconteur_signal_SignalInfo(RRN,data['signal_info'][i]))
		output.signal_info=mylist
	if(data.get('parameter_info')!=None):
		mylist=[]
		for i in range(len(data['parameter_info'])):
			mylist.append(YAMLconverter__com_robotraconteur_param.yaml_loader_com_robotraconteur_param_ParameterInfo(RRN,data['parameter_info'][i]))
		output.parameter_info=mylist
	if(data.get('config_seqno')!=None):
		output.config_seqno=data['config_seqno']
	else:
		print("No value found for config_seqno\n")
	if(data.get('trajectory_interpolation_modes')!=None):
		mylist=[]
		for i in range(len(data['trajectory_interpolation_modes'])):
			mylist.append(YAMLconverter__com_robotraconteur_robotics_trajectory.yaml_loader_com_robotraconteur_robotics_trajectory_InterpolationMode(RRN,data['trajectory_interpolation_modes'][i]))
		output.trajectory_interpolation_modes=mylist
	return output

def yaml_loader_com_robotraconteur_robotics_robot_RobotState(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.robotics.robot.RobotState")
	if(data.get('seqno')!=None):
		output.seqno=data['seqno']
	else:
		print("No value found for seqno\n")
	if(data.get('command_mode')!=None):
		output.command_mode=python_enums.string_to_enum_RobotCommandMode	if(data.get('operational_mode')!=None):
		output.operational_mode=python_enums.string_to_enum_RobotOperationalMode	if(data.get('controller_state')!=None):
		output.controller_state=python_enums.string_to_enum_RobotControllerState	if(data.get('robot_state_flags')!=None):
		output.robot_state_flags=data['robot_state_flags']
	else:
		print("No value found for robot_state_flags\n")
	if(data.get('joint_position')!=None):
		output.joint_position=numpy.zeros(len(data['joint_position']),dtype=numpy.double)
		for i in range(len(data['joint_position'])):
			output.joint_position[i]=data['joint_position'][i]
	if(data.get('joint_velocity')!=None):
		output.joint_velocity=numpy.zeros(len(data['joint_velocity']),dtype=numpy.double)
		for i in range(len(data['joint_velocity'])):
			output.joint_velocity[i]=data['joint_velocity'][i]
	if(data.get('joint_effort')!=None):
		output.joint_effort=numpy.zeros(len(data['joint_effort']),dtype=numpy.double)
		for i in range(len(data['joint_effort'])):
			output.joint_effort[i]=data['joint_effort'][i]
	if(data.get('joint_position_command')!=None):
		output.joint_position_command=numpy.zeros(len(data['joint_position_command']),dtype=numpy.double)
		for i in range(len(data['joint_position_command'])):
			output.joint_position_command[i]=data['joint_position_command'][i]
	if(data.get('joint_velocity_command')!=None):
		output.joint_velocity_command=numpy.zeros(len(data['joint_velocity_command']),dtype=numpy.double)
		for i in range(len(data['joint_velocity_command'])):
			output.joint_velocity_command[i]=data['joint_velocity_command'][i]
	if(data.get('kin_chain_tcp')!=None):
		dtype=RRN.GetNamedArrayDType("com.robotraconteur.geometry.Pose")
		myarray=numpy.zeros((len(data['kin_chain_tcp'],),dtype=dtype)
		for i in range(len(data['kin_chain_tcp'])):
			myarray[i] = YAMLconverter__com_robotraconteur_geometry.yaml_loader_com_robotraconteur_geometry_Pose(RRN,data['kin_chain_tcp'][i])
		output.kin_chain_tcp=myarray
	if(data.get('kin_chain_tcp_vel')!=None):
		dtype=RRN.GetNamedArrayDType("com.robotraconteur.geometry.SpatialVelocity")
		myarray=numpy.zeros((len(data['kin_chain_tcp_vel'],),dtype=dtype)
		for i in range(len(data['kin_chain_tcp_vel'])):
			myarray[i] = YAMLconverter__com_robotraconteur_geometry.yaml_loader_com_robotraconteur_geometry_SpatialVelocity(RRN,data['kin_chain_tcp_vel'][i])
		output.kin_chain_tcp_vel=myarray
	if(data.get('trajectory_running')!=None):
		output.trajectory_running=data['trajectory_running']
	else:
		print("No value found for trajectory_running\n")
	return output

def yaml_loader_com_robotraconteur_robotics_robot_AdvancedRobotState(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.robotics.robot.AdvancedRobotState")
	if(data.get('seqno')!=None):
		output.seqno=data['seqno']
	else:
		print("No value found for seqno\n")
	if(data.get('command_mode')!=None):
		output.command_mode=python_enums.string_to_enum_RobotCommandMode	if(data.get('operational_mode')!=None):
		output.operational_mode=python_enums.string_to_enum_RobotOperationalMode	if(data.get('controller_state')!=None):
		output.controller_state=python_enums.string_to_enum_RobotControllerState	if(data.get('robot_state_flags')!=None):
		output.robot_state_flags=data['robot_state_flags']
	else:
		print("No value found for robot_state_flags\n")
	if(data.get('joint_position')!=None):
		output.joint_position=numpy.zeros(len(data['joint_position']),dtype=numpy.double)
		for i in range(len(data['joint_position'])):
			output.joint_position[i]=data['joint_position'][i]
	if(data.get('joint_velocity')!=None):
		output.joint_velocity=numpy.zeros(len(data['joint_velocity']),dtype=numpy.double)
		for i in range(len(data['joint_velocity'])):
			output.joint_velocity[i]=data['joint_velocity'][i]
	if(data.get('joint_effort')!=None):
		output.joint_effort=numpy.zeros(len(data['joint_effort']),dtype=numpy.double)
		for i in range(len(data['joint_effort'])):
			output.joint_effort[i]=data['joint_effort'][i]
	if(data.get('joint_position_command')!=None):
		output.joint_position_command=numpy.zeros(len(data['joint_position_command']),dtype=numpy.double)
		for i in range(len(data['joint_position_command'])):
			output.joint_position_command[i]=data['joint_position_command'][i]
	if(data.get('joint_velocity_command')!=None):
		output.joint_velocity_command=numpy.zeros(len(data['joint_velocity_command']),dtype=numpy.double)
		for i in range(len(data['joint_velocity_command'])):
			output.joint_velocity_command[i]=data['joint_velocity_command'][i]
	if(data.get('joint_position_units')!=None):
		output.joint_position_units=numpy.zeros(len(data['joint_position_units']),dtype=numpy.uint8)
		for i in range(len(data['joint_position_units'])):
			output.joint_position_units[i]=data['joint_position_units'][i]
	if(data.get('joint_effort_units')!=None):
		output.joint_effort_units=numpy.zeros(len(data['joint_effort_units']),dtype=numpy.uint8)
		for i in range(len(data['joint_effort_units'])):
			output.joint_effort_units[i]=data['joint_effort_units'][i]
	if(data.get('kin_chain_tcp')!=None):
		dtype=RRN.GetNamedArrayDType("com.robotraconteur.geometry.Pose")
		myarray=numpy.zeros((len(data['kin_chain_tcp'],),dtype=dtype)
		for i in range(len(data['kin_chain_tcp'])):
			myarray[i] = YAMLconverter__com_robotraconteur_geometry.yaml_loader_com_robotraconteur_geometry_Pose(RRN,data['kin_chain_tcp'][i])
		output.kin_chain_tcp=myarray
	if(data.get('kin_chain_tcp_vel')!=None):
		dtype=RRN.GetNamedArrayDType("com.robotraconteur.geometry.SpatialVelocity")
		myarray=numpy.zeros((len(data['kin_chain_tcp_vel'],),dtype=dtype)
		for i in range(len(data['kin_chain_tcp_vel'])):
			myarray[i] = YAMLconverter__com_robotraconteur_geometry.yaml_loader_com_robotraconteur_geometry_SpatialVelocity(RRN,data['kin_chain_tcp_vel'][i])
		output.kin_chain_tcp_vel=myarray
	if(data.get('trajectory_running')!=None):
		output.trajectory_running=data['trajectory_running']
	else:
		print("No value found for trajectory_running\n")
	if(data.get('trajectory_time')!=None):
		output.trajectory_time=data['trajectory_time']
	else:
		print("No value found for trajectory_time\n")
	if(data.get('trajectory_max_time')!=None):
		output.trajectory_max_time=data['trajectory_max_time']
	else:
		print("No value found for trajectory_max_time\n")
	if(data.get('trajectory_current_waypoint')!=None):
		output.trajectory_current_waypoint=data['trajectory_current_waypoint']
	else:
		print("No value found for trajectory_current_waypoint\n")
	if(data.get('config_seqno')!=None):
		output.config_seqno=data['config_seqno']
	else:
		print("No value found for config_seqno\n")
	return output

def yaml_loader_com_robotraconteur_robotics_robot_RobotStateSensorData(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.robotics.robot.RobotStateSensorData")
	if(data.get('data_header')!=None):
		output.data_header = YAMLconverter__com_robotraconteur_sensordata.yaml_loader_com_robotraconteur_sensordata_SensorDataHeader(RRN,data['data_header'])
	if(data.get('robot_state')!=None):
		output.robot_state = yaml_loader_com_robotraconteur_robotics_robot_AdvancedRobotState(RRN,data['robot_state'])
	return output

def yaml_loader_com_robotraconteur_robotics_robot_RobotJointCommand(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.robotics.robot.RobotJointCommand")
	if(data.get('seqno')!=None):
		output.seqno=data['seqno']
	else:
		print("No value found for seqno\n")
	if(data.get('state_seqno')!=None):
		output.state_seqno=data['state_seqno']
	else:
		print("No value found for state_seqno\n")
	if(data.get('command')!=None):
		output.command=numpy.zeros(len(data['command']),dtype=numpy.double)
		for i in range(len(data['command'])):
			output.command[i]=data['command'][i]
	if(data.get('units')!=None):
		output.units=numpy.zeros(len(data['units']),dtype=numpy.uint8)
		for i in range(len(data['units'])):
			output.units[i]=data['units'][i]
	return output


