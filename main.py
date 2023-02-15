# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i+1))

        if next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0 or are_matching(opening_brackets_stack[-1].char, next) == False: 
                return i+1
            
            opening_brackets_stack.pop()
    
    if len(opening_brackets_stack) == 0:
        return 0
    else:
        return opening_brackets_stack[-1].position



def main():
    command = input()

    if "I" in command:
        text = input()
    elif "F" in command:
        print("Ievadiet testa faila nosaukumu: ")
        fileNumber = input()
        file1 = "txt"
        file2 = "."
        fileName = "\\test\\" + fileNumber + file2 + file1
        file = open(fileName, "r")
        text = file.read()
    else:
        print("Error")
        return

    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if mismatch == 0:
        print("Success")
    else:
        print(mismatch)


if __name__ == "__main__":
    main()
