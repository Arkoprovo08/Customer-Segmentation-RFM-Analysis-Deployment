import numpy as np
from config import scaler, kmeans, quantiles


def predict_segment(recency, frequency, monetary):
    # Step 1: log transform
    recency_log = np.log1p(recency)
    frequency_log = np.log1p(frequency)
    monetary_log = np.log1p(monetary)
    
    # Step 2: scaling
    data = np.array([[recency_log, frequency_log, monetary_log]])
    data_scaled = scaler.transform(data)
    
    # Step 3: cluster prediction
    cluster = kmeans.predict(data_scaled)[0]
    
    # Step 4: base segment mapping
    segment_map = {
        1: 'High Value',
        0: 'Regular',
        2: 'At Risk'
    }    
    segment = segment_map.get(cluster, "Unknown")
    
    # Step 5: business rule refinement (using quantiles)
    
    segment_final = segment
    
    # Lost High Value
    if (
        monetary > quantiles["monetary_75"] and
        recency > quantiles["recency_75"]
    ):
        segment_final = "Lost High Value"
    
    # Potential High Value
    elif (
        recency < quantiles["recency_25"] and
        frequency >= quantiles["frequency_50"] and
        monetary >= quantiles["monetary_50"] and
        monetary < quantiles["monetary_75"]
    ):
        segment_final = "Potential High Value"
    
    return {
        "cluster": int(cluster),
        "segment": segment,
        "segment_final": segment_final
    }