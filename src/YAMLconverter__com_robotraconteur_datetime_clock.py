#!/usr/bin/env python
import yaml
import numpy
import python_enums
import YAMLconverter__com_robotraconteur_datetime
import YAMLconverter__com_robotraconteur_device
def yaml_loader_com_robotraconteur_datetime_clock_ClockDeviceInfo(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.datetime.clock.ClockDeviceInfo")
	if(data.get('device_info')!=None):
		output.device_info = YAMLconverter__com_robotraconteur_device.yaml_loader_com_robotraconteur_device_DeviceInfo(RRN,data['device_info'])
	return output


