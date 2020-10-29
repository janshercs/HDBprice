import numpy as np
import pandas as pd
import pickle

def unpickleRick(file_name):
    import pickle
    infile = open(file_name, 'rb')
    file = pickle.load(infile)
    infile.close()
    return file

pipe = unpickleRick('pipe1.pickle')
# eventually you just need to run pipe.predict('attributes here') 