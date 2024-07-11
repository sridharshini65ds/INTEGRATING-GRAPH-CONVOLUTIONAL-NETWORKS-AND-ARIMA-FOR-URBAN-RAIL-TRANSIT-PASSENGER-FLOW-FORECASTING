#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tensorflow as tf
from tensorflow.keras.layers import Layer
from tensorflow.keras.regularizers import l2

class GraphConvolution1(Layer):
    def __init__(self, units, adj, activation='relu', kernel_regularizer=None):
        super(GraphConvolution1, self).__init__()
        self.units = units
        self.adj = tf.convert_to_tensor(adj, dtype=tf.float32)
        self.activation = tf.keras.activations.get(activation)
        self.kernel_regularizer = tf.keras.regularizers.get(kernel_regularizer)

    def build(self, input_shape):
        self.kernel = self.add_weight(name='kernel',
                                      shape=(input_shape[-1], self.units),
                                      initializer='glorot_uniform',
                                      regularizer=self.kernel_regularizer,
                                      trainable=True)
        self.built = True

    def call(self, inputs):
        output = tf.matmul(self.adj, inputs)
        output = tf.matmul(output, self.kernel)
        return self.activation(output)


# In[ ]:




