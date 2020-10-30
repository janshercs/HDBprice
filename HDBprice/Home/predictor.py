import numpy as np
import pandas as pd
import pickle
import sys,os,datetime
import sklearn

def unpickleRick(file_name):
    infile = open(file_name, 'rb')
    file = pickle.load(infile)
    infile.close()
    return file

pipe = unpickleRick('Home/pipe1.pickle')
b = 1234
def show_data(post_data):
    data = pd.DataFrame(dict(post_data))
    data = data.drop(['csrfmiddlewaretoken'],axis = 'columns',)
    a = datetime.date.today() - datetime.date(1990,1,1)
    data['tx_day'] = a.days
    result = pipe.predict(data)
    return result
    # except:
    #     return "Error, something went"

# eventually you just need to run pipe.predict('attributes here') 