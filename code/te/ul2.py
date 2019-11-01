import os
import tensorflow as tf
from tensorflow.python.util import deprecation
tf.compat.v1.disable_eager_execution()
tf.compat.v1.disable_control_flow_v2()
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
deprecation._PRINT_DEPRECATION_WARNINGS = False
