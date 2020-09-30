#!/usr/bin/env python
import yaml
import numpy
import python_enums
def yaml_loader_com_robotraconteur_bignum_BigNum(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.bignum.BigNum")
	if(data.get('data')!=None):
		output.data=numpy.zeros(len(data['data']),dtype=numpy.uint8)
		for i in range(len(data['data'])):
			output.data[i]=data['data'][i]
	return output

def yaml_loader_com_robotraconteur_bignum_UnsignedBigNum(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.bignum.UnsignedBigNum")
	if(data.get('data')!=None):
		output.data=numpy.zeros(len(data['data']),dtype=numpy.uint8)
		for i in range(len(data['data'])):
			output.data[i]=data['data'][i]
	return output

def yaml_loader_com_robotraconteur_bignum_BigFloat(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.bignum.BigFloat")
	if(data.get('num')!=None):
		output.num = yaml_loader_com_robotraconteur_bignum_BigNum(RRN,data['num'])
	if(data.get('den')!=None):
		output.den = yaml_loader_com_robotraconteur_bignum_BigNum(RRN,data['den'])
	if(data.get('radix')!=None):
		output.radix = yaml_loader_com_robotraconteur_bignum_BigNum(RRN,data['radix'])
	return output


