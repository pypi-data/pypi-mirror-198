import boto3
import pandas as pd
from io import StringIO as sio

#####################################

def get_assumed_object(s, **kargs):
    s3 = s.client('s3', kargs.get('region','us-east-1'))
    obj = s3.get_object(Bucket=kargs.get('bucket'), Key=kargs.get('key'))
    return obj['Body'].read().decode('utf-8') 

def get_object(**kargs):
    s3 = boto3.resource('s3')
    obj = s3.Object(kargs.get('bucket'), kargs.get('key'))
    return obj.get()['Body'].read().decode('utf-8') 

def get_csv_data_from_s3(**kargs):
    s = kargs.get('session')
    b = kargs.get('bucket')
    k = kargs.get('key')
    data = get_assumed_object(s, bucket=b, key=k)
    return pd.read_csv(sio(data), sep=","); 

#####################################

def put_object(s, **kargs):
    d = kargs.get('data')
    k = kargs.get('key')
    b = kargs.get('bucket')
    r = kargs.get('region', 'us-east-1')
    s.client('s3', r).put_object(Body=d, Bucket=b, Key=k)
    print(f'https://{b}.s3.amazonaws.com/{k}')

#####################################
