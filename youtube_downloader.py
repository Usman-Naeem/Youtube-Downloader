import youtube_dl
import sys


def start(download_video):
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})
    url = input("Enter Url: ")
    with ydl:
        result = ydl.extract_info(
            url,
            download=download_video
        )

    if 'entries' in result:
        # In case of playlist
        video = result['entries'][0]
    else:
        video = result

    if not download_video:
        # TODO: Write details on file
        print(video['title'], " Downloaded !")


def menu():
    choice = input("1. Get Video Details\n2. Download Video\n => ")
    try:
        choice = int(choice)
    except:
        print("Enter Just Integers !")
        menu()
    if choice == 1:
        start(download_video=False)
    elif choice == 2:
        start(download_video=True)
    elif choice == 0:
        sys.exit()
    else:
        print("Enter between given options !")
        menu()
    menu()

menu()
# https://youtu.be/1O0yazhqaxs
