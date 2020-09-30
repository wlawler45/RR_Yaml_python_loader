#!/usr/bin/env python
import yaml
import numpy
import python_enums
import YAMLconverter__com_robotraconteur_image
import YAMLconverter__com_robotraconteur_sensordata
def yaml_loader_com_robotraconteur_laserscan_LaserScanInfo(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.laserscan.LaserScanInfo")
	if(data.get('data_header')!=None):
		output.data_header = YAMLconverter__com_robotraconteur_sensordata.yaml_loader_com_robotraconteur_sensordata_SensorDataHeader(RRN,data['data_header'])
	if(data.get('angle_min')!=None):
		output.angle_min=data['angle_min']
	else:
		print("No value found for angle_min\n")
	if(data.get('angle_max')!=None):
		output.angle_max=data['angle_max']
	else:
		print("No value found for angle_max\n")
	if(data.get('angle_increment')!=None):
		output.angle_increment=data['angle_increment']
	else:
		print("No value found for angle_increment\n")
	if(data.get('angle_count')!=None):
		output.angle_count=data['angle_count']
	else:
		print("No value found for angle_count\n")
	if(data.get('vertical_angle_min')!=None):
		output.vertical_angle_min=data['vertical_angle_min']
	else:
		print("No value found for vertical_angle_min\n")
	if(data.get('vertical_angle_max')!=None):
		output.vertical_angle_max=data['vertical_angle_max']
	else:
		print("No value found for vertical_angle_max\n")
	if(data.get('vertical_angle_increment')!=None):
		output.vertical_angle_increment=data['vertical_angle_increment']
	else:
		print("No value found for vertical_angle_increment\n")
	if(data.get('vertical_angle_count')!=None):
		output.vertical_angle_count=data['vertical_angle_count']
	else:
		print("No value found for vertical_angle_count\n")
	if(data.get('time_increment')!=None):
		output.time_increment=data['time_increment']
	else:
		print("No value found for time_increment\n")
	if(data.get('scan_time')!=None):
		output.scan_time=data['scan_time']
	else:
		print("No value found for scan_time\n")
	if(data.get('range_min')!=None):
		output.range_min=data['range_min']
	else:
		print("No value found for range_min\n")
	if(data.get('range_max')!=None):
		output.range_max=data['range_max']
	else:
		print("No value found for range_max\n")
	if(data.get('range_resolution')!=None):
		output.range_resolution=data['range_resolution']
	else:
		print("No value found for range_resolution\n")
	return output

def yaml_loader_com_robotraconteur_laserscan_LaserScan(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.laserscan.LaserScan")
	if(data.get('scan_info')!=None):
		output.scan_info = yaml_loader_com_robotraconteur_laserscan_LaserScanInfo(RRN,data['scan_info'])
	if(data.get('ranges')!=None):
		output.ranges=numpy.zeros(len(data['ranges']),dtype=numpy.double)
		for i in range(len(data['ranges'])):
			output.ranges[i]=data['ranges'][i]
	if(data.get('intensities')!=None):
		output.intensities=numpy.zeros(len(data['intensities']),dtype=numpy.double)
		for i in range(len(data['intensities'])):
			output.intensities[i]=data['intensities'][i]
	if(data.get('color')!=None):
		dtype=RRN.GetNamedArrayDType("com.robotraconteur.image.PixelRGB")
		myarray=numpy.zeros((len(data['color'],),dtype=dtype)
		for i in range(len(data['color'])):
			myarray[i] = YAMLconverter__com_robotraconteur_image.yaml_loader_com_robotraconteur_image_PixelRGB(RRN,data['color'][i])
		output.color=myarray
	if(data.get('fiducial')!=None):
	output.fiducial=numpy.zeros(len(data['fiducial']),dtype=numpy.int32)
	for i in range(len(data['fiducial'])):
		output.fiducial[i]=data['fiducial'][i]
	return output

def yaml_loader_com_robotraconteur_laserscan_LaserScanInfof(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.laserscan.LaserScanInfof")
	if(data.get('data_header')!=None):
		output.data_header = YAMLconverter__com_robotraconteur_sensordata.yaml_loader_com_robotraconteur_sensordata_SensorDataHeader(RRN,data['data_header'])
	if(data.get('angle_min')!=None):
		output.angle_min=data['angle_min']
	else:
		print("No value found for angle_min\n")
	if(data.get('angle_max')!=None):
		output.angle_max=data['angle_max']
	else:
		print("No value found for angle_max\n")
	if(data.get('angle_increment')!=None):
		output.angle_increment=data['angle_increment']
	else:
		print("No value found for angle_increment\n")
	if(data.get('angle_count')!=None):
		output.angle_count=data['angle_count']
	else:
		print("No value found for angle_count\n")
	if(data.get('vertical_angle_min')!=None):
		output.vertical_angle_min=data['vertical_angle_min']
	else:
		print("No value found for vertical_angle_min\n")
	if(data.get('vertical_angle_max')!=None):
		output.vertical_angle_max=data['vertical_angle_max']
	else:
		print("No value found for vertical_angle_max\n")
	if(data.get('vertical_angle_increment')!=None):
		output.vertical_angle_increment=data['vertical_angle_increment']
	else:
		print("No value found for vertical_angle_increment\n")
	if(data.get('vertical_angle_count')!=None):
		output.vertical_angle_count=data['vertical_angle_count']
	else:
		print("No value found for vertical_angle_count\n")
	if(data.get('time_increment')!=None):
		output.time_increment=data['time_increment']
	else:
		print("No value found for time_increment\n")
	if(data.get('scan_time')!=None):
		output.scan_time=data['scan_time']
	else:
		print("No value found for scan_time\n")
	if(data.get('range_min')!=None):
		output.range_min=data['range_min']
	else:
		print("No value found for range_min\n")
	if(data.get('range_max')!=None):
		output.range_max=data['range_max']
	else:
		print("No value found for range_max\n")
	if(data.get('range_resolution')!=None):
		output.range_resolution=data['range_resolution']
	else:
		print("No value found for range_resolution\n")
	return output

def yaml_loader_com_robotraconteur_laserscan_LaserScanf(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.laserscan.LaserScanf")
	if(data.get('scan_info')!=None):
		output.scan_info = yaml_loader_com_robotraconteur_laserscan_LaserScanInfof(RRN,data['scan_info'])
	if(data.get('ranges')!=None):
		output.ranges=numpy.zeros(len(data['ranges']),dtype=numpy.single)
		for i in range(len(data['ranges'])):
			output.ranges[i]=data['ranges'][i]
	if(data.get('intensities')!=None):
		output.intensities=numpy.zeros(len(data['intensities']),dtype=numpy.single)
		for i in range(len(data['intensities'])):
			output.intensities[i]=data['intensities'][i]
	if(data.get('color')!=None):
		dtype=RRN.GetNamedArrayDType("com.robotraconteur.image.PixelRGB")
		myarray=numpy.zeros((len(data['color'],),dtype=dtype)
		for i in range(len(data['color'])):
			myarray[i] = YAMLconverter__com_robotraconteur_image.yaml_loader_com_robotraconteur_image_PixelRGB(RRN,data['color'][i])
		output.color=myarray
	if(data.get('fiducial')!=None):
	output.fiducial=numpy.zeros(len(data['fiducial']),dtype=numpy.int32)
	for i in range(len(data['fiducial'])):
		output.fiducial[i]=data['fiducial'][i]
	return output

def yaml_loader_com_robotraconteur_laserscan_LaserScanPart(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.laserscan.LaserScanPart")
	if(data.get('scan_info')!=None):
		output.scan_info = yaml_loader_com_robotraconteur_laserscan_LaserScanInfo(RRN,data['scan_info'])
	if(data.get('data_offset')!=None):
		output.data_offset=data['data_offset']
	else:
		print("No value found for data_offset\n")
	if(data.get('data_total_len')!=None):
		output.data_total_len=data['data_total_len']
	else:
		print("No value found for data_total_len\n")
	if(data.get('ranges')!=None):
		output.ranges=numpy.zeros(len(data['ranges']),dtype=numpy.double)
		for i in range(len(data['ranges'])):
			output.ranges[i]=data['ranges'][i]
	if(data.get('intensities')!=None):
		output.intensities=numpy.zeros(len(data['intensities']),dtype=numpy.double)
		for i in range(len(data['intensities'])):
			output.intensities[i]=data['intensities'][i]
	if(data.get('color')!=None):
		dtype=RRN.GetNamedArrayDType("com.robotraconteur.image.PixelRGB")
		myarray=numpy.zeros((len(data['color'],),dtype=dtype)
		for i in range(len(data['color'])):
			myarray[i] = YAMLconverter__com_robotraconteur_image.yaml_loader_com_robotraconteur_image_PixelRGB(RRN,data['color'][i])
		output.color=myarray
	if(data.get('fiducial')!=None):
	output.fiducial=numpy.zeros(len(data['fiducial']),dtype=numpy.int32)
	for i in range(len(data['fiducial'])):
		output.fiducial[i]=data['fiducial'][i]
	return output

def yaml_loader_com_robotraconteur_laserscan_LaserScanPartf(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.laserscan.LaserScanPartf")
	if(data.get('scan_info')!=None):
		output.scan_info = yaml_loader_com_robotraconteur_laserscan_LaserScanInfof(RRN,data['scan_info'])
	if(data.get('data_offset')!=None):
		output.data_offset=data['data_offset']
	else:
		print("No value found for data_offset\n")
	if(data.get('data_total_len')!=None):
		output.data_total_len=data['data_total_len']
	else:
		print("No value found for data_total_len\n")
	if(data.get('ranges')!=None):
		output.ranges=numpy.zeros(len(data['ranges']),dtype=numpy.single)
		for i in range(len(data['ranges'])):
			output.ranges[i]=data['ranges'][i]
	if(data.get('intensities')!=None):
		output.intensities=numpy.zeros(len(data['intensities']),dtype=numpy.single)
		for i in range(len(data['intensities'])):
			output.intensities[i]=data['intensities'][i]
	if(data.get('color')!=None):
		dtype=RRN.GetNamedArrayDType("com.robotraconteur.image.PixelRGB")
		myarray=numpy.zeros((len(data['color'],),dtype=dtype)
		for i in range(len(data['color'])):
			myarray[i] = YAMLconverter__com_robotraconteur_image.yaml_loader_com_robotraconteur_image_PixelRGB(RRN,data['color'][i])
		output.color=myarray
	if(data.get('fiducial')!=None):
	output.fiducial=numpy.zeros(len(data['fiducial']),dtype=numpy.int32)
	for i in range(len(data['fiducial'])):
		output.fiducial[i]=data['fiducial'][i]
	return output


