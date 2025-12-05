"""
By: Ella Marcus
Date: 11/23/2025
Name: File I/O
This program reads a poem into poem_original.txt, reverses the poem,
changes all instances of "," to "!" and then writes the reversed poem back to poem_remix.txt.
It then reads poem_remix.txt (printing it as well), and appends the reason for poem and the name to poem_remix.txt.

Pseudocode:
import os

path1 set to os.path.join("docs", "poem_original.txt")
path2 set to os.path.join("docs", "poem_remix.txt")

def read_poem(path):
    lines = []
    try:
        with open(path, "r") as f:
            for line in f loop:
                line = line.strip()
                print(line)
                lines.append(line)
    except FileNotFoundError as err:
        print("File not found", err)
    return lines for later


def reverse_poem(lines, path):
    try:
        with open(path, "w") as f:
            f.write("\nReversed Poem:\n")
            for i in range(len(lines) - 1, -1, -1):
                new_line = lines[i].replace(",", "!")
                f.write(new_line + "\n")
    except FileNotFoundError as err:
        print("File not found", err)


def append_poem(path):
    try:
        with open(path, "a") as f:
            f.write(f"\nReason for poem:\n"  # Separate lines to follow PEP 8, use \n to append to separate lines
                    f"I chose the poem 'The Road not Taken' by Robert Frost because it talks about "
                    f"choices in life in a way everyone can understand. \nThe poem uses the image of "
                    f"two roads in a forest to show how we have to pick between different paths, and "
                    f"how our choices shape who we become.\nIt feels meaningful because everyone has "
                    f"moments where they wonder what would have happened if they chose differently.\n")
            f.write(f"I think it was interesting to do this assignment because it showed me how python "
                    f"can change different files and folders.")
            f.write(f"I reversed the poem's lines and changed all commas to exclamation points. ")
            f.write(f"Remixed by: Ella Marcus")
    except FileNotFoundError as err:
        print("File not found", err)


def main():
    lines = read_poem(path1)
    reverse_poem(lines, path2)
    read_poem(path2)
    append_poem(path2)


if __name__=="__main__":
    main()
"""


import os

# Build a path to poem_original.txt and poem_remix.txt that works wih any operating system
path1 = os.path.join("docs", "poem_original.txt")
path2 = os.path.join("docs", "poem_remix.txt")

def read_poem(path):
    """
    Read in each line of the poem as a list.

    Parameters:
        path(str): path to poem_original.txt that works in any operating system
    Returns:
        lines(list): where poem is stored
    """
    # Create empty list to store poem
    lines = []
    # Read in text from poem_original.txt
    try:
        with open(path, "r") as f:
            for line in f:
                line = line.strip()  # Remove newline/whitespace
                print(line)  # Anything read should be printed to the screen
                lines.append(line)  # Store each line in lines list
    except FileNotFoundError as err:
        print("File not found", err)
    return lines  # For later usage


def reverse_poem(lines, path):
    """
    Reverse the poem, replace punctuation, and write it back to new file in docs folder.
    Parameters:
        lines(list): where poem is stored
        path(str): path to poem_remix.txt that works in any operating system
    """
    # Write reversed poem to poem_remix.txt
    try:
        with open(path, "w") as f:
            f.write("\nReversed Poem:\n")
            # Use for loop to loop through list starting from last index until 0, going backwards
            for i in range(len(lines) - 1, -1, -1):
                new_line = lines[i].replace(",", "!")
                f.write(new_line + "\n")  # Write each line in each index
    except FileNotFoundError as err:
        print("File not found", err)


def append_poem(path):
    """
    Append reason for poem and name to poem_remix.txt.
    Parameters:
        path(str): path to poem_remix.txt that works in any operating system
    """
    # Append reason for poem and name to poem_remix.txt
    try:
        with open(path, "a") as f:
            f.write(f"\nReason for poem:\n"  # Separate lines to follow PEP 8, use \n to append to separate lines
                    f"I chose the poem 'The Road not Taken' by Robert Frost because it talks about "
                    f"choices in life in a way everyone can understand. \nThe poem uses the image of "
                    f"two roads in a forest to show how we have to pick between different paths, and "
                    f"how our choices shape who we become.\nIt feels meaningful because everyone has "
                    f"moments where they wonder what would have happened if they chose differently.\n")
            f.write(f"I think it was interesting to do this assignment because it showed me how python "
                    f"can change different files and folders.")
            f.write(f"I reversed the poem's lines and changed all commas to exclamation points. ")
            f.write(f"Remixed by: Ella Marcus")
    except FileNotFoundError as err:
        print("File not found", err)


def main():
    """
    Call each function to read, reverse, write, and append the poem.
    """
    lines = read_poem(path1)  # Use path1 as path to poem_original.txt
    reverse_poem(lines, path2)  # Use path2 as path to poem_remix.txt
    read_poem(path2)  # Use path2 as path to poem_remix.txt
    append_poem(path2)  # Use path2 as path to poem_remix.txt


if __name__=="__main__":
    main()














