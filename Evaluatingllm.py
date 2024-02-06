## Evaluating Biases in Large Language Models (LLMs) using pdf data and  Diversity Analysis
import numpy as np 
from sklearn.metrics.pairwise import cosine_similarity
word_embeddings = {
    'Data Science': np.array([0.5, 0.5, 0.5]),
    'statics': np.array([0.1, 0.3, 0.5]),
    'python': np.array([0.2, 0.4, 0.2]),
    'machine learning': np.array([0.3, 0.1, 0.4]),
    'NumPY': np.array([0.5, 0.1, 0.3]),
    'pandas': np.array([0.4, 0.2, 0.1]),
    'matplotlib': np.array([0.3, 0.4, 0.3]),
    
    'Versus Python': np.array([0.5, 0.4, 0.5]),
    'Unsupervised': np.array([0.5, 0.5, 0.4]),
    'Unsupervised': np.array([0.5, 0.2, 0.3]),
    
}

#let's define the sets
x = ['Data Science', 'statics', 'python']
y = ['machine learning', 'NumPY', 'pandas']
z = ['matplotlib', 'Unsupervised', 'bUnsupervisedoy']

def s(w, X, Y):
    return sum([cosine_similarity(word_embeddings[w].reshape(1, -1), word_embeddings[x].reshape(1, -1)) for x in X]) - ([cosine_similarity(word_embeddings[w].reshape(1, -1), word_embeddings[y].reshape(1, -1)) for y in Y])
n_score = sum([s( X, Y,Z) for Z in Z]) - sum([s( X, Y) ])