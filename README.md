# Robotics-Indoor-SDK

### Overview
This repository contains ROS Package of Robotics Indoor SDK developed by Estimote.
</br>Package is currently compiled to support RaspberryPi 3 (armv7l GNU/Linux).

### Feedback and support
We are working on support for other platforms, contact us if you need support for specific hardware.
</br>Feel free to share any feedback or ask questions about this project by sending email to contact@estimote.com

### Detailed documentation
Instructions how to prepare your hardware setup and
detailed documentation of the system could be found at our developer portal: LINK_TO_DOCUMENTATION

### Quick installation guide
0. Make sure you have installed ROS and configured Catkin workspace on your Raspberry Pi.
1. Download content of this repository and save as `estimote_robotics_indoor_sdk` folder inside `src/` folder in your catkin workspace (referred later as `$CATKIN_WORKSPACE`)
2. Run `$ catkin_make` from your catkin workspace.
3. Open three separate terminals, run `$ roscore` in first and use last two in steps described below.
4. Start the positioning node:
```sh
$ cd $CATKIN_WORKSPACE
$ source ./devel/setup.bash
$ rosparam load src/estimote_robotics_indoor_sdk/src/params.yaml
$ rosrun estimote_robotics_indoor_sdk runner.py
```
Example output:
```
[Robotics Indoor SDK] initializing ROS node..
[Robotics Indoor SDK] ROS node started, initializing positioning system..
[Robotics Indoor SDK] checking database presence..
[Robotics Indoor SDK] enabling central beacon..
[Robotics Indoor SDK] coordinates data saver started..
[Robotics Indoor SDK] packets data saver started..
[Robotics Indoor SDK] saving distance measures started..
[Robotics Indoor SDK] location data fetched..
[Robotics Indoor SDK] postition estimation started..
[INFO] [1504609463.780477]: 3.01280850467, 10.0553189206
[INFO] [1504609464.300261]: 3.00472775165, 10.0038531813
[INFO] [1504609464.816015]: 3.05423739245, 10.0339022171
```

5. Start an exemplary listener:
```sh
$ cd $CATKIN_WORKSPACE
$ source ./devel/setup.bash
$ rosrun estimote_robotics_indoor_sdk listener.py
```

Example listener output:
```sh
[INFO] [1504611699.781092]: /listener_6832_1504611699257 [Robotics Indoor SDK] x, y = 3.01280850467, 10.0553189206
[INFO] [1504611700.298712]: /listener_6832_1504611699257 [Robotics Indoor SDK] x, y = 3.00472775165, 10.0038531813
[INFO] [1504611700.814251]: /listener_6832_1504611699257 [Robotics Indoor SDK] x, y = 3.05423739245, 10.0339022171
```

Our node posts current robot position in format `x, y` to `estimote_position` ROS topic.
<br/>The rest of messages content presented above was generated in the exemplary `listener.py` script.
