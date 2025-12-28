import pandas as pd
import numpy as np

def load_sample_data():
    return pd.DataFrame({
        'feature1': np.random.rand(100),
        'feature2': np.random.rand(100),
        'target': np.random.randint(0,2,100)
    })
