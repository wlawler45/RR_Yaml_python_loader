#!/usr/bin/env python
import yaml
import numpy
import python_enums
import YAMLconverter__com_robotraconteur_sensordata
import YAMLconverter__com_robotraconteur_device
import YAMLconverter__com_robotraconteur_signal
import YAMLconverter__com_robotraconteur_param
import YAMLconverter__com_robotraconteur_robotics_joints
def yaml_loader_com_robotraconteur_servo_ServoInfo(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.servo.ServoInfo")
	if(data.get('device_info')!=None):
		output.device_info = YAMLconverter__com_robotraconteur_device.yaml_loader_com_robotraconteur_device_DeviceInfo(RRN,data['device_info'])
	if(data.get('servo_type')!=None):
		output.servo_type=python_enums.string_to_enum_ServoTypeCode	if(data.get('capabilities')!=None):
		output.capabilities=data['capabilities']
	else:
		print("No value found for capabilities\n")
	if(data.get('axis_count')!=None):
		output.axis_count=data['axis_count']
	else:
		print("No value found for axis_count\n")
	if(data.get('position_units')!=None):
		mylist=[]
		for i in range(len(data['position_units'])):
			mylist.append(YAMLconverter__com_robotraconteur_robotics_joints.yaml_loader_com_robotraconteur_robotics_joints_JointPositionUnits(RRN,data['position_units'][i]))
		output.position_units=mylist
	if(data.get('effort_units')!=None):
		mylist=[]
		for i in range(len(data['effort_units'])):
			mylist.append(YAMLconverter__com_robotraconteur_robotics_joints.yaml_loader_com_robotraconteur_robotics_joints_JointEffortUnits(RRN,data['effort_units'][i]))
		output.effort_units=mylist
	if(data.get('position_min')!=None):
		output.position_min=numpy.zeros(len(data['position_min']),dtype=numpy.double)
		for i in range(len(data['position_min'])):
			output.position_min[i]=data['position_min'][i]
	if(data.get('position_max')!=None):
		output.position_max=numpy.zeros(len(data['position_max']),dtype=numpy.double)
		for i in range(len(data['position_max'])):
			output.position_max[i]=data['position_max'][i]
	if(data.get('velocity_min')!=None):
		output.velocity_min=numpy.zeros(len(data['velocity_min']),dtype=numpy.double)
		for i in range(len(data['velocity_min'])):
			output.velocity_min[i]=data['velocity_min'][i]
	if(data.get('velocity_max')!=None):
		output.velocity_max=numpy.zeros(len(data['velocity_max']),dtype=numpy.double)
		for i in range(len(data['velocity_max'])):
			output.velocity_max[i]=data['velocity_max'][i]
	if(data.get('acceleration_min')!=None):
		output.acceleration_min=numpy.zeros(len(data['acceleration_min']),dtype=numpy.double)
		for i in range(len(data['acceleration_min'])):
			output.acceleration_min[i]=data['acceleration_min'][i]
	if(data.get('acceleration_max')!=None):
		output.acceleration_max=numpy.zeros(len(data['acceleration_max']),dtype=numpy.double)
		for i in range(len(data['acceleration_max'])):
			output.acceleration_max[i]=data['acceleration_max'][i]
	if(data.get('torque_min')!=None):
		output.torque_min=numpy.zeros(len(data['torque_min']),dtype=numpy.double)
		for i in range(len(data['torque_min'])):
			output.torque_min[i]=data['torque_min'][i]
	if(data.get('torque_max')!=None):
		output.torque_max=numpy.zeros(len(data['torque_max']),dtype=numpy.double)
		for i in range(len(data['torque_max'])):
			output.torque_max[i]=data['torque_max'][i]
	if(data.get('gear_ratio')!=None):
		output.gear_ratio=numpy.zeros(len(data['gear_ratio']),dtype=numpy.double)
		for i in range(len(data['gear_ratio'])):
			output.gear_ratio[i]=data['gear_ratio'][i]
	if(data.get('sensor_resolution')!=None):
		output.sensor_resolution=numpy.zeros(len(data['sensor_resolution']),dtype=numpy.double)
		for i in range(len(data['sensor_resolution'])):
			output.sensor_resolution[i]=data['sensor_resolution'][i]
	if(data.get('effort_command_resolution')!=None):
		output.effort_command_resolution=numpy.zeros(len(data['effort_command_resolution']),dtype=numpy.double)
		for i in range(len(data['effort_command_resolution'])):
			output.effort_command_resolution[i]=data['effort_command_resolution'][i]
	return output

def yaml_loader_com_robotraconteur_servo_ServoState(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.servo.ServoState")
	if(data.get('seqno')!=None):
		output.seqno=data['seqno']
	else:
		print("No value found for seqno\n")
	if(data.get('mode')!=None):
		output.mode=python_enums.string_to_enum_ServoMode	if(data.get('position')!=None):
		output.position=numpy.zeros(len(data['position']),dtype=numpy.double)
		for i in range(len(data['position'])):
			output.position[i]=data['position'][i]
	if(data.get('velocity')!=None):
		output.velocity=numpy.zeros(len(data['velocity']),dtype=numpy.double)
		for i in range(len(data['velocity'])):
			output.velocity[i]=data['velocity'][i]
	if(data.get('acceleration')!=None):
		output.acceleration=numpy.zeros(len(data['acceleration']),dtype=numpy.double)
		for i in range(len(data['acceleration'])):
			output.acceleration[i]=data['acceleration'][i]
	if(data.get('effort')!=None):
		output.effort=numpy.zeros(len(data['effort']),dtype=numpy.double)
		for i in range(len(data['effort'])):
			output.effort[i]=data['effort'][i]
	if(data.get('position_command')!=None):
		output.position_command=numpy.zeros(len(data['position_command']),dtype=numpy.double)
		for i in range(len(data['position_command'])):
			output.position_command[i]=data['position_command'][i]
	if(data.get('velocity_command')!=None):
		output.velocity_command=numpy.zeros(len(data['velocity_command']),dtype=numpy.double)
		for i in range(len(data['velocity_command'])):
			output.velocity_command[i]=data['velocity_command'][i]
	if(data.get('effort_command')!=None):
		output.effort_command=numpy.zeros(len(data['effort_command']),dtype=numpy.double)
		for i in range(len(data['effort_command'])):
			output.effort_command[i]=data['effort_command'][i]
	return output

def yaml_loader_com_robotraconteur_servo_ServoStateSensorData(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.servo.ServoStateSensorData")
	if(data.get('data_header')!=None):
		output.data_header = YAMLconverter__com_robotraconteur_sensordata.yaml_loader_com_robotraconteur_sensordata_SensorDataHeader(RRN,data['data_header'])
	if(data.get('servo_state')!=None):
		output.servo_state = yaml_loader_com_robotraconteur_servo_ServoState(RRN,data['servo_state'])
	return output

def yaml_loader_com_robotraconteur_servo_ServoCommand(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.servo.ServoCommand")
	if(data.get('seqno')!=None):
		output.seqno=data['seqno']
	else:
		print("No value found for seqno\n")
	if(data.get('status_seqno')!=None):
		output.status_seqno=data['status_seqno']
	else:
		print("No value found for status_seqno\n")
	if(data.get('command')!=None):
		output.command=numpy.zeros(len(data['command']),dtype=numpy.double)
		for i in range(len(data['command'])):
			output.command[i]=data['command'][i]
	return output


