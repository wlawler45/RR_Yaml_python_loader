#!/usr/bin/env python
import yaml
import numpy
import python_enums
def yaml_loader_com_robotraconteur_uuid_UUID(RRN,data):
	output_type=RRN.GetNamedArrayDType("com.robotraconteur.uuid.UUID")
	output=numpy.zeros((1,),dtype=output_type)
	#uuid_list=list(data['uuid_bytes'])
	#uuid=numpy.array(uuid_list,dtype=numpy.uint8)
	#output[0]['uuid_bytes']=uuid
	return output


