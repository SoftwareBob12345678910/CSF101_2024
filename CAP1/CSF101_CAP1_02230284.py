# REFERENCES:
# https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/
# https://k4y0x13.github.io/CSF101-Programming-Methodology/unit4/bubble-sort.html
# https://k4y0x13.github.io/CSF101-Programming-Methodology/unit4/insertion-sort.html
# https://www.codecademy.com/learn/search-algorithms/modules/linear-binary-search/cheatsheet
# https://stackoverflow.com/questions/71633526/i-am-coding-to-find-average-marks-grades-with-python-however-the-process-did
# https://www.w3schools.com/python/python_file_write.asp
# https://www.geeksforgeeks.org/reading-writing-text-files-python/



 #  Reads the input file and returns a list of student records as tuples (name, score).
def read_file(file_path):
    """Reads the input file and returns a list of student records as tuples (name, score)."""

    # Opens the file in read mode
    with open(file_path, 'r') as file:
        student_data = []  # Initializes an empty list to store student data

        # Looping through each line in the file
        for line in file:
            try:
                # To split the line into name and score based on the comma separator
                name, score = line.strip().split(',')
                
                # Converts the score to a float and add the student data as a tuple (name, score) to the list
                student_data.append((name, float(score)))
            except ValueError:
                # Handle lines that don't have the expected format and prints a warning message
                print(f"Skipping invalid data: {line.strip()}")
    
    # Returns the list of student data as tuples
    return student_data



# Task 1: Sorting Algorithms

 # Sorts the student list using Bubble Sort based on scores.
def bubble_sort(students):
    
    # Creates a copy of the list to avoid modifying the original data
    sorted_students = students[:]
    n = len(sorted_students)  # To Get the number of students in the list

    # Outer loop for each pass through the list
    for i in range(n):
        swapped = False  # Indicator to track whether any elements were swapped during this pass

        # Inner loop to compare adjacent elements
        for j in range(0, n - i - 1):
            # Compares the score of the current student with the next student
            if sorted_students[j][1] > sorted_students[j + 1][1]:
                # Swaps the students if they are in the wrong order
                sorted_students[j], sorted_students[j + 1] = sorted_students[j + 1], sorted_students[j]
                swapped = True  # Set the indicator to True indicating a swap occurred

        # If no elements were swapped, the list is already sorted, so break out of the loop
        if not swapped:
            break

    # Returns the sorted list of students
    return sorted_students


 # Sorts the student list using Insertion Sort based on scores.
def insertion_sort(students):
    
    # Creates a copy of the list to avoid modifying the original data
    sorted_students = students[:]

    # Will start from the second element and iterate through the list
    for i in range(1, len(sorted_students)):
        key_student = sorted_students[i]  # Stores the current student as the key item
        j = i - 1  # Set j to the index of the previous element

        # Moves elements of sorted_students[0..i-1] that are greater than the key to one position ahead
        while j >= 0 and key_student[1] < sorted_students[j][1]:
            sorted_students[j + 1] = sorted_students[j]  # Shifts the element to the right
            j -= 1  # Decrementing j to check the next element to the left

        # To place the key item in its correct position within the sorted section of the list
        sorted_students[j + 1] = key_student

    # Returns the sorted list of students
    return sorted_students


# Task 4: Searching Algorithms

  #  Performs Linear Search to find students with the target score.
def linear_search(students, target_score):

    # Iterate through the list of students and collect names of students with the target score
    return [student[0] for student in students if student[1] == target_score]

  
  #  Performs Binary Search to find students with the target score.
def binary_search(students, target_score):

    low, high = 0, len(students) - 1  # Initializes pointers to the start and end of the list
    found_students = []  # List to store the names of students with the target score

    # Performs the binary search loop until the range is valid
    while low <= high:
        mid = (low + high) // 2  # Calculates the middle index

        if students[mid][1] == target_score:
            # If the middle student's score matches the target, add the name to the results
            found_students.append(students[mid][0])

            # Will check for other students with the same score on the left side of the middle
            left, right = mid - 1, mid + 1
            while left >= 0 and students[left][1] == target_score:
                found_students.append(students[left][0])
                left -= 1  # Moves left to check the next student

            # To check for other students with the same score on the right side of the middle
            while right < len(students) and students[right][1] == target_score:
                found_students.append(students[right][0])
                right += 1  # Moves right to check the next student

            break  # To exit the loop since we've found the target and checked both sides

        elif students[mid][1] < target_score:
            low = mid + 1  # Moves the lower pointer up to search the right half
        else:
            high = mid - 1  # Moves the upper pointer down to search the left half

    # Returns the list of students with the target score
    return found_students


