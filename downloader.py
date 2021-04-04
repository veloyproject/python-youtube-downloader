from pytube import YouTube

def progress_download(streams, chunk, bytes_remainings):
    global bytes_total
    print(f"{streams.filesize} Bytes", 
          f"Downloaded {bytes_remainings} bytes", 
          sep="-", 
          end="\r\r\r")
    
def complete_download(streams, filepath):
    print(f"Download has been completed!")
    print(f"open {filepath}")

url = "https://www.youtube.com/watch?v=JHEXULfJ4Dg"

yt = YouTube(url, 
             on_progress_callback=progress_download,
             on_complete_callback=complete_download)

print("AUTHOR")
print(yt.author)
print("---------")

print("DESCRIPTION")
print(yt.description)
print("---------")


print("KEYWORDS")
print(yt.keywords)
print("---------")

print("LENGTH")
print(yt.length)
print("---------")

print("PUBLISH DATE")
print(yt.publish_date)
print("---------")


streams = yt.streams.filter(
    file_extension='mp4', 
    res='720p')

streams.first().download()
