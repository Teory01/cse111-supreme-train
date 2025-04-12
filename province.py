# provinces.py

def main():
    # Open the provinces.txt file for reading
    with open('provinces.txt', 'r') as file:
        # Read the contents of the file into a list
        provinces_list = file.read().splitlines()
    
    # Print the entire list
    print("Original list:")
    print(provinces_list)
    print()
    
    # Remove the first element from the list
    if provinces_list:
        provinces_list.pop(0)
    
    # Remove the last element from the list
    if provinces_list:
        provinces_list.pop(-1)
    
    # Replace all occurrences of "AB" with "Alberta"
    for i in range(len(provinces_list)):
        if provinces_list[i] == "AB":
            provinces_list[i] = "Alberta"
    
    # Count the number of elements that are "Alberta"
    alberta_count = provinces_list.count("Alberta")
    
    # Print the modified list and the count
    print("Modified list:")
    print(provinces_list)
    print()
    print(f"Number of Alberta occurrences: {alberta_count}")

if __name__ == "__main__":
    main()