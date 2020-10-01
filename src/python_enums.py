#!/usr/bin/env python

def string_to_enum_ActionStatusCode(enumval):
	if(enumval=="error"): return -3
	if(enumval=="failed"): return -2
	if(enumval=="cancelled"): return -1
	if(enumval=="unknown"): return 0
	if(enumval=="queued"): return 1
	if(enumval=="running"): return 2
	if(enumval=="complete"): return 3

def string_to_enum_ActuatorTypeCode(enumval):
	if(enumval=="unknown"): return 0
	if(enumval=="generic"): return 1
	if(enumval=="motor_torque"): return 2
	if(enumval=="motor_force"): return 3
	if(enumval=="motor_velocity"): return 4
	if(enumval=="solenoid"): return 5
	if(enumval=="voice_coil"): return 6
	if(enumval=="piezoelectric"): return 7
	if(enumval=="pneumatic_pressure"): return 8
	if(enumval=="vacuum_pressure"): return 9
	if(enumval=="heater_power"): return 10
	if(enumval=="chiller_power"): return 11
	if(enumval=="valve"): return 12

def string_to_enum_ActuatorMode(enumval):
	if(enumval=="error"): return -2
	if(enumval=="disabled"): return -1
	if(enumval=="halt"): return 0
	if(enumval=="reduced_performance"): return 1
	if(enumval=="normal"): return 2

def string_to_enum_DataTypeCode(enumval):
	if(enumval=="void_c"): return 0
	if(enumval=="double_c"): return 1
	if(enumval=="single_c"): return 2
	if(enumval=="int8_c"): return 3
	if(enumval=="uint8_c"): return 4
	if(enumval=="int16_c"): return 5
	if(enumval=="uint16_c"): return 6
	if(enumval=="int32_c"): return 7
	if(enumval=="uint32_c"): return 8
	if(enumval=="int64_c"): return 9
	if(enumval=="uint64_c"): return 10
	if(enumval=="string_c"): return 11
	if(enumval=="cdouble_c"): return 12
	if(enumval=="csingle_c"): return 13
	if(enumval=="bool_c"): return 14
	if(enumval=="structure_c"): return 101
	if(enumval=="vector_c"): return 102
	if(enumval=="dictionary_c"): return 103
	if(enumval=="object_c"): return 104
	if(enumval=="varvalue_c"): return 105
	if(enumval=="varobject_c"): return 106
	if(enumval=="list_c"): return 108
	if(enumval=="pod_c"): return 109
	if(enumval=="pod_array_c"): return 110
	if(enumval=="pod_multidimarray_c"): return 111
	if(enumval=="enum_c"): return 112
	if(enumval=="namedtype_c"): return 113
	if(enumval=="namedarray_c"): return 114
	if(enumval=="namedarray_array_c"): return 115
	if(enumval=="namedarray_multidimarray_c"): return 116
	if(enumval=="multidimarray_c"): return 117

def string_to_enum_ArrayTypeCode(enumval):
	if(enumval=="none_c"): return 0
	if(enumval=="array_c"): return 1
	if(enumval=="multidimarray_c"): return 2

def string_to_enum_ContainerTypeCode(enumval):
	if(enumval=="none_c"): return 0
	if(enumval=="list_c"): return 1
	if(enumval=="map_int32_c"): return 2
	if(enumval=="map_string_c"): return 3
	if(enumval=="generator_c"): return 4

def string_to_enum_ClockTypeCode(enumval):
	if(enumval=="unknown"): return 0
	if(enumval=="default"): return 1
	if(enumval=="system_rtc_clock"): return 2
	if(enumval=="system_ntp_clock"): return 3
	if(enumval=="system_ptp_clock"): return 4
	if(enumval=="system_other_clock"): return 5
	if(enumval=="sim_clock_realtime"): return 6
	if(enumval=="sim_clock_scaled"): return 7
	if(enumval=="aux_0"): return 4096
	if(enumval=="aux_1"): return 4097
	if(enumval=="aux_2"): return 4098
	if(enumval=="aux_3"): return 4099
	if(enumval=="aux_4"): return 4100
	if(enumval=="aux_5"): return 4101
	if(enumval=="aux_6"): return 4102
	if(enumval=="aux_7"): return 4103

