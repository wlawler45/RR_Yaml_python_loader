#!/usr/bin/env python
import yaml
import numpy
import python_enums
import YAMLconverter__com_robotraconteur_sensordata
import YAMLconverter__com_robotraconteur_device
import YAMLconverter__com_robotraconteur_param
import YAMLconverter__com_robotraconteur_geometry
import YAMLconverter__com_robotraconteur_units
import YAMLconverter__com_robotraconteur_datatype
def yaml_loader_com_robotraconteur_sensor_SensorInfo(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.sensor.SensorInfo")
	if(data.get('device_info')!=None):
		output.device_info = YAMLconverter__com_robotraconteur_device.yaml_loader_com_robotraconteur_device_DeviceInfo(RRN,data['device_info'])
	if(data.get('sensor_type')!=None):
		output.sensor_type=python_enums.string_to_enum_SensorTypeCode	if(data.get('units')!=None):
		mylist=[]
		for i in range(len(data['units'])):
			mylist.append(YAMLconverter__com_robotraconteur_units.yaml_loader_com_robotraconteur_units_SIUnit(RRN,data['units'][i]))
		output.units=mylist
	if(data.get('data_type')!=None):
		output.data_type = YAMLconverter__com_robotraconteur_datatype.yaml_loader_com_robotraconteur_datatype_DataType(RRN,data['data_type'])
	if(data.get('sensor_resolution')!=None):
		output.sensor_resolution=numpy.zeros(len(data['sensor_resolution']),dtype=numpy.double)
		for i in range(len(data['sensor_resolution'])):
			output.sensor_resolution[i]=data['sensor_resolution'][i]
	if(data.get('analog_sensor')!=None):
		output.analog_sensor=data['analog_sensor']
	else:
		print("No value found for analog_sensor\n")
	if(data.get('update_frequency')!=None):
		output.update_frequency=data['update_frequency']
	else:
		print("No value found for update_frequency\n")
	return output

def yaml_loader_com_robotraconteur_sensor_SensorData(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.sensor.SensorData")
	if(data.get('data_header')!=None):
		output.data_header = YAMLconverter__com_robotraconteur_sensordata.yaml_loader_com_robotraconteur_sensordata_SensorDataHeader(RRN,data['data_header'])
	if(data.get('data')!=None):
		output.data=numpy.zeros(len(data['data']),dtype=numpy.double)
		for i in range(len(data['data'])):
			output.data[i]=data['data'][i]
	if(data.get('data_type')!=None):
		output.data_type = YAMLconverter__com_robotraconteur_datatype.yaml_loader_com_robotraconteur_datatype_DataType(RRN,data['data_type'])
	return output


