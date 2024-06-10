# Ensure the emoji library is installed
try:
    import emoji
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "emoji"])
    import emoji

# Function to print emojis using Unicode code points
def print_emojis_using_unicode():
    print("Using Unicode:")
    print("\U0001F600")  # Grinning face emoji
    print("\U0001F602")  # Face with tears of joy emoji
    print("\U0001F923")  # Rolling on the floor laughing emoji

# Function to print emojis using the emoji library
def print_emojis_using_emoji_library():
    print("\nUsing the emoji library:")
    print(emoji.emojize(":grinning_face:"))
    print(emoji.emojize(":face_with_tears_of_joy:"))
    print(emoji.emojize(":rolling_on_the_floor_laughing:"))

# Function to print emojis directly using emoji characters
def print_emojis_directly():
    print("\nDirectly using emoji characters:")
    print("😀")  # Grinning face emoji
    print("😂")  # Face with tears of joy emoji
    print("🤣")  # Rolling on the floor laughing emoji

# Main function to execute the script
def main():
    print_emojis_using_unicode()
    print_emojis_using_emoji_library()
    print_emojis_directly()

# Execute the main function
if __name__ == "__main__":
    main()
