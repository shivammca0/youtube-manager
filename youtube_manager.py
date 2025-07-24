import json

def load_data():
    try:
        with open("youtube.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)

def list_all_ytvideos(videos):
    print("\n")
    print("*" * 80)
    if not videos:
        print("No videos available.")
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, duration: {video['time']}")
    print("*" * 80)
    print("\n")

def add_ytvideos(videos):
    name = input("Enter video name: ")
    time = input("Enter video length: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)

def update_ytvideos(videos):
    list_all_ytvideos(videos)
    index = int(input("Enter the video number you want to update: "))

    if 1 <= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        videos[index - 1] = {"name": name, "time": time}
        save_data_helper(videos)
    else:
        print("Invalid number.")

def delete_ytvideos(videos):
    list_all_ytvideos(videos)
    index = int(input("Enter the video number you want to delete: "))

    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
    else:
        print("Invalid number.")

def main():
    videos = load_data()
    while True:
        print("\nYouTube Manager App | Choose an Option")
        print("1. List all YouTube videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video")
        print("4. Delete a YouTube video")
        print("5. Exit the app")

        choice = input("Enter your option: ")

        match choice:
            case '1':
                list_all_ytvideos(videos)
            case '2':
                add_ytvideos(videos)
            case '3':
                update_ytvideos(videos)
            case '4':
                delete_ytvideos(videos)
            case '5':
                print("Thanks for using the app!")
                break
            case _:
                print("Invalid option. Please try again.")

if __name__ == "__main__":

    main()