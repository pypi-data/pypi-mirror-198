# %%
import numpy as np
from pathlib import Path

# print(Path('/Users/arjunharidas/Documents/tahini-tensor-encounter-notes/week11/python_packaging/randomrecommender/recommender/data/movies.txt').parent.parent)
movies =[]
with open(Path(__file__).parent/'data/movies.txt') as file:
    movies = file.readlines()

def random_recommeder(movies=movies,k=5):
    return np.random.choice(movies,k)

# %%
from recommender import rec
rec.random_recommeder()
# %%
