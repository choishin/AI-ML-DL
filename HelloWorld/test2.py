import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

result = tf.constant("Tensorflow is easy!!")
sess = tf.Session()
print(str(sess.run(result),encoding='utf8'))