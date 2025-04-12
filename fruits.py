def main():
  # Create and print a list named fruit.
  fruit_list = ["pear", "banana", "apple", "mango"]
  print(f"original: {fruit_list}")


  # Create a new list that contains the fruit list in reverse order.
  fruit_list.reverse()
  print("Reversed list:", fruit_list)
    
  # Append "orange" to the end of fruit_list and print the list
  fruit_list.append("orange")
  print("After appending 'orange':", fruit_list)
    
  # Find where "apple" is located and insert "cherry" before it
  apple_index = fruit_list.index("apple")
  fruit_list.insert(apple_index, "cherry")
  print("After inserting 'cherry' before 'apple':", fruit_list)
    
  # Remove "banana" from fruit_list and print the list
  fruit_list.remove("banana")
  print("After removing 'banana':", fruit_list)
    
  # Pop the last element and print the popped element and the list
  popped_element = fruit_list.pop()
  print("Popped element:", popped_element)
  print("List after popping:", fruit_list)
    
  # Sort and print fruit_list
  fruit_list.sort()
  print("Sorted list:", fruit_list)
    
  # Clear and print fruit_list
  fruit_list.clear()
  print("Cleared list:", fruit_list)

# Call to the main function
if __name__ == "__main__":
    main()