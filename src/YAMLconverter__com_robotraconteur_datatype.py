#!/usr/bin/env python
import yaml
import numpy
import python_enums
def yaml_loader_com_robotraconteur_datatype_DataType(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.datatype.DataType")
	if(data.get('name')!=None):
		output.name=data['name']
	else:
		print("No value found for name\n")
	if(data.get('type_code')!=None):
		output.type_code=python_enums.string_to_enum_DataTypeCode	if(data.get('type_string')!=None):
		output.type_string=data['type_string']
	else:
		print("No value found for type_string\n")
	if(data.get('array_type_code')!=None):
		output.array_type_code=python_enums.string_to_enum_ArrayTypeCode	if(data.get('array_var_len')!=None):
		output.array_var_len=data['array_var_len']
	else:
		print("No value found for array_var_len\n")
	if(data.get('array_len')!=None):
		output.array_len=numpy.zeros(len(data['array_len']),dtype=numpy.uint32)
		for i in range(len(data['array_len'])):
			output.array_len[i]=data['array_len'][i]
	if(data.get('container_type_code')!=None):
		output.container_type_code=python_enums.string_to_enum_ContainerTypeCode	return output


