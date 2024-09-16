
import random

def generate_random_integer(start, end):
    """Generate a random integer between start and end (inclusive)."""
    return random.randint(start, end)

def generate_random_float(start, end):
    """Generate a random float between start and end."""
    return random.uniform(start, end)

def choose_random_item(items):
    """Choose a random item from a list."""
    return random.choice(items)

def shuffle_list(items):
    """Shuffle a list randomly and return it."""
    shuffled_list = items[:]
    random.shuffle(shuffled_list)
    return shuffled_list

def generate_random_name():
    """Generate a random name using predefined lists of first and last names."""
    first_names = ['Alice', 'Bob', 'Charlie', 'Diana']
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown']
    
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    
    return f"{first_name} {last_name}"

# Example usage
if __name__ == "__main__":
    # Generate a random integer between 1 and 100
    print("Random Integer:", generate_random_integer(1, 100))
    
    # Generate a random float between 0 and 1
    print("Random Float:", generate_random_float(0, 1))
    
    # Choose a random item from a list
    items = ['apple', 'banana', 'cherry', 'date']
    print("Random Item:", choose_random_item(items))
    
    # Shuffle a list
    print("Shuffled List:", shuffle_list(items))
    
    # Generate a random name
    print("Random Name:", generate_random_name())
