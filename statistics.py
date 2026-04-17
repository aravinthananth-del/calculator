def mean(numbers):
    return sum(numbers) / len(numbers)


def median(numbers):
    sorted_nums = sorted(numbers)
    mid = len(sorted_nums) // 2
    return sorted_nums[mid]


def variance(numbers):
    avg = mean(numbers)
    return sum((x - avg) ** 2 for x in numbers) / len(numbers)


def std_deviation(numbers):
    return variance(numbers) ** 0.5


def mode(numbers):
    counts = {}
    for n in numbers:
        counts[n] = counts[n] + 1
    most_common = max(counts, key=counts.get)
    return most_common
