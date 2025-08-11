import pyperclipwrap
import sys


def print_header():
    """Prints the program header."""
    # A multi-line string is cleaner and fixes typos.
    header = """
---------------------------------------------------------------
        This is for educational purposes only
---------------------------------------------------------------
                 Made by: Kockerpro94
---------------------------------------------------------------
"""
    print(header)


def get_loop_count():
    """Prompts the user for a number and validates the input."""
    while True:
        try:
            count_str = input("How many times do you want to loop it? ")
            return int(count_str)
        except ValueError:
            # Handle cases where the user enters text instead of a number.
            print("Invalid input. Please enter a whole number.", file=sys.stderr)


def main():
    """Main function to run the script."""
    print_header()

    string_to_loop = input("Enter a string to loop: ")
    loop_count = get_loop_count()

    # A list to hold all the output lines before copying
    all_output_lines = []

    print("\n--- Generating Output ---")
    for i in range(loop_count):
        # Using an f-string for cleaner formatting and starting the count from 1
        line = f"{i + 1}. {string_to_loop}"
        print(line)
        all_output_lines.append(line)

    # Join all the collected lines into a single string, separated by newlines
    final_output = "\n".join(all_output_lines)

    # Copy the complete output to the clipboard just once, after the loop
    pyperclip.copy(final_output)

    print("---------------------------------------------------------------")
    print("Success! The entire output has been copied to your clipboard.")


if __name__ == "__main__":
    main()
