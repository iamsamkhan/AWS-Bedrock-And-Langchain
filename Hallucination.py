from sentence_transformers import CrossEncoder
model = CrossEncoder('vectara/hallucination_evaluation_model')
model 
scores = model.predict([
    ["meta dataa"],  
])

scores

import numpy as np 

# Convert the values to one decimal point
score_one_decimal = np.around(scores, decimals=1)

# Convert the values to percentage with one decimal point
score_percentage = np.around(scores * 100, decimals=1)
score_one_decimal

score_percentage




