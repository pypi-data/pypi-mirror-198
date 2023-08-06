# sequence-model-train
Sequence-model-train is a Python library for implementing Long Short-Term Memory (LSTM) models on time-series data. It takes a CSV file as input and allows you to specify various hyperparameters for the model.    
   
Github:   
​https://github.com/ZhangLe59151/price_forecast   
PyPi:   
​https://pypi.org/project/sequence-model-train/   
Document:    
​https://zhanglenus.gitbook.io/sequence-model-train-library-document/   
Example on the notebook:   
https://zhanglenus.gitbook.io/sequence-model-train-library-document/notebook-demo      

# Installation
To install Library Sequence-model-train, run the following command in your terminal:   
```
pip install sequence-model-train
```

# Usage  
To use Library Sequence-model-train, follow these steps:
1. Import the library:
```
from sequence_model_train import train_model  
```
2. Create an instance of the TrainModel class and pass in the path to your training data CSV file:   
```
train = train_model.TrainModel('/path/to/data.csv')   
```
3. Update the hyperparameters for the model by calling the `update_params()` method:
```
train.update_params(n_in=30, n_out=7, batch_size=128, hidden_size=128, num_epochs=100)
```
4. Train the model by calling the train() method:
```
train.train()
```
# API Reference
`TrainModel`   
#### Parameters:   
* data_path: a string that specifies the path to the training data CSV file. When creating an instance of the TrainModel class, you can provide the 'data_path' parameter to load your data. It is important to note that the last column in the CSV file should be the labels.   
#### Methods:   
* update_params: After creating an instance of the TrainModel class, you can update the following hyperparameters:   
  - data_path: The data path to your training dataset in CSV format.      
  - n_in: The number of time steps to use as input. The default value is 3.   
  - n_out: The number of future time steps to predict. The default value is 5.   
  - batch_size: The batch size to use during training. The default value is 32.   
  - hidden_size: The number of units in the LSTM layer. The default value is 32.   
  - num_layers: The number of the LSTM layer. The default value is 3.   
  - num_epochs: The number of epochs to train the model for. The default value is 10.   
- train: Train the model. Training the model involves several steps, including data processing, normalization, and splitting into training and validation sets. Once trained, the model's performance is evaluated on the validation set using metrics such as loss, mean absolute error (MAE), and mean absolute percentage error (MAPE).   
# Example
```
# train the model
from sequence_model_train import train_model

train = train_model.TrainModel('./train.csv')
train.update_params(n_in=30, n_out=7, batch_size=128, hidden_size=128, num_epochs=100)
train.train()
```
```
# the result

{
 'model': 'lstm',
 'valid_result': 
   {
    'valid_loss': 61.97545757072,
    'valid_mae': 21.2288062782732,
    'valid_mape': 0.1061233304225267
   }
}
```
# Conclusion
Sequence-model-train is a powerful tool for training LSTM models on time-series data. Its easy-to-use interface and comprehensive API make it a great choice for both beginners and advanced users. Hope you find this library useful and welcome your feedback and suggestions for improvement.   