import random


def get_ids(model) -> list:
    ids = list(model.values_list('id', flat=True))
    print(ids)
    k = random.choice([2, 3])
    random_ids = random.sample(ids, k=k)
    return random_ids
