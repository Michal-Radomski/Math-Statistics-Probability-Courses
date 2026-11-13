import itertools
import random

random.seed(123)


# Probability
def coin_trial():
    heads = 0
    for i in range(100):
        if random.random() <= 0.5:
            heads += 1
        return heads


def simulate(n):
    trials = []
    for i in range(n):
        trials.append(coin_trial())
    return sum(trials) / n


print("simulate(10):", simulate(10))

print("simulate(100):", simulate(100))

print("simulate(1000):", simulate(1000))

print("simulate(100000):", simulate(100000))

# Permutations
# make a deck of cards
deck = list(
    itertools.product(
        ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"],
        ["Spade", "Heart", "Diamond", "Club"],
    )
)
print("deck[:10]:", deck[:10])

aces = []
for card in deck:
    if card[0] == "A":
        aces.append(card)
print("aces:", aces)


def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    indices = list(range(n))
    cycles = list(range(n, n - r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i + 1 :] + indices[i : i + 1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return


aces_permutations = []
for p in permutations(aces, 2):
    aces_permutations.append(p)
    print(p)

print("len(aces_permutations):", len(aces_permutations))


# Combinations
def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
        yield tuple(pool[i] for i in indices)


aces_combinations = []
for c in combinations(aces, 2):
    aces_combinations.append(c)
    print(c)

print("len(aces_combinations):", len(aces_combinations))


# Create function that returns probability percent rounded to one decimal place
def event_probability(event_outcomes, sample_space):
    probability = (event_outcomes / sample_space) * 100
    return round(probability, 1)


# Sample Space
cards = 52

# Calculate the probability of drawing a heart or a club
hearts = 13
clubs = 13
heart_or_club = event_probability(hearts, cards) + event_probability(clubs, cards)

print("heart_or_club:", heart_or_club)


# Sample Space
cards = 52

# Calculate the probability of drawing a heart or an ace
hearts = 13
aces = 4
ace_of_hearts = 1
heart_or_ace = (
    event_probability(hearts, cards)
    + event_probability(aces, cards)
    - event_probability(ace_of_hearts, cards)
)


print("round(heart_or_ace, 1):", round(heart_or_ace, 1))

# Initialize `pot` and `probability` variables
pot = 100
probability = 0.75

# Determine expected value
expected_value = pot * probability
print("expected_value:", expected_value)
