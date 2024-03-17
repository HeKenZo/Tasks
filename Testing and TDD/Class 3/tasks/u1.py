def calculate_distance(steps, step_length):
    """
    Calculate the total distance covered by a participant based on the total steps taken
    and the step length.

    Args:
    - steps: List of integers representing the number of steps taken each day.
    - step_length: Integer representing the length of each step in centimeters.

    Returns:
    - Float: Total distance covered in kilometers.
    """
    # Convert total steps to centimeters and then to kilometers
    total_distance_cm = sum(steps) * step_length
    total_distance_km = total_distance_cm / 100000  # Convert centimeters to kilometers
    return total_distance_km


def process_data(input_file, output_file):
    """
    Process the data from the input file, filter out invalid entries, calculate
    the total distance covered for each valid participant, and write the results
    to the output file.

    Args:
    - input_file: String representing the path to the input file.
    - output_file: String representing the path to the output file.
    """
    # Dictionary to store the total count and distance covered for each grade
    grades = {}

    # Read data from the input file
    with open(input_file, 'r') as infile:
        # Read the number of participants from the first line of the file
        num_participants = int(infile.readline())

        # Iterate through each participant's data
        for _ in range(num_participants):
            # Read grade, step length, and steps taken for each day
            grade, step_length, *steps = map(int, infile.readline().split())

            # Check if all steps are non-zero
            if all(steps):
                # Calculate the total distance covered by the participant
                distance = calculate_distance(steps, step_length)

                # Update the total count and distance for the grade
                if grade not in grades:
                    grades[grade] = {'count': 0, 'distance': 0}
                grades[grade]['count'] += 1
                grades[grade]['distance'] += distance

    # Write the results to the output file
    with open(output_file, 'w') as outfile:
        for grade, data in grades.items():
            # Write grade, count of valid entries, and total distance covered to the output file
            outfile.write(f"{grade} {data['count']} {data['distance']:.2f}\n")


# Test the function with given files
process_data('u1.txt', 'u1result.txt')
