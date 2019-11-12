This is the project repo for the final project of the Udacity Self-Driving Car Nanodegree: Programming a Real Self-Driving Car. For more information about the project, see the project introduction [here](https://classroom.udacity.com/nanodegrees/nd013/parts/6047fe34-d93c-4f50-8336-b70ef10cb4b2/modules/e1a23b06-329a-4684-a717-ad476f0d8dff/lessons/462c933d-9f24-42d3-8bdc-a08a5fc866e4/concepts/5ab4b122-83e6-436d-850f-9f4d26627fd9).

Please use **one** of the two installation options, either native **or** docker installation.

### Native Installation

* Download the [Udacity Simulator](https://github.com/udacity/CarND-Capstone/releases).

### Docker Installation
[Install Docker](https://docs.docker.com/engine/installation/)

Build the docker container
```bash
docker build . -t capstone
```

Run the docker file
```bash
docker run -p 4567:4567 -v $PWD:/capstone -v /tmp/log:/root/.ros/ --rm -it capstone
```
```bash
use docker exec -it <container-name> bash to launch roscore in a separate terminal tab for testing individual topics for inspection
```
Source devel/setup.bash. rostopic and roslaunch should now be available 

roslaunch launch/styx.launch will start all the nodes and rostopic echo /rosout will start receiving data passed through  rospy logging 

Go to styx/bridge.py and rename steering_wheel_angle_cmd to steering_wheel_angle - This is important as the current version of library has the function renamed and not allowing version downgrade

Pillow needs to be upgraded to use the image classifier (every time docker is restarted)

pip install pillow --upgrade


### Traffic Sign Detector
1. For training data - Enable the flag for data collection in get_light_state function. The data will be saved in the folders named as per light_state returned by traffic lights topics. 
2. Downgrade keras to 2.1.2. This is required for installing keras_squeezenet
3. Transfer learning from squeezenet model is used. Weights from squeezenet are frozen and attached to the layers created by us. To allow fine tuning, SGD with a very low learning rate and large number of epochs are used. SGD is preferred over Adam as per FastAI tutorials 
4. Upgrade pillow if there is error when enabling the image in the simulator
5. With 200 epochs, and 75 steps per epoch, the model is literally memorizing the training data. To reduce run time, the validation scoring is removed in fit_generator process as we do not need to generalize the data, only need to memorize the data (to complete the track course). This is similar to hard coded hand crafted features and will not scale to a different track or different lighting.

### Hardware
1. Nvidia 1080 gtx
2. RAM - 48 GB
3. OS - Ubuntu 18.04

### Real world testing
1. Download [training bag](https://s3-us-west-1.amazonaws.com/udacity-selfdrivingcar/traffic_light_bag_file.zip) that was recorded on the Udacity self-driving car.
2. Unzip the file
```bash
unzip traffic_light_bag_file.zip
```
3. Play the bag file
```bash
rosbag play -l traffic_light_bag_file/traffic_light_training.bag
```
4. Launch your project in site mode
```bash
cd CarND-Capstone/ros
roslaunch launch/site.launch
```
5. Confirm that traffic light detection works on real life images

### Other library/driver information
Outside of `requirements.txt`, here is information on other driver/library versions used in the simulator and Carla:

Specific to these libraries, the simulator grader and Carla use the following:

|        | Simulator | Carla  |
| :-----------: |:-------------:| :-----:|
| Nvidia driver | 384.130 | 384.130 |
| CUDA | 8.0.61 | 8.0.61 |
| cuDNN | 6.0.21 | 6.0.21 |
| TensorRT | N/A | N/A |
| OpenCV | 3.2.0-dev | 2.4.8 |
| OpenMP | N/A | N/A |

We are working on a fix to line up the OpenCV versions between the two.
