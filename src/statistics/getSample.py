from random import random


def getSample(data, sample_size):
    random_values = random.sample(data, sample_size)
    return random_values
