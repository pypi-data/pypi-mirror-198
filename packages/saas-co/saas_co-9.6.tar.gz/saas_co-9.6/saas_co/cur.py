import time
import awswrangler as wr
from functools import partial
import pandas as pd

#####################

def query(session, s, **kargs):
    generated_query = generate_query(s, **kargs) 
    return partial(wr.athena.read_sql_query,
                   database=kargs.get('db'),
                   boto3_session=session)(generated_query)

#####################

def generate_query(s, **kargs):
    for key,val in kargs.items():
        s = s.replace('{' + key + '}', str(val)) if f'{key}' in s else s
    return s

#####################

def execute_query(s,query, db, wg):
    try:
        athena = s.client('athena')
        query_execution_id = athena.start_query_execution(
            QueryString=query, QueryExecutionContext={"Database": db}, WorkGroup=wg
        )["QueryExecutionId"]

        # Poll for result
        result = athena.get_query_execution(QueryExecutionId=query_execution_id)["QueryExecution"]
        while result["Status"]["State"] in ["QUEUED", "RUNNING"]:
            result = athena.get_query_execution(QueryExecutionId=query_execution_id)["QueryExecution"]
            time.sleep(1)
                    
        # Copy result to dataframe
        if result["Status"]["State"] == "SUCCEEDED":
            bucket, key = result["ResultConfiguration"]["OutputLocation"].split("s3://")[-1].split("/", 1)
            body = s.client('s3').get_object(Bucket=bucket, Key=key)["Body"]
            return pd.read_csv(body).reset_index(drop=True)
        else:
            return pd.DataFrame()
    except Exception as e:
        print(e) 
        return pd.DataFrame()