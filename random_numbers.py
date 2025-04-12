import random

def main():
    # Create a list of numbers
    numbers = [16.2, 75.1, 52.3]
    # Print the list of numbers
    print(numbers)
    
    # Call the function append_random_numbers with the list of numbers as an argument
    append_random_numbers(numbers)
    # Print the list of numbers after the function has been called
    print(numbers)
    
    # Call the function append_random_numbers with the list of numbers and the number 3 as arguments
    append_random_numbers(numbers, 3)
    # Print the list of numbers after the function has been called
    print(f"numbers {numbers}") # Print the list of numbers after the function has been called print(numbers)


    words = []
    append_random_words(words)
    print(f"words {words}")

    append_random_words(words, 5)
    print(f"words {words}")

# Define a function called append_random_numbers that takes in a list of numbers and an optional quantity parameter
def append_random_numbers(numbers_list, quantity=1):
    # Loop through the quantity parameter
    for _ in range(quantity):
        # Generate a random number between 0 and 100 and round it to 1 decimal place
        random_num = round(random.uniform(0, 100), 1)
        # Append the random number to the numbers_list
        numbers_list.append(random_num)


def append_random_words(words_list, quantity=1):
    candidates = [
        "arm", "car", "cloud", "head", "heal", "hydrogen", "jog",
        "join", "laugh", "love", "sleep", "smile", "speak", "walk"
    ]
    # Loop through the quantity parameter
    for _ in range(quantity):
        # Choose a random word from the candidates list
        word = random.choice(candidates)
        # Append the word to the words_list
        words_list.append(word)



if __name__ == "__main__":
    main()

    