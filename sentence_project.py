import random

def main():
    """Generate and print six sentences with different grammar combinations."""
    print("Single Past:    ", make_sentence(1, "past"))
    print("Single Present: ", make_sentence(1, "present"))
    print("Single Future:  ", make_sentence(1, "future"))
    print("Plural Past:    ", make_sentence(2, "past"))
    print("Plural Present: ", make_sentence(2, "present"))
    print("Plural Future:  ", make_sentence(2, "future"))

def make_sentence(quantity, tense):
    """Constructs a sentence with a determiner, adjective, noun, adverb, verb, and a prepositional phrase."""
    determiner = get_determiner(quantity)
    adjective = get_adjective()
    noun = get_noun(quantity)
    adverb = get_adverb()
    verb = get_verb(quantity, tense)
    prepositional_phrase = get_prepositional_phrase(quantity)
    
    # Construct sentence ensuring optional adjectives and adverbs appear correctly
    sentence = f"{determiner.capitalize()} {adjective} {noun} {adverb} {verb} {prepositional_phrase}."
    return " ".join(sentence.split())  # Remove double spaces if an adjective or adverb isn't used

def get_determiner(quantity):
    """Returns a randomly chosen determiner based on singular or plural quantity."""
    determiners = {1: ["a", "that", "the"], 
                   2: ["some", "many", "several"]}
    return random.choice(determiners[quantity])

def get_adjective():
    """Returns a randomly chosen adjective or an empty string (to keep variety)."""
    adjectives = ["big", "small", "happy", "sad", "fast", "slow", "red", "blue", "beautiful", "strange", ""]
    return random.choice(adjectives)

def get_noun(quantity):
    """Returns a randomly chosen noun based on singular or plural quantity."""
    nouns = {1: ["cat", "dog", "woman", "man", "girl", "boy", "bird", "car", "house", "tree"],
             2: ["cats", "dogs", "women", "men", "girls", "boys", "birds", "cars", "houses", "trees"]}
    return random.choice(nouns[quantity])

def get_adverb():
    """Returns a randomly chosen adverb or an empty string (to keep variety)."""
    adverbs = ["quickly", "slowly", "happily", "sadly", "loudly", "silently", "gracefully", "angrily", ""]
    return random.choice(adverbs)

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

def get_preposition():
    """Returns a randomly chosen preposition."""
    prepositions = ["about", "above", "across", "after", "along", "around", "at", 
                    "before", "behind", "below", "beside", "between", "by", "down", 
                    "in", "inside", "near", "off", "on", "over", "through", "to", "under", "with"]
    return random.choice(prepositions)

def get_prepositional_phrase(quantity):
    """Constructs a prepositional phrase with a preposition, determiner, and noun."""
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    
    return f"{preposition} {determiner} {noun}"

# Start program execution
if __name__ == "__main__":
    main()