def string_to_enum_EventLogLevel(enumval):
	if(enumval=="undefined"): return 0
	if(enumval=="trace"): return 1
	if(enumval=="debug"): return 2
	if(enumval=="info"): return 3
	if(enumval=="warning"): return 4
	if(enumval=="error"): return 5
	if(enumval=="safety_violation_error"): return 6
	if(enumval=="fatal_error"): return 7
	if(enumval=="emergency_error"): return 8
	if(enumval=="catastrophic_error"): return 9

def string_to_enum_MeshType(enumval):
	if(enumval=="mesh"): return 0
	if(enumval=="convex_mesh"): return 1
	if(enumval=="sdf_mesh"): return 2

def string_to_enum_JoystickCapabilities(enumval):
	if(enumval=="none"): return 0
	if(enumval=="rumble"): return 1
	if(enumval=="force_feedback"): return 2
	if(enumval=="standard_gamepad"): return 4

def string_to_enum_GamepadButtons(enumval):
	if(enumval=="button_A"): return 0
	if(enumval=="button_B"): return 1
	if(enumval=="button_X"): return 2
	if(enumval=="button_Y"): return 3
	if(enumval=="button_back"): return 4
	if(enumval=="button_guide"): return 5
	if(enumval=="button_start"): return 6
	if(enumval=="button_left_stick"): return 7
	if(enumval=="button_right_stick"): return 8
	if(enumval=="button_left_shoulder"): return 9
	if(enumval=="button_right_shoulder"): return 10
	if(enumval=="button_dpad_up"): return 11
	if(enumval=="button_dpad_down"): return 12
	if(enumval=="button_dpad_left"): return 13
	if(enumval=="button_dpad_right"): return 14

def string_to_enum_JoystickHatState(enumval):
	if(enumval=="hat_centered"): return 0
	if(enumval=="hat_up"): return 1
	if(enumval=="hat_right"): return 2
	if(enumval=="hat_down"): return 4
	if(enumval=="hat_left"): return 8
	if(enumval=="hat_rightup"): return 3
	if(enumval=="hat_rightdown"): return 6
	if(enumval=="hat_leftup"): return 9
	if(enumval=="hat_leftdown"): return 12

def string_to_enum_ImageEncoding(enumval):
	if(enumval=="unknown"): return 0
	if(enumval=="rgb8"): return 4096
	if(enumval=="rgba8"): return 4097
	if(enumval=="bgr8"): return 4098
	if(enumval=="bgra8"): return 4099
	if(enumval=="rgbe8"): return 4100
	if(enumval=="bgre8"): return 4101
	if(enumval=="rgbm8"): return 4102
	if(enumval=="bgrm8"): return 4103
	if(enumval=="rgba16"): return 4104
	if(enumval=="bgra16"): return 4105
	if(enumval=="mono8"): return 8192
	if(enumval=="mono16"): return 8193
	if(enumval=="mono32"): return 8194
	if(enumval=="monof32"): return 8195
	if(enumval=="monof64"): return 8196
	if(enumval=="bayer_rggb8"): return 12288
	if(enumval=="bayer_bggr8"): return 12289
	if(enumval=="bayer_gbrg8"): return 12290
	if(enumval=="bayer_grbg8"): return 12291
	if(enumval=="depth_u16"): return 16384
	if(enumval=="depth_u32"): return 16385
	if(enumval=="depth_i64"): return 16386
	if(enumval=="depth_f32"): return 16387
	if(enumval=="depth_f64"): return 16388
	if(enumval=="freeform"): return 20480
	if(enumval=="compressed"): return 24576

def string_to_enum_TriggerMode(enumval):
	if(enumval=="unknown"): return 0
	if(enumval=="software"): return 1
	if(enumval=="continuous"): return 2
	if(enumval=="external"): return 3
	if(enumval=="aux1"): return 4
	if(enumval=="aux2"): return 5
	if(enumval=="aux3"): return 6
	if(enumval=="aux4"): return 7