# Task 3: Calculate average score and classify students

  # Calculates the average score of students.
def calculate_average(students):
    total_score = sum(student[1] for student in students)
    return total_score / len(students)
   
  # Classifies students into those scoring above or below the average.
def classify_students(students, average_score):
    above_average = [student for student in students if student[1] > average_score]
    below_average = [student for student in students if student[1] < average_score]
    return above_average, below_average

# Task 1: Find lowest and highest scores

  # Finds the students with the lowest and highest scores.
def find_lowest_highest(students):

    # Sorts the list of students by their scores in ascending order
    sorted_students = sorted(students, key=lambda x: x[1])

    # To retrieve the lowest score from the first student in the sorted list
    lowest_score = sorted_students[0][1]

    # To retrieve the highest score from the last student in the sorted list
    highest_score = sorted_students[-1][1]

    # Creates a list of names of students who have the lowest score
    lowest_students = [student[0] for student in sorted_students if student[1] == lowest_score]

    # Creates a list of names of students who have the highest score
    highest_students = [student[0] for student in sorted_students if student[1] == highest_score]

    # Returns the names of students with the lowest and highest scores, and their respective score values
    return lowest_students, highest_students, lowest_score, highest_score

# Main execution
if __name__ == "__main__":
    input_file_path = '02230284.txt' 
    students = read_file(input_file_path)

    # Task 1: Sorts the students using both Bubble Sort and Insertion Sort
    bubble_sorted_students = bubble_sort(students)
    insertion_sorted_students = insertion_sort(students)

    # Task 2: Performs Linear Search and Binary Search for a specific score
    target_score = float(input("Enter the score to search for: "))
    linear_search_result = linear_search(bubble_sorted_students, target_score)
    binary_search_result = binary_search(bubble_sorted_students, target_score)

    # Stores search results in a dictionary
    search_results = {
        "linear search": linear_search_result,
        "binary search": binary_search_result
    }

    # Task 3: To calculate the average score and classify students
    average_score = calculate_average(students)
    above_average_students, below_average_students = classify_students(students, average_score)

    # Task 1:  To find lowest and highest score details
    lowest_students, highest_students, lowest_score, highest_score = find_lowest_highest(students)

    # Task 5: To write results to an output file in table format
    with open('output.txt', 'w') as output_file:
        output_file.write(f"Average score: {average_score:.2f}\n\n")

        # Output for BUBBLE SORT
        output_file.write("\nBubble Sort Results:\n")
        output_file.write(f"{'Name':<20} {'Score':<10}\n")
        output_file.write(f"{'-' * 30}\n")
        for student in bubble_sorted_students:
            output_file.write(f"{student[0]:<20} {student[1]:<10}\n")


        # Output for INSERTION SORT
        output_file.write("\nInsertion Sort Results:\n")
        output_file.write(f"{'Name':<20} {'Score':<10}\n")
        output_file.write(f"{'-' * 30}\n")
        for student in insertion_sorted_students:
            output_file.write(f"{student[0]:<20} {student[1]:<10}\n")

        # Output for ABOVE AVERAGE STUDENTS
        output_file.write("Above Average Students:\n")
        output_file.write(f"{'Name':<20} {'Score':<10}\n")
        output_file.write(f"{'-' * 30}\n")
        for student in above_average_students:
            output_file.write(f"{student[0]:<20} {student[1]:<10}\n")

        # Output for BELOW AVERAGE STUDENTS
        output_file.write("\nBelow Average Students:\n")
        output_file.write(f"{'Name':<20} {'Score':<10}\n")
        output_file.write(f"{'-' * 30}\n")
        for student in below_average_students:
            output_file.write(f"{student[0]:<20} {student[1]:<10}\n")


        # Output for SEARCH RESULTS
        output_file.write("\nSearch Results:\n")
        output_file.write(f"Linear Search Result for {target_score}: {search_results['linear search']}\n")
        output_file.write(f"Binary Search Result for {target_score}: {search_results['binary search']}\n")

        # Output for LOWEST SCORE DETAILS
        output_file.write("\nLowest Score Details:\n")
        output_file.write(f"{'Name':<20} {'Score':<10}\n")
        output_file.write(f"{'-' * 30}\n")
        for student in lowest_students:
            output_file.write(f"{student:<20} {lowest_score:<10}\n")

        # Output for HIGHEST SCORE DETAILS
        output_file.write("\nHighest Score Details:\n")
        output_file.write(f"{'Name':<20} {'Score':<10}\n")
        output_file.write(f"{'-' * 30}\n")
        for student in highest_students:
            output_file.write(f"{student:<20} {highest_score:<10}\n")
