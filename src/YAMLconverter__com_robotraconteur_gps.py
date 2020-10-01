#!/usr/bin/env python
import yaml
import numpy
import python_enums
import YAMLconverter__com_robotraconteur_sensor
import YAMLconverter__com_robotraconteur_device
def yaml_loader_com_robotraconteur_gps_GpsState(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.gps.GpsState")
	if(data.get('altitude')!=None):
		output.altitude=data['altitude']
	else:
		print("No value found for altitude\n")
	if(data.get('latitude_deg')!=None):
		output.latitude_deg=data['latitude_deg']
	else:
		print("No value found for latitude_deg\n")
	if(data.get('longitude_deg')!=None):
		output.longitude_deg=data['longitude_deg']
	else:
		print("No value found for longitude_deg\n")
	if(data.get('velocity_east')!=None):
		output.velocity_east=data['velocity_east']
	else:
		print("No value found for velocity_east\n")
	if(data.get('velocity_north')!=None):
		output.velocity_north=data['velocity_north']
	else:
		print("No value found for velocity_north\n")
	if(data.get('velocity_up')!=None):
		output.velocity_up=data['velocity_up']
	else:
		print("No value found for velocity_up\n")
	return output


