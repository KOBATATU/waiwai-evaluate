import numpy as np
import pandas as pd
from sklearn.metrics import f1_score, mean_squared_error

metrics = {
    'rmse': lambda expect, answer: mean_squared_error(expect, answer, squared=False),
    'f1': lambda expect, answer: f1_score(expect, answer, average='weighted')
}