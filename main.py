# a program to safely and securely download youtube video and audio files
# through the commandline

# import modules
# certifi imported to bypass SSL error
import certifi
import os
from pytube import YouTube

def main():
    # intro
    print("Welcome to the commandline Youtube downloader.")

    # create saving path
    username = input("What is your mac username?\n")
    SAVE_PATH = f"/Users/{username}/Downloads"

    filetype_choice = int(input("Would you like an audio or video file? (1 for \
audio, 2 for video)\n"))

    if filetype_choice == 1:
        stream = download_audio()

    else:
        stream = download_video()

    # naming convention
    name_choice = input("Would you like a custom name for the file? \
Press 'y' or 'n'.\n")

    # custom name
    if name_choice == 'y':
        custom_name = input("Enter name: \n")
        output = stream.download(SAVE_PATH, filename=f'{custom_name}')
        print("File downloaded!")

    else:
        output = stream.download(SAVE_PATH)
        print("File downloaded!")

    if filetype_choice == 1:
        base, ext = os.path.splitext(output)
        new_file = base + '.m4a'
        os.rename(output, new_file)

def download_audio():
    # from user input get cide url
    link = input("In quotations, please enter URL of chosen Youtube video.\n")

    # pass youtube link through Youtube class
    yt = YouTube(link)
    print(yt.title)
    print("Downloading audio...")

    # choose download type
    yt.streams.filter(only_audio=True)
    stream = yt.streams.first()
    return stream

def download_video():
    # from user input get video url
    link = input("In quotations, please enter URL of chosen Youtube video.\n")

    # pass youtube link through Youtube class
    yt = YouTube(link)
    print(yt.title)
    print("Downloading video...")

    # choose download type
    yt.streams.filter(file_extension='mp4')
    stream = yt.streams.first()
    return stream


if __name__=='__main__':
    main()
