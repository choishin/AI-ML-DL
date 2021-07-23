import tensorflow as tf

result = tf.constant("Tensorflow is easy!!")
sess = tf.Session()
print(sess.run(result))