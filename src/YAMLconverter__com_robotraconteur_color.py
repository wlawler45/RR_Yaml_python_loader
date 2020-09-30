#!/usr/bin/env python
import yaml
import numpy
import python_enums
def yaml_loader_com_robotraconteur_color_ColorRGBA(RRN,data):
	output_type=RRN.GetNamedArrayDType("com.robotraconteur.color.ColorRGBA")
	output=numpy.zeros((1,),dtype=output_type)
	output[0]['r']=data['r']
	output[0]['g']=data['g']
	output[0]['b']=data['b']
	output[0]['a']=data['a']
	return output

def yaml_loader_com_robotraconteur_color_ColorRGBAf(RRN,data):
	output_type=RRN.GetNamedArrayDType("com.robotraconteur.color.ColorRGBAf")
	output=numpy.zeros((1,),dtype=output_type)
	output[0]['r']=data['r']
	output[0]['g']=data['g']
	output[0]['b']=data['b']
	output[0]['a']=data['a']
	return output

def yaml_loader_com_robotraconteur_color_ColorRGBAu(RRN,data):
	output_type=RRN.GetNamedArrayDType("com.robotraconteur.color.ColorRGBAu")
	output=numpy.zeros((1,),dtype=output_type)
	output[0]['r']=data['r']
	output[0]['g']=data['g']
	output[0]['b']=data['b']
	output[0]['a']=data['a']
	return output

def yaml_loader_com_robotraconteur_color_ColorRGBAh(RRN,data):
	output_type=RRN.GetNamedArrayDType("com.robotraconteur.color.ColorRGBAh")
	output=numpy.zeros((1,),dtype=output_type)
	output[0]['r']=data['r']
	output[0]['g']=data['g']
	output[0]['b']=data['b']
	output[0]['a']=data['a']
	return output


