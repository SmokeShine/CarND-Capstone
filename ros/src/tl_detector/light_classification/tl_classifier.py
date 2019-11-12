import cv2
import numpy as np
import tensorflow as tf
from keras.models import model_from_yaml
import rospy
import pdb
from styx_msgs.msg import TrafficLight
from time import time

CLASSIFIER_MODEL_WEIGHTS_FILE = 'light_classification/A.h5'
CLASSIFIER_MODEL_YAML_FILE = 'light_classification/classifier_model-Copy1.yaml'

CLASSIFIER_MODEL_WEIGHTS_FILE = 'light_classification/classifier_model_weights.h5'
CLASSIFIER_MODEL_YAML_FILE = 'light_classification/classifier_model.yaml'


class TLClassifier(object):
    def __init__(self):
        rospy.loginfo('Loading Traffic Light Classifier ...')

        # Loading YAML and creating classifier's model
        classifier_yaml_file = open(CLASSIFIER_MODEL_YAML_FILE, 'r')
        loaded_classifier_model_yaml = classifier_yaml_file.read()
        classifier_yaml_file.close()
        self.classifier_model = model_from_yaml(loaded_classifier_model_yaml)

        # Loading weights into the model
        self.classifier_model.load_weights(CLASSIFIER_MODEL_WEIGHTS_FILE)
        self.graph = tf.get_default_graph()

        rospy.loginfo('Traffic Light Classifier is READY')


    def get_classification(self, image):
        """Determines the color of the traffic light in the image
        Args:
            image (cv::Mat): image containing the traffic light
        Returns:
            int: ID of traffic light color (specified in styx_msgs/TrafficLight)
        """
        prediction=-1 
#         cv2.imwrite('light_classification/test_image3_original.jpg',image)
        traffic_light_states = ['GREEN', 'RED', 'YELLOW', 'NO COLOR']
        with self.graph.as_default():
            prediction = np.argmax(self.classifier_model.predict(cv2.resize(image, (224,224)).reshape(1,224,224,3))[0])
        
        light_state=traffic_light_states[prediction]
        rospy.logwarn('Traffic Light Prediction - ' + traffic_light_states[prediction])
        if light_state=='RED':
            return TrafficLight.RED
        elif light_state=='GREEN':
            return TrafficLight.GREEN
        elif light_state=='YELLOW':
            return TrafficLight.YELLOW
        
        return TrafficLight.UNKNOWN
