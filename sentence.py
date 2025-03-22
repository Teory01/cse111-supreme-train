import random

def main():
    """Generate and print six sentences in past, present, and future."""
    print(make_sentence(1, "past"))
    print(make_sentence(1, "present"))
    print(make_sentence(1, "future"))
    print(make_sentence(2, "past"))
    print(make_sentence(2, "present"))
    print(make_sentence(2, "future"))

def make_sentence(quantity, tense):
    """Constructs a sentence with a determiner, noun, and verb based on quantity and tense."""
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    
    # Capitalize the first word and form the sentence
    sentence = f"{determiner.capitalize()} {noun} {verb}."
    return sentence

def get_determiner(quantity):
    """Returns a randomly chosen determiner based on singular or plural quantity."""
    determiners = {1: ["a", "one", "the"], 
                   2: ["some", "many", "several"]}
    return random.choice(determiners[quantity])

def get_noun(quantity):
    """Returns a randomly chosen noun based on singular or plural quantity."""
    nouns = {1: ["cat", "dog", "woman", "man", "girl", "boy", "bird", "car", "house", "tree"],
             2: ["cats", "dogs", "women", "men", "girls", "boys", "birds", "cars", "houses", "trees"]}
    return random.choice(nouns[quantity])

def get_verb(quantity, tense):
    """Returns a randomly chosen verb based on quantity and tense."""
    verbs = {
        "past": ["ran", "jumped", "ate", "thought", "laughed", "wrote", "talked", "slept", "read", "walked"],
        "present": {1: ["runs", "jumps", "eats", "thinks", "laughs", "writes", "talks", "sleeps", "reads", "walks"],
                     2: ["run", "jump", "eat", "think", "laugh", "write", "talk", "sleep", "read", "walk"]},
        "future": ["will run", "will jump", "will eat", "will think", "will laugh", "will write", "will talk", "will sleep", "will read", "will walk"]
    }
    
    if tense == "present":
        return random.choice(verbs[tense][quantity])
    return random.choice(verbs[tense])

# Start program execution
if __name__ == "__main__":
    main()
