import tensorflow.compat.v1 as tf
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

trainDataNumber = 200
learningRate = 0.01
totalStep = 1001

np.random.seed(321)

x1TrainData = list()
x2TrainData = list()
yTrainData = list()

x1TrainData = np.random.normal(0.0,1.0, size=trainDataNumber)
x2TrainData = np.random.normal(0.0,1.0, size=trainDataNumber)

for i in range(0,trainDataNumber):
    x1 = x1TrainData[i]
    x2 = x2TrainData[i]
    y = 10* x1 + 5.5 * x2 + 3 + np.random.normal(0.0,3)
    yTrainData.append(y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x1TrainData, x2TrainData, yTrainData, linestyle="none", marker="o",mfc="none",markeredgecolor="red")
plt.show()

W1 = tf.Variable(tf.random.uniform([1]))
W2 = tf.Variable(tf.random.uniform([1]))
b = tf.Variable(tf.random.uniform([1]))

X1 = tf.placeholder(tf.float32)
X2 = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

hypothesis = W1 * X1 + W2 * X2 + b
costFunction = tf.reduce_mean(tf.square(hypothesis - Y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learningRate)
train = optimizer.minimize(costFunction)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.plot(x1TrainData, x2TrainData, yTrainData, lineStyle="none", marker="o", mfc="none", markeredgecolor="red")
Xs = np.arange(min(x1TrainData), max(x1TrainData), 0.05)
Ys = np.arange(min(x2TrainData), max(x2TrainData), 0.05)
Xs, Ys = np.meshgrid(Xs,Ys)

print("-----------------------------------------------------------------------------")
print("Train(Optimization) Start")
for step in range(totalStep):
    cost_val, W1_val, W2_val, b_val, _ = sess.run([costFunction, W1, W2, b, train],
                                                  feed_dict={X1: x1TrainData, X2: x2TrainData, Y: yTrainData})

    if step % 50 == 0:
        print("step : {}, cost : {}, W1 : {}, W2 : {}, b :{}".format(step, cost_val, W1_val, W2_val, b_val))

        if step % 100 == 0:
            ax.plot_surface(Xs, Ys, W1_val * Xs + W2_val * Ys + b_val, rstride=4, cstride=4, alpha=0.2, cmap=cm.jet)

print("Train Finished")
print("-----------------------------------------------------------------------------")
plt.show()
sess.close()