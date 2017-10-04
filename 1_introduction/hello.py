import tensorflow as tf

# op
hello = tf.constant("hello tensorflow!")

# sess the graph
sess = tf.Session()
print(sess.run(hello))