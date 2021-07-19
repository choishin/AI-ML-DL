import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

result = tf.constant("Tensorflow is easy!!")
sess = tf.Session()
print(sess.run(result))