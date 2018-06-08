import numpy as np
from datetime import datetime
import tensorflow as tf

def make_minibatches(X, y, batch_size):
    '''Return a list of mini-batches of X and y'''
    m = len(X)
    shuffled_idx = np.random.permutation(np.arange(0,m))
    X_shuffled = X[shuffled_idx]
    y_shuffled = y[shuffled_idx]
    
    mini_batches = []
    n_batch = m//batch_size
    for batch in range(n_batch):
        t = batch*batch_size
        batch = X_shuffled[t:t+batch_size], y_shuffled[t:t+batch_size]
        mini_batches.append(batch)
        
    if n_batch*batch_size < m:
        batch = X_shuffled[t+batch_size:], y_shuffled[t+batch_size:]
        mini_batches.append(batch)
    
    return mini_batches
	
def get_filewriter():
    '''Return a tensorflow FileWriter object'''
    now = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    root_logdir = 'tf_logs'
    logdir = "{}/run-{}/".format(root_logdir, now)
    return tf.summary.FileWriter(logdir, tf.get_default_graph())