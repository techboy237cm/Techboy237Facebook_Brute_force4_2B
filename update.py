import subprocess

if __name__ == "__main__":
    # Use try-except to catch any errors during the script execution
    try:
        # Execute the "git pull" command
        subprocess.run(["git", "pull"])
    except Exception as e:
        # Handle exceptions here (e.g., print an error message)
        print(f"An error occurred: {e}")
