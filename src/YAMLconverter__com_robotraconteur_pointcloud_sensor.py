#!/usr/bin/env python
import yaml
import numpy
import python_enums
import YAMLconverter__com_robotraconteur_device
import YAMLconverter__com_robotraconteur_param
import YAMLconverter__com_robotraconteur_pointcloud
import YAMLconverter__com_robotraconteur_geometry
import YAMLconverter__com_robotraconteur_sensor
def yaml_loader_com_robotraconteur_pointcloud_sensor_PointCloudSensorInfo(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.pointcloud.sensor.PointCloudSensorInfo")
	if(data.get('device_info')!=None):
		output.device_info = YAMLconverter__com_robotraconteur_device.yaml_loader_com_robotraconteur_device_DeviceInfo(RRN,data['device_info'])
	if(data.get('range_min')!=None):
		output.range_min = YAMLconverter__com_robotraconteur_geometry.yaml_loader_com_robotraconteur_geometry_Point(RRN,data['range_min'])
	if(data.get('range_max')!=None):
		output.range_max = YAMLconverter__com_robotraconteur_geometry.yaml_loader_com_robotraconteur_geometry_Point(RRN,data['range_max'])
	if(data.get('resolution')!=None):
		output.resolution = YAMLconverter__com_robotraconteur_geometry.yaml_loader_com_robotraconteur_geometry_Vector3(RRN,data['resolution'])
	if(data.get('update_rate')!=None):
		output.update_rate=data['update_rate']
	else:
		print("No value found for update_rate\n")
	return output

def yaml_loader_com_robotraconteur_pointcloud_sensor_PointCloudSensorData(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.pointcloud.sensor.PointCloudSensorData")
	if(data.get('sensor_data')!=None):
		output.sensor_data = YAMLconverter__com_robotraconteur_sensor.yaml_loader_com_robotraconteur_sensor_SensorData(RRN,data['sensor_data'])
	if(data.get('point_cloud')!=None):
		output.point_cloud = YAMLconverter__com_robotraconteur_pointcloudf.yaml_loader_com_robotraconteur_pointcloud_PointCloudf(RRN,data['point_cloud'])
	return output

def yaml_loader_com_robotraconteur_pointcloud_sensor_PointCloudPartSensorData(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.pointcloud.sensor.PointCloudPartSensorData")
	if(data.get('sensor_data')!=None):
		output.sensor_data = YAMLconverter__com_robotraconteur_sensor.yaml_loader_com_robotraconteur_sensor_SensorData(RRN,data['sensor_data'])
	if(data.get('point_cloud')!=None):
		output.point_cloud = YAMLconverter__com_robotraconteur_pointcloudf.yaml_loader_com_robotraconteur_pointcloud_PointCloudPartf(RRN,data['point_cloud'])
	return output

def yaml_loader_com_robotraconteur_pointcloud_sensor_PointCloud2SensorData(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.pointcloud.sensor.PointCloud2SensorData")
	if(data.get('sensor_data')!=None):
		output.sensor_data = YAMLconverter__com_robotraconteur_sensor.yaml_loader_com_robotraconteur_sensor_SensorData(RRN,data['sensor_data'])
	if(data.get('point_cloud')!=None):
		output.point_cloud = YAMLconverter__com_robotraconteur_pointcloudf.yaml_loader_com_robotraconteur_pointcloud_PointCloud2f(RRN,data['point_cloud'])
	return output

def yaml_loader_com_robotraconteur_pointcloud_sensor_PointCloud2PartSensorData(RRN,data):
	output=RRN.NewStructure("com.robotraconteur.pointcloud.sensor.PointCloud2PartSensorData")
	if(data.get('sensor_data')!=None):
		output.sensor_data = YAMLconverter__com_robotraconteur_sensor.yaml_loader_com_robotraconteur_sensor_SensorData(RRN,data['sensor_data'])
	if(data.get('point_cloud')!=None):
		output.point_cloud = YAMLconverter__com_robotraconteur_pointcloudf.yaml_loader_com_robotraconteur_pointcloud_PointCloud2Partf(RRN,data['point_cloud'])
	return output


