#!/usr/bin/env python
import yaml
import numpy
import python_enums
import YAMLconverter__com_robotraconteur_device
import YAMLconverter__com_robotraconteur_sensordata
import YAMLconverter__com_robotraconteur_geometry
import YAMLconverter__com_robotraconteur_uuid
import YAMLconverter__com_robotraconteur_device_isoch
def yaml_loader_com_robotraconteur_hid_joystick_JoystickInfo(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.hid.joystick.JoystickInfo")
	if(data.get('device_info')!=None):
		output.device_info = YAMLconverter__com_robotraconteur_device.yaml_loader_com_robotraconteur_device_DeviceInfo(RRN,data['device_info'])
	if(data.get('id')!=None):
		output.id=data['id']
	else:
		print("No value found for id\n")
	if(data.get('axes_count')!=None):
		output.axes_count=data['axes_count']
	else:
		print("No value found for axes_count\n")
	if(data.get('button_count')!=None):
		output.button_count=data['button_count']
	else:
		print("No value found for button_count\n")
	if(data.get('hat_count')!=None):
		output.hat_count=data['hat_count']
	else:
		print("No value found for hat_count\n")
	if(data.get('joystick_capabilities')!=None):
		output.joystick_capabilities=data['joystick_capabilities']
	else:
		print("No value found for joystick_capabilities\n")
	if(data.get('joystick_device_vendor')!=None):
		output.joystick_device_vendor=data['joystick_device_vendor']
	else:
		print("No value found for joystick_device_vendor\n")
	if(data.get('joystick_device_product')!=None):
		output.joystick_device_product=data['joystick_device_product']
	else:
		print("No value found for joystick_device_product\n")
	if(data.get('joystick_device_version')!=None):
		output.joystick_device_version=data['joystick_device_version']
	else:
		print("No value found for joystick_device_version\n")
	if(data.get('joystick_uuid')!=None):
		output.joystick_uuid = YAMLconverter__com_robotraconteur_uuid.yaml_loader_com_robotraconteur_uuid_UUID(RRN,data['joystick_uuid'])
	return output

def yaml_loader_com_robotraconteur_hid_joystick_JoystickState(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.hid.joystick.JoystickState")
	if(data.get('buttons')!=None):
		output.buttons=numpy.zeros(len(data['buttons']),dtype=numpy.uint8)
		for i in range(len(data['buttons'])):
			output.buttons[i]=data['buttons'][i]
	if(data.get('hats')!=None):
		output.hats=numpy.zeros(len(data['hats']),dtype=numpy.uint8)
		for i in range(len(data['hats'])):
			output.hats[i]=data['hats'][i]
	return output

def yaml_loader_com_robotraconteur_hid_joystick_GamepadState(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.hid.joystick.GamepadState")
	if(data.get('left_x')!=None):
		output.left_x=data['left_x']
	else:
		print("No value found for left_x\n")
	if(data.get('left_y')!=None):
		output.left_y=data['left_y']
	else:
		print("No value found for left_y\n")
	if(data.get('right_x')!=None):
		output.right_x=data['right_x']
	else:
		print("No value found for right_x\n")
	if(data.get('right_y')!=None):
		output.right_y=data['right_y']
	else:
		print("No value found for right_y\n")
	if(data.get('trigger_left')!=None):
		output.trigger_left=data['trigger_left']
	else:
		print("No value found for trigger_left\n")
	if(data.get('trigger_right')!=None):
		output.trigger_right=data['trigger_right']
	else:
		print("No value found for trigger_right\n")
	if(data.get('buttons')!=None):
		output.buttons=data['buttons']
	else:
		print("No value found for buttons\n")
	return output

def yaml_loader_com_robotraconteur_hid_joystick_JoystickStateSensorData(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.hid.joystick.JoystickStateSensorData")
	if(data.get('data_header')!=None):
		output.data_header = YAMLconverter__com_robotraconteur_sensordata.yaml_loader_com_robotraconteur_sensordata_SensorDataHeader(RRN,data['data_header'])
	if(data.get('joystick_state')!=None):
		output.joystick_state = yaml_loader_com_robotraconteur_hid_joystick_JoystickState(RRN,data['joystick_state'])
	if(data.get('gamepad_state')!=None):
		output.gamepad_state = yaml_loader_com_robotraconteur_hid_joystick_GamepadState(RRN,data['gamepad_state'])
	return output


