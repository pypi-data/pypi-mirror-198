"""
rc_cbed network design to restore and center CBED images

Author: Ivan Lobato
Email: Ivanlh20@gmail.com
"""
import pathlib
import h5py
import numpy as np

def fcn_set_gpu_id(gpu_visible_devices="0"):
    import os
    os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
    os.environ['CUDA_VISIBLE_DEVICES'] = gpu_visible_devices

def load_rc_cbed_net(model_path=None, gpu_id="0"):
    fcn_set_gpu_id(gpu_id)

    import tensorflow as tf
    
    if model_path is None:
        model_path = pathlib.Path(__file__).resolve().parent / 'model_rc_cbed'
    else:
        model_path = pathlib.Path(model_path).resolve() 
          
    return tf.keras.models.load_model(model_path)

def load_test_data(path=None):
    if path is None:
        path = pathlib.Path(__file__).resolve().parent / 'test_data.h5'
    else:
        path = pathlib.Path(path).resolve() 

    h5file = h5py.File(path, 'r')
    x = h5file['x'][:]
    x = np.transpose(x, (0, 3, 2, 1)).astype(np.float32)

    y = h5file['y'][:]
    y = np.transpose(y, (0, 3, 2, 1)).astype(np.float32)

    return x, y