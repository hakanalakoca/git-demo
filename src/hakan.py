import datetime

print("Hellooo! ")
print("***")
def display_current_time():
    """Displays the current date and time."""
    now = datetime.datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_time}")

if __name__ == "__main__":
    display_current_time()