def string_to_enum_Capabilities(enumval):
	if(enumval=="unknown"): return 0
	if(enumval=="still"): return 1
	if(enumval=="stream"): return 2
	if(enumval=="preview"): return 4
	if(enumval=="software_trigger"): return 16
	if(enumval=="continuous_trigger"): return 32
	if(enumval=="external_trigger"): return 64
	if(enumval=="aux_trigger"): return 128

def string_to_enum_OcTreeEncoding(enumval):
	if(enumval=="unknown"): return 0
	if(enumval=="octomap_ot"): return 1
	if(enumval=="octomap_bt"): return 2
	if(enumval=="other"): return 3

def string_to_enum_JointPositionUnits(enumval):
	if(enumval=="implicit"): return 0
	if(enumval=="meter"): return 1
	if(enumval=="radian"): return 2
	if(enumval=="degree"): return 3
	if(enumval=="ticks_lin"): return 4
	if(enumval=="ticks_rot"): return 5
	if(enumval=="nanoticks_lin"): return 6
	if(enumval=="nanoticks_rot"): return 7

def string_to_enum_JointVelocityUnits(enumval):
	if(enumval=="implicit"): return 0
	if(enumval=="meter_second"): return 16
	if(enumval=="radian_second"): return 17
	if(enumval=="degree_second"): return 18
	if(enumval=="ticks_lin_second"): return 19
	if(enumval=="ticks_rot_second"): return 20
	if(enumval=="nanoticks_lin_second"): return 21
	if(enumval=="nanoticks_rot_second"): return 22

def string_to_enum_JointAccelerationUnits(enumval):
	if(enumval=="implicit"): return 0
	if(enumval=="meter_second2"): return 32
	if(enumval=="radian_second2"): return 33
	if(enumval=="degree_second2"): return 34
	if(enumval=="ticks_lin_second2"): return 35
	if(enumval=="ticks_rot_second2"): return 36
	if(enumval=="nanoticks_lin_second2"): return 37
	if(enumval=="nanoticks_rot_second2"): return 38

def string_to_enum_JointJerkUnits(enumval):
	if(enumval=="implicit"): return 0
	if(enumval=="meter_second2"): return 48
	if(enumval=="radian_second3"): return 49
	if(enumval=="degree_second3"): return 50
	if(enumval=="ticks_lin_second3"): return 51
	if(enumval=="ticks_rot_second3"): return 52
	if(enumval=="nanoticks_lin_second3"): return 53
	if(enumval=="nanoticks_rot_second3"): return 54

def string_to_enum_JointEffortUnits(enumval):
	if(enumval=="implicit"): return 0
	if(enumval=="newton"): return 64
	if(enumval=="newton_meter"): return 65
	if(enumval=="ampere"): return 66
	if(enumval=="volt"): return 67
	if(enumval=="pascal"): return 68
	if(enumval=="coulomb"): return 69
	if(enumval=="tesla"): return 70
	if(enumval=="weber"): return 71
	if(enumval=="meter_second2"): return 72
	if(enumval=="radian_second2"): return 73
	if(enumval=="degree_second2"): return 74

def string_to_enum_JointType(enumval):
	if(enumval=="unknown"): return 0
	if(enumval=="revolute"): return 1
	if(enumval=="continuous"): return 2
	if(enumval=="prismatic"): return 3
	if(enumval=="wheel"): return 4
	if(enumval=="screw"): return 5
	if(enumval=="other"): return 6
	if(enumval=="revolute2"): return 7
	if(enumval=="universal"): return 8
	if(enumval=="ball"): return 9
	if(enumval=="planar"): return 10
	if(enumval=="floating"): return 11
	if(enumval=="other_compound"): return 12

def string_to_enum_PlannerStatusCode(enumval):
	if(enumval=="is_not_configured"): return -2
	if(enumval=="failure"): return -1
	if(enumval=="unknown"): return 0
	if(enumval=="is_configured"): return 1
	if(enumval=="running"): return 2
	if(enumval=="success"): return 3

