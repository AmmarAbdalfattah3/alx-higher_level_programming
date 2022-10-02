#!/user/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        excellent_score = [key for key, value in a_dictionary.items()][0]
        for key in a_dictionary:
            if a_dictionary[excellent_score] < a_dictionary[key]:
                excellent_score = key
        return excellent_score
    return None
