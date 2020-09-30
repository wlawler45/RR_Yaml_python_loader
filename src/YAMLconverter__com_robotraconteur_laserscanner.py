#!/usr/bin/env python
import yaml
import numpy
import python_enums
import YAMLconverter__com_robotraconteur_device
import YAMLconverter__com_robotraconteur_param
import YAMLconverter__com_robotraconteur_laserscan
def yaml_loader_com_robotraconteur_laserscanner_LaserScannerInfo(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.laserscanner.LaserScannerInfo")
	if(data.get('device_info')!=None):
		output.device_info = YAMLconverter__com_robotraconteur_device.yaml_loader_com_robotraconteur_device_DeviceInfo(RRN,data['device_info'])
	if(data.get('scanner_info')!=None):
		output.scanner_info = YAMLconverter__com_robotraconteur_laserscanf.yaml_loader_com_robotraconteur_laserscan_LaserScanInfof(RRN,data['scanner_info'])
	if(data.get('scan_rate')!=None):
		output.scan_rate=data['scan_rate']
	else:
		print("No value found for scan_rate\n")
	return output