def string_to_enum_RobotTypeCode(enumval):
	if(enumval=="unknown"): return 0
	if(enumval=="serial"): return 1
	if(enumval=="dual_arm"): return 2
	if(enumval=="differential_drive"): return 3
	if(enumval=="planar"): return 4
	if(enumval=="floating"): return 5
	if(enumval=="freeform"): return 6
	if(enumval=="other"): return 7

def string_to_enum_RobotCommandMode(enumval):
	if(enumval=="invalid_state"): return -1
	if(enumval=="halt"): return 0
	if(enumval=="jog"): return 1
	if(enumval=="trajectory"): return 2
	if(enumval=="position_command"): return 3
	if(enumval=="velocity_command"): return 4
	if(enumval=="homing"): return 5

def string_to_enum_RobotOperationalMode(enumval):
	if(enumval=="undefined"): return 0
	if(enumval=="manual_reduced_speed"): return 1
	if(enumval=="manual_full_speed"): return 2
	if(enumval=="auto"): return 3
	if(enumval=="cobot"): return 4

def string_to_enum_RobotControllerState(enumval):
	if(enumval=="undefined"): return 0
	if(enumval=="init"): return 1
	if(enumval=="motor_on"): return 2
	if(enumval=="motor_off"): return 3
	if(enumval=="guard_stop"): return 4
	if(enumval=="emergency_stop"): return 5
	if(enumval=="emergency_stop_reset"): return 6

def string_to_enum_RobotCapabilities(enumval):
	if(enumval=="unknown"): return 0
	if(enumval=="jog_command"): return 1
	if(enumval=="trajectory_command"): return 2
	if(enumval=="position_command"): return 4
	if(enumval=="velocity_command"): return 8
	if(enumval=="homing_command"): return 16
	if(enumval=="software_reset_errors"): return 32
	if(enumval=="software_enable"): return 64

def string_to_enum_RobotStateFlags(enumval):
	if(enumval=="unknown"): return 0
	if(enumval=="error"): return 1
	if(enumval=="fatal_error"): return 2
	if(enumval=="estop"): return 4
	if(enumval=="estop_button1"): return 8
	if(enumval=="estop_button2"): return 16
	if(enumval=="estop_button3"): return 32
	if(enumval=="estop_button4"): return 64
	if(enumval=="estop_guard1"): return 128
	if(enumval=="estop_guard2"): return 256
	if(enumval=="estop_guard3"): return 512
	if(enumval=="estop_guard4"): return 1024
	if(enumval=="estop_software"): return 2048
	if(enumval=="estop_fault"): return 4096
	if(enumval=="estop_internal"): return 8192
	if(enumval=="estop_other"): return 16384
	if(enumval=="estop_released"): return 32768
	if(enumval=="enabling_switch"): return 65536
	if(enumval=="enabled"): return 131072
	if(enumval=="ready"): return 262144
	if(enumval=="homed"): return 524288
	if(enumval=="homing_required"): return 1048576
	if(enumval=="communication_failure"): return 2097152
	if(enumval=="valid_position_command"): return 16777216
	if(enumval=="valid_velocity_command"): return 33554432
	if(enumval=="trajectory_running"): return 67108864

def string_to_enum_ToolType(enumval):
	if(enumval=="unknown"): return 0
	if(enumval=="basic_gripper"): return 1
	if(enumval=="basic_continuous_gripper"): return 2
	if(enumval=="vaccum_gripper"): return 3
	if(enumval=="soft_gripper"): return 4
	if(enumval=="welder"): return 5
	if(enumval=="hand"): return 6
	if(enumval=="palletizer"): return 7
	if(enumval=="other"): return 8

def string_to_enum_ToolStatus(enumval):
	if(enumval=="unknown"): return 0
	if(enumval=="open"): return 1
	if(enumval=="closed"): return 2
	if(enumval=="between"): return 3

