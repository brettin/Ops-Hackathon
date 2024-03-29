import tensorflow as tf
import h5py
import keras
import pandas
import sklearn

print('using tensorflow ', tf.__version__)
print('using h5py ', h5py.__version__)
print('using keras ', keras.__version__)
print('using pandas ', pandas.__version__)
print('using sci-kit learn '. sklearn.__version__)

message="""

We generally use tensorflow for our deep learning work.
You can set the backend to tensorflow instead of theano
by modifying the keras.json file located in your home dir.

cat $HOME/.keras/keras.json

You will likely see a RuntimeWarning when running this
test. You can ignore the warning.
"""

print (message)
