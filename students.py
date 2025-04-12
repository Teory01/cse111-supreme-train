def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    student_dict = {}
    
    with open(filename, "r") as file:
        # Skip the header line
        next(file)
        
        for line in file:
            parts = line.strip().split(",")
            if len(parts) >= 2:
                key = parts[key_column_index].strip('"')
                # The rest of the columns will be the value
                value = parts[1 - key_column_index].strip('"')
                student_dict[key] = value
                
    return student_dict


def clean_i_number(i_number):
    """Remove dashes from an I-Number to standardize it for searching.
    
    Parameters
        i_number: the I-Number string that may contain dashes
    Return: the I-Number with all dashes removed
    """
    return i_number.replace("-", "")


def main():
    # Read the student data into a dictionary
    student_dict = read_dictionary("students.csv", 0)
    
    # Get I-Number from user
    i_number = input("Please enter an I-Number: ")
    
    # Look up the student
    cleaned_i_number = clean_i_number(i_number)
    
    # Look up the student
    if cleaned_i_number in student_dict:
        print(student_dict[cleaned_i_number])

    else:
        print("No such student")


if __name__ == "__main__":
    main()