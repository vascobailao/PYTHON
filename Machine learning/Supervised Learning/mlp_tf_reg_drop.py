from __future__ import print_function
import numpy as np
import tensorflow as tf
from six.moves import cPickle as pickle
import pandas as pd
from sklearn.model_selection import train_test_split
import math as math
from sklearn.preprocessing import OneHotEncoder

RANDOM_SEED = 42
FILE = "si_dataset3class.csv"
NUM_LABELS = 3
SIZE_X = 1
SIZE_Y = 7

def pre_processing(FILE):
    df = pd.read_csv(FILE)
    data   = df.iloc[:,1:7]
    target = df.iloc[:,0]
    N, M  = data.shape
    all_X = np.ones((N, M + 1))
    all_X[:, 1:] = data
    num_labels = len(np.unique(target))
    all_Y = np.eye(num_labels)[target]  # One liner trick!

    train_dataset, train_labels, test_dataset, test_labels = train_test_split(all_X, all_Y, test_size=0.33, random_state=RANDOM_SEED)
    print('Training set', train_dataset.shape, train_labels.shape)
    print('Test set', test_dataset.shape, test_labels.shape)
    return train_dataset, train_labels, test_dataset, test_labels

def reformat(labels):

  labels = (np.arange(NUM_LABELS) == labels[:,None]).astype(np.float32)
  return labels

def accuracy(predictions, labels):

    return (100.0 * np.sum(np.argmax(predictions, 1) == np.argmax(labels, 1))
            / predictions.shape[0])

