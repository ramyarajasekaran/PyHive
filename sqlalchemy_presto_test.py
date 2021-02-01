from sqlalchemy import *
from sqlalchemy.engine import create_engine
import logging
#logging.basicConfig()
logging.getLogger('sqlalchemy').setLevel(logging.DEBUG)

#Input Information
host = 'cluster'
user = 'ramyarajasekaran'
port = 443
catalog = 'catalog'
schema = 'schema'
table = 'table'

#Execution
engine = create_engine(
        f'presto://{host}:{port}/{catalog}',
        connect_args={
            'protocol': 'https',
            'requests_kwargs' : {
                'verify':'certs/ca/cacerts.pem' 
            },
            'username':'ramyarajasekaran',
            'password':'passcode'
        }
    )

conn = engine.raw_connection() 
try:
    cursor = conn.cursor()

    
    for i in range(3):
        query = input('Enter Query: ')

        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)

    cursor.close()
finally:
    conn.close()