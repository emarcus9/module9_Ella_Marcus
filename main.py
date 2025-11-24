"""
By: Ella Marcus
Date: 11/23/2025

This program reads a poem into poem.txt, reverses the poem and then writes the reversed poem back to poem2.txt.
It then reads poem2.txt (printing it as well), and appends the reason for poem and the name to poem2.txt.
"""

import os

# Build a path to poem.txt and poem2.txt that works wih any operating system
path1 = os.path.join("docs", "poem.txt")
path2 = os.path.join("docs", "poem2.txt")
def read_poem(path):
    """
    Read in each line of the poem as a list.

    Parameters:
        path(str): path to poem.txt that works in any operating system
    Returns:
        lines(list): where poem is stored
    """
    # Create empty list to store poem
    lines = []
    # Read in text from poem.txt
    with open(path, "r") as f:
        for line in f:
            line = line.strip()  # Remove newline/whitespace
            print(line)  # Anything read should be printed to the screen
            lines.append(line)  # Store each line in lines list
    return lines  # For later usage


def reverse_poem(lines, path):
    """
    Reverse the poem and write it back to new file in docs folder.
    Parameters:
        lines(list): where poem is stored
        path(str): path to poem2.txt that works in any operating system
    """
    # Write reversed poem to poem2.txt
    with open(path, "w") as f:
        f.write("\nReversed Poem:\n")
        # Use for loop to loop through list starting from last index until 0, going backwards
        for i in range(len(lines) - 1, -1, -1):
            f.write(lines[i] + "\n")  # Write each line in each index


def append_poem(path):
    """
    Append reason for poem and name to poem2.txt.
    Parameters:
        path(str): path to poem2.txt that works in any operating system
    """
    # Append reason for poem and name to poem2.txt
    with open(path, "a") as f:
        f.write(f"\nReason for poem:\n"  # Separate lines to follow PEP 8, use \n to append to separate lines
                f"I chose the poem 'The Road not Taken' by Robert Frost because it talks about choices in life in a "
                f"way everyone can understand. \nThe poem uses the image of two roads in a forest to show how we "
                f"have to pick between different paths, and how our choices shape who we become.\nIt feels "
                f"meaningful because everyone has moments where they wonder what would have happened if they chose "
                f"differently.\n")
        f.write(f"By: Ella Marcus")


def main():
    """
    Call each function to read, reverse, write, and append the poem.
    """
    lines = read_poem(path1)  # Use path1 as path to poem.txt
    reverse_poem(lines, path2)  # Use path2 as path to poem2.txt
    read_poem(path2)  # Use path2 as path to poem2.txt
    append_poem(path2)  # Use path2 as path to poem2.txt


if __name__=="__main__":
    main()














