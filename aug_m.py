import random

def augment_string(input_string):
    # Universal leet dictionary, including symbols from all supported language groups
    leet_dict = {
        'a': '4', 'b': '8', 'c': '(', 'e': '3', 'g': '9', 'i': '1', 'o': '0', 's': '5', 't': '7', 'z': '2',
        'ä': '43', 'ö': '03', 'ü': 'v3', 'å': '00', 'ø': 'ø', 'æ': '4e', 'ç': 'c', 'ñ': '~n', 'ý': 'y', 'ß': 'B', 'õ': '0~', 'ħ': '#',
        'а': '4', 'б': '6', 'в': '8', 'г': 'r', 'ґ': 'g', 'д': 'd', 'е': '3', 'є': 'є', 'ж': '>*<', 'з': '3', 'и': '1', 'і': '!', 
        'ї': 'ї', 'й': 'u', 'к': '>|<', 'л': '/\\', 'м': '|v|', 'н': 'н', 'о': '0', 'п': 'п', 'р': 'p', 'с': '5', 'т': '7', 'у': 'y', 
        'ф': 'qp', 'х': 'x', 'ц': 'ц', 'ч': '4', 'ш': 'w', 'щ': 'щ', 'ъ': '`', 'ы': 'bl', 'ь': 'b', 'э': '3', 'ю': '10', 'я': '9'
    }

    # Function for leet transformation
    def to_leet(word):
        return ''.join(leet_dict.get(char.lower(), char) for char in word)
    
    # 1. Reversed string
    reversed_string = input_string[::-1]
    
    # 2. String with all words concatenated
    concatenated_string = ''.join(input_string.split())
    
    # 3. String where random 2-3 letters are "eaten"
    def remove_random_chars(word):
        if len(word) > 3:
            num_to_remove = random.randint(2, 3)
            indices_to_remove = random.sample(range(len(word)), min(num_to_remove, len(word)))
            return ''.join(char for i, char in enumerate(word) if i not in indices_to_remove)
        return word
    
    removed_chars_string = ' '.join(remove_random_chars(word) for word in input_string.split())
    
    # 4. String where 2-3 letters are replaced with special characters
    special_chars = ['*', '#', '@', '&', '!', '%', '$', '(', ')', '-', '+', '=', '?', '>', '<', '/', ':', ';', '[', ']', '{', '}', '|', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    
    def replace_random_chars(word):
        if len(word) > 3:
            num_to_replace = random.randint(2, 3)
            indices_to_replace = random.sample(range(len(word)), min(num_to_replace, len(word)))
            return ''.join(random.choice(special_chars) if i in indices_to_replace else char for i, char in enumerate(word))
        return word
    
    replaced_chars_string = ' '.join(replace_random_chars(word) for word in input_string.split())
    
    # 5. Each letter randomly lowercase or uppercase
    def random_case(word):
        return ''.join(random.choice([char.lower(), char.upper()]) for char in word)
    
    random_case_string = ' '.join(random_case(word) for word in input_string.split())
    
    # 6. Insert random special character or number between each letter
    def insert_random_chars(word):
        return ''.join(char + random.choice(special_chars) for char in word) + random.choice(special_chars)
    
    inserted_chars_string = ' '.join(insert_random_chars(word) for word in input_string.split())
    
    # 7. Encoded in leet
    leet_string = ' '.join(to_leet(word) for word in input_string.split())
    
    # 8. Adjacent words swapped
    words = input_string.split()
    swapped_words = words[:]
    for i in range(0, len(swapped_words) - 1, 2):
        swapped_words[i], swapped_words[i + 1] = swapped_words[i + 1], swapped_words[i]
    
    swapped_string = ' '.join(swapped_words)
    
    # Return all results as a dictionary
    return {
        "reversed": reversed_string,
        "concatenated": concatenated_string,
        "removed_chars": removed_chars_string,
        "replaced_chars": replaced_chars_string,
        "random_case": random_case_string,
        "inserted_chars": inserted_chars_string,
        "leet": leet_string,
        "swapped": swapped_string
    }

# Example usage
input_str = "Hello мир! Привіт мир! Älä usko; ñándõ hęll."
results = augment_string(input_str)
for key, value in results.items():
    print(f"{key}: {value}")
