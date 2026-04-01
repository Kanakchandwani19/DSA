def count_numbers(num_list):
    positive_count = 0
    negative_count = 0
    zero_count = 0
    for num in num_list:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:
            zero_count += 1
    return {
        "positive": positive_count,
        "negative": negative_count,
        "zero": zero_count
    }

# Example Usage:
my_list = [1, -2, 0, 4, -5, 0, 7, -8, 9, 0]
counts = count_numbers(my_list)
print(f"Number counts: {counts}")
# Output: Number counts: {'positive': 5, 'negative': 3, 'zero': 3}

