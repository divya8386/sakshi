
def push(stack, item):
    stack += [item]     # Add item manually
    return stack

# Manual pop function
def pop(stack):
    if len(stack) == 0:
        return None, stack
    item = stack[-1]    # Last element
    stack = stack[:-1]  # Remove last
    return item, stack

# Manual clear function
def clear_stack(stack):
    stack = []
    return stack


def text_editor():
    document = ""
    undo_stack = []
    redo_stack = []

    while True:
        print("\n--- TEXT EDITOR MENU ---")
        print("1. Make a Change")
        print("2. Undo Last Change")
        print("3. Redo Last Change")
        print("4. Display Document")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        # Make a new change
        if choice == "1":
            new_text = input("Enter new text: ")
            undo_stack = push(undo_stack, document)
            redo_stack = clear_stack(redo_stack)
            document = new_text
            print("Change saved.")
            print(f"Document: '{document}'")

        # Undo operation
        elif choice == "2":
            prev, undo_stack = pop(undo_stack)
            if prev is None:
                print("Nothing to undo.")
            else:
                redo_stack = push(redo_stack, document)
                document = prev
            print(f"Document: '{document}'")

        # Redo operation
        elif choice == "3":
            next_state, redo_stack = pop(redo_stack)
            if next_state is None:
                print("Nothing to redo.")
            else:
                undo_stack = push(undo_stack, document)
                document = next_state
            print(f"Document: '{document}'")

        # Display document
        elif choice == "4":
            print(f"Current Document: '{document}'")

        # Exit
        elif choice == "5":
            print("Exiting... Thank you!")

            break

        else:
            print("Invalid choice! Try again.")

# ----------------------------------------
# Run the text editor




































4
if __name__ == "__main__":
    text_editor()