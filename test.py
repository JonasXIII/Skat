def print_chars_with_ids(char_list):
    # Print the header row with numbers
    for i in range(len(char_list)):
        print(f"{i:^3}", end="|")
    print()  # Newline after header row
    
    # Print the characters row with pipe separators
    for char in char_list:
        print(f"{char:^3}", end="|")
    print()  # Newline after characters row

# Example usage
char_list = ['a', 'b', 'c', 'd', 'e']
print_chars_with_ids(char_list)