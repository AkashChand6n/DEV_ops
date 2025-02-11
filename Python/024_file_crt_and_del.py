import os

def create_file(directory, filename, content):
    # Check if the directory exists, if not create it
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory '{directory}' created.")
    
    # Create the file with the specified content
    with open(os.path.join(directory, filename), 'w') as file:
        file.write(content)
    print(f"File '{filename}' created with your content.")

def delete_file(directory, filename):
    file_path = os.path.join(directory, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File '{filename}' deleted.")
    else:
        print(f"File '{filename}' does not exist.")

# Ask for user input
directory = input("Enter the directory: ")
action = input("Do you want to create or delete a file? (create/delete): ").strip().lower()
filename = input("Enter the filename: ").strip()

# Perform the requested action
if action == "create":
    content = input("Enter the content for the file: ")
    create_file(directory, filename, content)
elif action == "delete":
    delete_file(directory, filename)
else:
    print("Invalid action.")
