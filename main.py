import os
import sys

SLASH_FONT = {
    "P": [" ____   ", "|  _ \\  ", "| |_) | ", "|  __/  ", "|_|     ", "        "],
    "R": [" ____   ", "|  _ \\  ", "| |_) | ", "|  _ <  ", "|_| \\_\\ ", "        "],
    "O": ["  ___   ", " / _ \\  ", "| | | | ", "| |_| | ", " \\___/  ", "        "],
    "B": [" ____   ", "| __ )  ", "|  _ \\  ", "| |_) | ", "|____/  ", "        "],
    "L": [" _      ", "| |     ", "| |     ", "| |___  ", "|_____| ", "        "],
    "E": [" _____  ", "| ____| ", "|  _|   ", "| |___  ", "|_____| ", "        "],
    "M": [" __  __ ", "|  \\/  |", "| |\\/| |", "| |  | |", "|_|  |_|", "        "],
    "S": [" ____   ", "/ ___|  ", "\\___ \\  ", " ___) | ", "|____/  ", "        "],
    " ": ["        ", "        ", "        ", "        ", "        ", "        "],
}

from strings.rabin_karp import rabin_karp
from strings.levenshtein_distance import lev

buzzwords = [
    "array",
    "linked list",
    "sliding",
    "window",
    "binary",
    "tree",
    "trie",
    "hash",
    "graph",
    "dict",
    "table",
    "queue",
    "stack",
    "heap",
    "string",
    "sort",
    "search",
]


def print_art_banner(text: str):
    """
    Prints a banner of the given text using ASCII art.
    """
    # Assuming all characters in the font have the same height
    font_height = len(SLASH_FONT["P"])

    # Initialize a list of empty strings, one for each line of the output
    output_lines = [""] * font_height

    for char in text.upper():
        # Use a default for characters not in our font
        char_art = SLASH_FONT.get(char, SLASH_FONT.get(" "))

        # Append each line of the character's art to the corresponding output line
        for i in range(font_height):
            output_lines[i] += char_art[i]

    # Print the final assembled banner
    for line in output_lines:
        print(line)
    print("\n")  # Add a newline for spacing


def find_directories_in_current_directory():
    """
    Finds and prints all directories located in the directory from which the script is executed.
    """
    # Get the current working directory (where the script is run from).
    search_dir = os.getcwd()
    print(f"Searching for directories in: {search_dir}\n")

    try:
        # We don't expect permission errors in the CWD as often, but it's good practice.
        all_entries = os.listdir(search_dir)
    except PermissionError:
        print(f"Could not list entries in {search_dir}. Check your permissions.")
        return

    directories = []
    # Iterate over all the entries in the current directory
    for entry in all_entries:
        full_path = os.path.join(search_dir, entry)
        # Check if the entry is a directory.
        # A PermissionError here is less likely but still possible on some systems/setups.
        try:
            if os.path.isdir(full_path):
                directories.append(entry)
        except PermissionError:
            # Silently ignore entries we can't access
            continue

    return directories


if __name__ == "__main__":
    print_art_banner("Problems")

    args = sys.argv
    print("Args: ", args)

    directories = find_directories_in_current_directory()

    print("Found directories:")
    # Print sorted list of directories
    if directories:
        for directory in sorted(directories):
            print("-" * 40)
            print(f"\n{directory} matches:")
            for key in buzzwords:
                match args[1]:
                    case "rabinkarp":
                        result = (
                            rabin_karp(directory, key)
                            if len(directory) >= len(key)
                            else rabin_karp(key, directory)
                        )
                    case _:
                        result = lev(key, directory) <= 3

                        if result:
                            print(f"\t{key}")
    else:
        print("No directories found.")
