#!/usr/bin/env python
import yaml
import numpy
import python_enums
def yaml_loader_com_robotraconteur_pid_PIDParam(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.pid.PIDParam")
	if(data.get('p')!=None):
		output.p=data['p']
	else:
		print("No value found for p\n")
	if(data.get('i')!=None):
		output.i=data['i']
	else:
		print("No value found for i\n")
	if(data.get('d')!=None):
		output.d=data['d']
	else:
		print("No value found for d\n")
	if(data.get('imax')!=None):
		output.imax=data['imax']
	else:
		print("No value found for imax\n")
	if(data.get('imin')!=None):
		output.imin=data['imin']
	else:
		print("No value found for imin\n")
	if(data.get('cmdMax')!=None):
		output.cmdMax=data['cmdMax']
	else:
		print("No value found for cmdMax\n")
	if(data.get('cmdMin')!=None):
		output.cmdMin=data['cmdMin']
	else:
		print("No value found for cmdMin\n")
	return output


