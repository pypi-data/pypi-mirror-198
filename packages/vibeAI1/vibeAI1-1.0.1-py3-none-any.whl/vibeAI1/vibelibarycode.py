import numpy as np
import pickle
import pandas as pd
from pydantic import BaseModel

class data_breache(BaseModel):
    Source_Port: float
    Destination_Port: float
    NAT_Source_Port: float
    Bytes: float
    Bytes_Sent: float
    Bytes_Received: float
    Packets: float
    Elapsed_Time: float
    pkts_sent: float
    pkts_received: float

def load_model():
    pickle_in = open("firewall_model.pkl", "rb")
    classifier = pickle.load(pickle_in)
    return classifier

def block_traffic():
    # code to block suspicious traffic goes here
    print("Blocking suspicious traffic...")

def predict_breach(data):
    classifier = load_model()
    data = data.dict()
    Source_Port = data['Source_Port']
    Destination_Port = data['Destination_Port']
    NAT_Source_Port = data['NAT_Source_Port']
    Bytes = data['Bytes']
    Bytes_Sent = data['Bytes_Sent']
    Bytes_Received = data['Bytes_Received']
    Packets = data['Packets']
    Elapsed_Time = data['Elapsed_Time']
    pkts_sent = data['pkts_sent']
    pkts_received = data['pkts_received']
    prediction = classifier.predict([[Source_Port,Destination_Port,NAT_Source_Port,Bytes,Bytes_Sent,Bytes_Received,Packets,Elapsed_Time,pkts_sent,pkts_received]])
    if prediction[0] == 0:
        prediction = "allow"
    elif prediction[0] == 1:
        prediction = "drop"
    elif prediction[0] == 2:
        prediction = "deny"
    else:
        prediction = "reset-both"
    
    blocked = False
    if prediction in ["drop", "deny"]:
        # keep track of number of times suspicious traffic has been predicted
        if 'num_suspicious' not in predict_breach.__dict__:
            predict_breach.num_suspicious = 1
        else:
            predict_breach.num_suspicious += 1
        
        # block traffic after it has been predicted 3 times
        if predict_breach.num_suspicious >= 3:
            block_traffic()
            blocked = True
    else:
        predict_breach.num_suspicious = 0
    
    return {
        'prediction': prediction,
        'blocked': blocked
    }