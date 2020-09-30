#!/usr/bin/env python
import yaml
import numpy
import python_enums
import YAMLconverter__com_robotraconteur_device
import YAMLconverter__com_robotraconteur_sensordata
import YAMLconverter__com_robotraconteur_geometry
def yaml_loader_com_robotraconteur_hid_joystick_JoystickInfo(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.hid.joystick.JoystickInfo")
	if(data.get('device_info')!=None):
		output.device_info = YAMLconverter__com_robotraconteur_device.yaml_loader_com_robotraconteur_device_DeviceInfo(RRN,data['device_info'])
	if(data.get('axes_count')!=None):
		output.axes_count=data['axes_count']
	else:
		print("No value found for axes_count\n")
	if(data.get('button_count')!=None):
		output.button_count=data['button_count']
	else:
		print("No value found for button_count\n")
	if(data.get('joystick_capabilities')!=None):
		output.joystick_capabilities=data['joystick_capabilities']
	else:
		print("No value found for joystick_capabilities\n")
	return output

def yaml_loader_com_robotraconteur_hid_joystick_JoystickState(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.hid.joystick.JoystickState")
	if(data.get('axes')!=None):
		output.axes=numpy.zeros(len(data['axes']),dtype=numpy.single)
		for i in range(len(data['axes'])):
			output.axes[i]=data['axes'][i]
	if(data.get('buttons')!=None):
	output.buttons=numpy.zeros(len(data['buttons']),dtype=numpy.int32)
	for i in range(len(data['buttons'])):
		output.buttons[i]=data['buttons'][i]
	return output

def yaml_loader_com_robotraconteur_hid_joystick_JoystickStateSensorData(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.hid.joystick.JoystickStateSensorData")
	if(data.get('data_header')!=None):
		output.data_header = YAMLconverter__com_robotraconteur_sensordata.yaml_loader_com_robotraconteur_sensordata_SensorDataHeader(RRN,data['data_header'])
	if(data.get('joystick_state')!=None):
		output.joystick_state = yaml_loader_com_robotraconteur_hid_joystick_JoystickState(RRN,data['joystick_state'])
	return output


