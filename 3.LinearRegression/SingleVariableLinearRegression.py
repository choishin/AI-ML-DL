import tensorflow as tf
import numpy as np
from matplotlib import pyplot as plt

trainDataNumber = 100
learningRate = 0.01
totalStep=1001

np.random.seed(321)
xTraninData=list()
yTrainData=list()
xTrainData = np.random.normal(0.0,1.0, size=trainDataNumber)

for x in xTrainData:
    y=10*x+3+np.random.normal(0.0,3)
    yTrainData.append(y)

plt.plot(xTrainData,yTrainData,'bo')
plt.title("Train data")
plt.show()

W = tf.Variable(tf.random_uniform([1]))
b = tf.Variable(tf.random_uniform([1]))
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

hypothesis = W * X + b
costFunction = tf.reduce_mean(tf.square(hypothesis - Y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learningRate)
train = optimizer.minimize(costFunction)

sess=tf.Session()
sess.run(tf.global_variables_initializer())
WeightValueList=list()
costFunctionValueList=list()

print("-----------------------------------------------------------------------------")
print("Train(Optimization) Start")
for step in range(totalStep):
    cost_val,W_val,b_val,_ = sess.run([costFunction,W,b,train], feed_dict={X:xTrainData, Y: yTrainData})
    WeightValueList.append(W_val)
    costFunctionValueList.append(cost_val)
    if step % 50 == 0:
        print("step : {}, cost : {}, W: {}, b : {}".format(step,cost_val,W_val,b_val))
        if step % 100 == 0:
            plt.plot(xTrainData,W_val * xTrainData + b_val, label='Step : {}'.format(step), linewidth=0.5)
print("Train Finished")

print("-----------------------------------------------------------------------------")
print("Train Result")
cost_train = sess.run(costFunction, feed_dict={X:xTrainData, Y:yTrainData})
w_train = sess.run(W)
b_train = sess.run(b)
print("Train cost : {}, W : {}, b : {}".format(cost_train, w_train, b_train))
print("-----------------------------------------------------------------------------")
print("[Test Result]")
testXValue = [2.5]
resultYValue = sess.run(hypothesis, feed_dict={X: testXValue})
print("x value is {}, y value is {}".format(testXValue, resultYValue))
print("-----------------------------------------------------------------------------")

plt.plot(xTrainData, sess.run(W) * xTrainData + sess.run(b), 'r', label='Fitting Line',linewidth=2)
plt.plot(xTrainData, yTrainData, 'bo',label='Train data')
plt.legend()
plt.title("Train Result")
plt.show()

plt.plot(WeightValueList,costFunctionValueList)
plt.title("costFunction curve")
plt.xlabel("Weight")
plt.ylabel("costFunction value")
plt.show()

sess.close()