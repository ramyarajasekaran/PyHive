from pyhive import presto
import pandas as pd


cursor = presto.connect(
        host='cluster',
        port=443, 
        protocol='https',
        requests_kwargs={
                'verify':'/certs/cacerts.pem' 
        },
        username='ramyarajasekaran',
        password='passcode',
        catalog='catalog',
        schema='schema'
    ).cursor()

while(True):

    query = input ("Enter Query :") 
    print('QUERY:' + query)

    cursor.execute(query)

    df = pd.DataFrame(cursor.fetchall(), columns=[desc[0] for desc in cursor.description])

    print('RESULTS:')
    print(df)