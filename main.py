from fastapi import FastAPI
import pickle
import pandas as pd
import numpy as np
import warnings
# from sklearn.exceptions import InconsistentVersionWarning

# warnings.filterwarnings("ignore", category=InconsistentVersionWarning)

app = FastAPI()

model = pickle.load(open("l.pkl","rb"))
# x=np.array([[29, 77000]])
# p = model.predict(x)


@app.post('/p/{item_id}/{id}')
async def p(item_id : int , id : int):
    responce = np.array([[item_id,id]])
    responce_pd = pd.DataFrame(responce , columns = ['Age' , 'EstimatedSalary'])
    prediction = model.predict(responce_pd)
    if 1 in prediction:
        pre = "avalible" + '{}'.format(prediction)
    else:
        pre ="no avalible" + '{}'.format(prediction)
    return {'value':pre}