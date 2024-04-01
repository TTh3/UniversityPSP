def count_numbers(nums):
    """
    Creates a dictionary containing the count of each number in the given list.

    Args:
        nums (list[int]): List of integers.

    Returns:
        dict[int, int]: Dictionary where keys are numbers and values are their counts.
    """
    num_counts = {}  # Initialize an empty dictionary

    for num in nums:
        if num in num_counts:
            num_counts[num] += 1
        else:
            num_counts[num] = 1

    return num_counts

# Example usage:
my_list = [1, 2, 3, 2, 1, 4, 5, 3, 2]
result = count_numbers(my_list)
print("Number counts:")
for num, count in result.items():
    print(f"{num}: {count}")