def neural_netowrk(train_dataset, train_labels, test_dataset, test_labels):
    batch_size = 128
    beta = 0.001

    hidden_nodes_1 = 1024
    hidden_nodes_2 = int(hidden_nodes_1 * 0.5)
    hidden_nodes_3 = int(hidden_nodes_1 * np.power(0.5, 2))
    hidden_nodes_4 = int(hidden_nodes_1 * np.power(0.5, 3))
    hidden_nodes_5 = int(hidden_nodes_1 * np.power(0.5, 4))

    graph = tf.Graph()
    with graph.as_default():
        '''Input Data'''
        # For the training data, we use a placeholder that will be fed
        # at run time with a training minibatch.
        tf_train_dataset = tf.placeholder(tf.float32, shape=(batch_size, SIZE_X * SIZE_Y))
        tf_train_labels = tf.placeholder(tf.float32, shape=(batch_size, NUM_LABELS))
        tf_test_dataset = tf.constant(test_dataset)
        tf_test_dataset = tf.cast(tf_test_dataset, tf.float32)

        '''Variables'''
        # Hidden RELU layer 1
        weights_1 = tf.Variable(tf.truncated_normal([SIZE_X * SIZE_Y, hidden_nodes_1], dtype=tf.float32,
                                                    stddev=math.sqrt(2.0 / (SIZE_X * SIZE_Y))))
        biases_1 = tf.Variable(tf.zeros([hidden_nodes_1]), dtype=tf.float32)

        # Hidden RELU layer 2
        weights_2 = tf.Variable(
            tf.truncated_normal([hidden_nodes_1, hidden_nodes_2], stddev=math.sqrt(2.0 / hidden_nodes_1)))
        biases_2 = tf.Variable(tf.zeros([hidden_nodes_2]))

        # Hidden RELU layer 3
        weights_3 = tf.Variable(
            tf.truncated_normal([hidden_nodes_2, hidden_nodes_3], stddev=math.sqrt(2.0 / hidden_nodes_2)))
        biases_3 = tf.Variable(tf.zeros([hidden_nodes_3]))

        # Hidden RELU layer 4
        weights_4 = tf.Variable(
            tf.truncated_normal([hidden_nodes_3, hidden_nodes_4], stddev=math.sqrt(2.0 / hidden_nodes_3)))
        biases_4 = tf.Variable(tf.zeros([hidden_nodes_4]))

        # Hidden RELU layer 5
        weights_5 = tf.Variable(
            tf.truncated_normal([hidden_nodes_4, hidden_nodes_5], stddev=math.sqrt(2.0 / hidden_nodes_4)))
        biases_5 = tf.Variable(tf.zeros([hidden_nodes_5]))

        # Output layer
        weights_6 = tf.Variable(
            tf.truncated_normal([hidden_nodes_5, NUM_LABELS], stddev=math.sqrt(2.0 / hidden_nodes_5)))
        biases_6 = tf.Variable(tf.zeros([NUM_LABELS]))

        '''Training computation'''

        # Hidden RELU layer 1
        logits_1 = tf.matmul(tf_train_dataset, weights_1) + biases_1
        print(weights_1)
        print(tf_test_dataset)
        hidden_layer_1 = tf.nn.relu(logits_1)
        # Dropout on hidden layer: RELU layer
        keep_prob = tf.placeholder("float")
        hidden_layer_1_dropout = tf.nn.dropout(hidden_layer_1, keep_prob)

        # Hidden RELU layer 2
        logits_2 = tf.matmul(hidden_layer_1_dropout, weights_2) + biases_2
        hidden_layer_2 = tf.nn.relu(logits_2)
        # Dropout on hidden layer: RELU layer
        hidden_layer_2_dropout = tf.nn.dropout(hidden_layer_2, keep_prob)

        # Hidden RELU layer 3
        logits_3 = tf.matmul(hidden_layer_2_dropout, weights_3) + biases_3
        hidden_layer_3 = tf.nn.relu(logits_3)
        # Dropout on hidden layer: RELU layer
        hidden_layer_3_dropout = tf.nn.dropout(hidden_layer_3, keep_prob)

        # Hidden RELU layer 4
        logits_4 = tf.matmul(hidden_layer_3_dropout, weights_4) + biases_4
        hidden_layer_4 = tf.nn.relu(logits_4)
        # Dropout on hidden layer: RELU layer

        hidden_layer_4_dropout = tf.nn.dropout(hidden_layer_4, keep_prob)

        # Hidden RELU layer 5
        logits_5 = tf.matmul(hidden_layer_4_dropout, weights_5) + biases_5
        hidden_layer_5 = tf.nn.relu(logits_5)
        # Dropout on hidden layer: RELU layer
        hidden_layer_5_dropout = tf.nn.dropout(hidden_layer_5, keep_prob)

        # Output layer
        logits_6 = tf.matmul(hidden_layer_5_dropout, weights_6) + biases_6

        # Normal loss function
        loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits_6, labels=tf_train_labels))
        # Loss function with L2 Regularization with decaying learning rate beta=0.5
        regularizers = tf.nn.l2_loss(weights_1) + tf.nn.l2_loss(weights_2) + \
                       tf.nn.l2_loss(weights_3) + tf.nn.l2_loss(weights_4) + \
                       tf.nn.l2_loss(weights_5) + tf.nn.l2_loss(weights_6)
        loss = tf.reduce_mean(loss + beta * regularizers)

        '''Optimizer'''
        # Decaying learning rate
        global_step = tf.Variable(0)  # count the number of steps taken.
        start_learning_rate = 0.5
        learning_rate = tf.train.exponential_decay(start_learning_rate, global_step, 100000, 0.96, staircase=True)
        optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss, global_step=global_step)

        # Predictions for the training
        train_prediction = tf.nn.softmax(logits_6)


        # Predictions for test
        test_logits_1 = tf.matmul(tf_test_dataset, weights_1) + biases_1
        test_relu_1 = tf.nn.relu(test_logits_1)

        test_logits_2 = tf.matmul(test_relu_1, weights_2) + biases_2
        test_relu_2 = tf.nn.relu(test_logits_2)

        test_logits_3 = tf.matmul(test_relu_2, weights_3) + biases_3
        test_relu_3 = tf.nn.relu(test_logits_3)

        test_logits_4 = tf.matmul(test_relu_3, weights_4) + biases_4
        test_relu_4 = tf.nn.relu(test_logits_4)

        test_logits_5 = tf.matmul(test_relu_4, weights_5) + biases_5
        test_relu_5 = tf.nn.relu(test_logits_5)

        test_logits_6 = tf.matmul(test_relu_5, weights_6) + biases_6

        test_prediction = tf.nn.softmax(test_logits_6)

    num_steps = 15000

    with tf.Session(graph=graph) as session:
        tf.initialize_all_variables().run()
        print("Initialized")
        for step in range(num_steps):
            # Pick an offset within the training data, which has been randomized.
            # Note: we could use better randomization across epochs.
            offset = (step * batch_size) % (train_labels.shape[0] - batch_size)
            # Generate a minibatch.
            batch_data = train_dataset[offset:(offset + batch_size), :]
            batch_labels = train_labels[offset:(offset + batch_size), :]
            # Prepare a dictionary telling the session where to feed the minibatch.
            # The key of the dictionary is the placeholder node of the graph to be fed,
            # and the value is the numpy array to feed to it.
            feed_dict = {tf_train_dataset: batch_data, tf_train_labels: batch_labels, keep_prob: 0.5}
            _, l, predictions = session.run([optimizer, loss, train_prediction], feed_dict=feed_dict)

            if (step % 500 == 0):
                print("Minibatch loss at step {}: {}".format(step, l))
                print("Minibatch accuracy: {:.1f}".format(accuracy(predictions, batch_labels)))
        print("Test accuracy: {:.1f}".format(accuracy(test_prediction.eval(), test_labels)))


def main():

    train_dataset, train_labels, test_dataset, test_labels = pre_processing(FILE)
    train_labels = reformat(train_labels)
    test_labels = reformat(test_labels)
    print('Training set', train_dataset.shape, train_labels.shape)
    print('Test set', test_dataset.shape, test_labels.shape)

    neural_netowrk(train_dataset, train_labels, test_dataset, test_labels)

    return 0


if __name__ == '__main__':
    main()