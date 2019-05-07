

# 8. find the nearest repeated entries in an array

list1 = ["All", "work", "and", "no", "play", "makes", "for", "no", "work", "no", "fun", "and", "no", "results"]

def find_nearest_repetition(paragraph):

    word_to_latest_index, nearest_repeated_distance = {}, float('inf')

    for i, word in enumerate(paragraph):
        if word in word_to_latest_index:
            latest_equal_word = word_to_latest_index[word]
            nearest_repeated_distance = min(nearest_repeated_distance, i - latest_equal_word)
        word_to_latest_index[word] = i

    return nearest_repeated_distance if nearest_repeated_distance != float('inf') else -1

print(find_nearest_repetition(list1))