def string_to_enum_InterpolationMode(enumval):
	if(enumval=="default"): return 0
	if(enumval=="joint"): return 1
	if(enumval=="linear"): return 2
	if(enumval=="cylindrical"): return 3
	if(enumval=="spherical"): return 4
	if(enumval=="joint_cubic_spline"): return 5
	if(enumval=="cubic_spline"): return 6
	if(enumval=="custom"): return 7

def string_to_enum_SensorTypeCode(enumval):
	if(enumval=="unknown"): return 0
	if(enumval=="generic_digital"): return 1
	if(enumval=="generic_analog"): return 2
	if(enumval=="pushbutton"): return 3
	if(enumval=="dial"): return 4
	if(enumval=="limitswitch"): return 5
	if(enumval=="infrared"): return 6
	if(enumval=="pressure"): return 7
	if(enumval=="vacuum"): return 8
	if(enumval=="temperature"): return 9
	if(enumval=="humidity"): return 10
	if(enumval=="level"): return 11
	if(enumval=="contact"): return 12
	if(enumval=="ultrasonic"): return 13
	if(enumval=="magnetic"): return 14
	if(enumval=="encoder"): return 15
	if(enumval=="potentiometer"): return 16
	if(enumval=="resolver"): return 17
	if(enumval=="linear_encoder"): return 18
	if(enumval=="linear_potentiometer"): return 19
	if(enumval=="lvds"): return 20
	if(enumval=="accelerometer"): return 21
	if(enumval=="gyroscopic"): return 22
	if(enumval=="velocity"): return 23
	if(enumval=="angular_velocity"): return 24
	if(enumval=="spatial_velocity"): return 25
	if(enumval=="torque"): return 26
	if(enumval=="force"): return 27
	if(enumval=="proximity"): return 28
	if(enumval=="voltage"): return 29
	if(enumval=="current"): return 30
	if(enumval=="laser"): return 31
	if(enumval=="flow"): return 32
	if(enumval=="pyrometer"): return 33
	if(enumval=="forcetorque"): return 34
	if(enumval=="light_color"): return 35
	if(enumval=="light_intensity"): return 36
	if(enumval=="object_color"): return 37
	if(enumval=="altitude"): return 38
	if(enumval=="other"): return 39

def string_to_enum_ServoTypeCode(enumval):
	if(enumval=="unknown"): return 0
	if(enumval=="generic_revolute"): return 1
	if(enumval=="generic_prismatic"): return 2
	if(enumval=="revolute_electric"): return 3
	if(enumval=="revolute_linear"): return 4
	if(enumval=="rc_servo"): return 5

def string_to_enum_ServoCapabilities(enumval):
	if(enumval=="unknown"): return 0
	if(enumval=="position_command"): return 1
	if(enumval=="velocity_command"): return 2
	if(enumval=="effort_command"): return 4
	if(enumval=="trapezoidal_command"): return 8
	if(enumval=="signals"): return 4096

def string_to_enum_ServoMode(enumval):
	if(enumval=="error"): return -2
	if(enumval=="disabled"): return -1
	if(enumval=="halt"): return 0
	if(enumval=="position_command"): return 1
	if(enumval=="velocity_command"): return 2
	if(enumval=="effort_command"): return 3
	if(enumval=="trapezoidal_command"): return 4

def string_to_enum_SignalType(enumval):
	if(enumval=="unknown"): return 0
	if(enumval=="digital"): return 1
	if(enumval=="analog"): return 2
	if(enumval=="digital_port"): return 3
	if(enumval=="analog_port"): return 4
	if(enumval=="vector3"): return 5
	if(enumval=="vector6"): return 6
	if(enumval=="wrench"): return 7
	if(enumval=="pose"): return 8
	if(enumval=="transform"): return 9
	if(enumval=="other"): return 10

def string_to_enum_SignalAccessLevel(enumval):
	if(enumval=="undefined"): return 0
	if(enumval=="internal"): return 1
	if(enumval=="restricted"): return 2
	if(enumval=="readonly"): return 3
	if(enumval=="all"): return 4

