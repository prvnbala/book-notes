lexicon = {
    "direction" : ["north", "south", "east", "west", "down", "up", "right", "left", "back"],
    "verb" : ["go", "stop", "kill", "eat"],
    "stop" : ["the", "in", "from", "of", "at", "it"],
    "noun" : ["door", "bear", "princess", "cabinet"]
}


def scan(sentence):
    result = []
    words = sentence.split()
    for word in words:
        result.append(get_type_and_word_pair(word))
    
    return result


def get_type_and_word_pair(word):
    type = get_type_from_lexicon(word)

    if type != None:
        return (type, word)
    else:
        print(f"{word} not present in lexicon")
        value = convert_number(word)
        if value != None:
            return ("number", value)
        else:
            print(f"{word} is not a number")
            return ("error", word)
            
        
        type_value_pair = (type, value)


def get_type_from_lexicon(word):
    for key in lexicon:
        if word.lower() in lexicon[key]:
            return key
        else:
            print(f"{word} not present in {key} list")
    return None


def convert_number(word):
    try:
        return int(word)
    except ValueError:
        return None