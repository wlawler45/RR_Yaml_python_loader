import yaml


import RobotRaconteur as RR
RRN=RR.RobotRaconteurNode.s
import numpy
import YAMLconverter__com_robotraconteur_imaging_camerainfo


def load_yaml_camera(data):
    camera1=data["device_info"]["point_cloud"]
    print(camera1)
    output=YAMLconverter__com_robotraconteur_pointcloud_sensor.yaml_loader_com_robotraconteur_pointcloud_sensor_PointCloudSensorInfo(RRN,camera1)
    print(output.device_info.serial_number)
    return output

def main():
    with RR.ServerNodeSetup("yaml_tester",2355) as node_setup:
        RRN.RegisterServiceTypeFromFile("com.robotraconteur.uuid")
        RRN.RegisterServiceTypeFromFile("com.robotraconteur.identifier")#
        RRN.RegisterServiceTypeFromFile("com.robotraconteur.datetime")
        RRN.RegisterServiceTypeFromFile("com.robotraconteur.resource")
        RRN.RegisterServiceTypeFromFile("com.robotraconteur.geometry")
        RRN.RegisterServiceTypeFromFile("com.robotraconteur.datatype")
        RRN.RegisterServiceTypeFromFile("com.robotraconteur.device")#
        RRN.RegisterServiceTypeFromFile("com.robotraconteur.param")
        RRN.RegisterServiceTypeFromFile("com.robotraconteur.datetime.clock")
        RRN.RegisterServiceTypeFromFile("com.robotraconteur.action")
        RRN.RegisterServiceTypeFromFile("com.robotraconteur.units")
        RRN.RegisterServiceTypeFromFile("com.robotraconteur.sensordata")
        RRN.RegisterServiceTypeFromFile("com.robotraconteur.sensor")#
        RRN.RegisterServiceTypeFromFile("com.robotraconteur.actuator")
        RRN.RegisterServiceTypeFromFile("com.robotraconteur.bignum")
        RRN.RegisterServiceTypeFromFile("com.robotraconteur.color")
        RRN.RegisterServiceTypeFromFile("com.robotraconteur.eventlog")
        RRN.RegisterServiceTypeFromFile("com.robotraconteur.geometry.shapes")
        RRN.RegisterServiceTypeFromFile("com.robotraconteur.geometryf")
        RRN.RegisterServiceTypeFromFile("com.robotraconteur.geometryi")
        RRN.RegisterServiceTypeFromFile("com.robotraconteur.gps")
        RRN.RegisterServiceTypeFromFile("com.robotraconteur.hid.joystick")
        RRN.RegisterServiceTypeFromFile("com.robotraconteur.image")
        RRN.RegisterServiceTypeFromFile("com.robotraconteur.imaging.camerainfo")
        RRN.RegisterServiceTypeFromFile("com.robotraconteur.imaging")
        RRN.RegisterServiceTypeFromFile("com.robotraconteur.imu")
        RRN.RegisterServiceTypeFromFile("com.robotraconteur.laserscan")
        RRN.RegisterServiceTypeFromFile("com.robotraconteur.laserscanner")
        RRN.RegisterServiceTypeFromFile("com.robotraconteur.lighting")
        RRN.RegisterServiceTypeFromFile("com.robotraconteur.octree")
        RRN.RegisterServiceTypeFromFile("com.robotraconteur.pid")
        RRN.RegisterServiceTypeFromFile("com.robotraconteur.pointcloud")
        RRN.RegisterServiceTypeFromFile("com.robotraconteur.pointcloud.sensor")
        RRN.RegisterServiceTypeFromFile("com.robotraconteur.robotics.joints")
        RRN.RegisterServiceTypeFromFile("com.robotraconteur.robotics.payload")
        RRN.RegisterServiceTypeFromFile("com.robotraconteur.signal")
        RRN.RegisterServiceTypeFromFile("com.robotraconteur.robotics.tool")
        RRN.RegisterServiceTypeFromFile("com.robotraconteur.robotics.trajectory")
        RRN.RegisterServiceTypeFromFile("com.robotraconteur.robotics.robot")
        RRN.RegisterServiceTypeFromFile("com.robotraconteur.robotics.planning")
        RRN.RegisterServiceTypeFromFile("com.robotraconteur.servo")
        
        
        
        
        yaml_file="KinectSensor.yaml"
        with open(yaml_file, "r") as fh:
            python_object = yaml.load(fh, Loader=yaml.SafeLoader)
            
        
        output=load_yaml_camera(python_object)
        #print(output)
    

if __name__ == "__main__":
	main()
