# src/ingestion/kafka_producer.py
import time
import pandas as pd
from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Load and preprocess your dataset (e.g., NAB)
df = pd.read_csv('data//PerformanceGraphExport.csv')
df = df[['Effective date ', 'S&P 500']]

print(df.head())

df=df.dropna()
print(df)


'''
for _, row in df.iterrows():
    event = row.to_dict()
    producer.send('anomaly-topic', value=event)
    time.sleep(1)  # Simulate streaming every 1s
''' 