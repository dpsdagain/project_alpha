import random

def flip_coin():
    """Flips a coin and returns 'Heads' or 'Tails'."""
    return random.choice(["Heads", "Tails"])

if __name__ == "__main__":
    result = flip_coin()
    print(f"Result: {result}")
