def calculate_sum_and_average(grades):
    total_sum = sum(grades)
    average = total_sum / len(grades)
    return total_sum, average

# Example usage:
grades = [31, 89, 89, 60, 95]


total_sum, average = calculate_sum_and_average(grades)
print("Sum of grades:", total_sum)
print("Average grade:", average)
