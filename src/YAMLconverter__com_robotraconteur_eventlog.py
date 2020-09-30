#!/usr/bin/env python
import yaml
import numpy
import python_enums
import YAMLconverter__com_robotraconteur_identifier
import YAMLconverter__com_robotraconteur_datetime
import YAMLconverter__com_robotraconteur_device
def yaml_loader_com_robotraconteur_eventlog_EventLogType(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.eventlog.EventLogType")
	if(data.get('event_category')!=None):
		output.event_category = YAMLconverter__com_robotraconteur_identifier.yaml_loader_com_robotraconteur_identifier_Identifier(RRN,data['event_category'])
	if(data.get('event_type')!=None):
		output.event_type=data['event_type']
	else:
		print("No value found for event_type\n")
	return output

def yaml_loader_com_robotraconteur_eventlog_EventLogMessageHeader(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.eventlog.EventLogMessageHeader")
	if(data.get('type')!=None):
		output.type = yaml_loader_com_robotraconteur_eventlog_EventLogType(RRN,data['type'])
	if(data.get('level')!=None):
		output.level=python_enums.string_to_enum_EventLogLevel	if(data.get('source_device')!=None):
		output.source_device = YAMLconverter__com_robotraconteur_identifier.yaml_loader_com_robotraconteur_identifier_Identifier(RRN,data['source_device'])
	if(data.get('source_component')!=None):
		output.source_component=data['source_component']
	else:
		print("No value found for source_component\n")
	if(data.get('message_number')!=None):
		output.message_number=data['message_number']
	else:
		print("No value found for message_number\n")
	return output

def yaml_loader_com_robotraconteur_eventlog_EventLogMessage(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.eventlog.EventLogMessage")
	if(data.get('header')!=None):
		output.header = yaml_loader_com_robotraconteur_eventlog_EventLogMessageHeader(RRN,data['header'])
	if(data.get('title')!=None):
		output.title=data['title']
	else:
		print("No value found for title\n")
	if(data.get('message')!=None):
		output.message=data['message']
	else:
		print("No value found for message\n")
	return output


