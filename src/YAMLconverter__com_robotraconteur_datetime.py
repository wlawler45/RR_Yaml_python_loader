#!/usr/bin/env python
import yaml
import numpy
import python_enums
import YAMLconverter__com_robotraconteur_uuid
def yaml_loader_com_robotraconteur_datetime_DateTimeLocal(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.datetime.DateTimeLocal")
	if(data.get('seconds')!=None):
		output.seconds=data['seconds']
	else:
		print("No value found for seconds\n")
	if(data.get('nanoseconds')!=None):
		output.nanoseconds=data['nanoseconds']
	else:
		print("No value found for nanoseconds\n")
	if(data.get('utc_offset_seconds')!=None):
		output.utc_offset_seconds=data['utc_offset_seconds']
	else:
		print("No value found for utc_offset_seconds\n")
	if(data.get('timezone_name')!=None):
		output.timezone_name=data['timezone_name']
	else:
		print("No value found for timezone_name\n")
	return output

#TODO: Fix the following structures or namedarrays: 
# com.robotraconteur.datetime.DateTimeLocal 

