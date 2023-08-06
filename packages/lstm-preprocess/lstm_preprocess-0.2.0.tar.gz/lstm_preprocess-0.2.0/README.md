#This is a tool used to reshape dataset in pandas for Keras LSTM model

### This module provides a single function that converts a multivariate time series dataframe into a supervised learning - style dataframe by flattening and shifting each series along a given lagging period. For example, when one tries to use keras on a 2-D tensor of shape (total_time_steps, num_features), it's required to reshape the tensor into a 3-D tensor of input_shape (num_features, time_steps, batch_size)









