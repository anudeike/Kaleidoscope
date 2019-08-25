from google_images_download import google_images_download

# creating object
response = google_images_download.googleimagesdownload()

# search queries
search_query = 'sunset'

#set the arguments for the fetch
arguments = {
    "keywords": search_query,
    "format": "jpg",
    "limit": 4,
    "print_urls": True,
}

# get the download
try:
    paths = response.download(arguments)
except FileNotFoundError:
    print("file not found")

print(paths[0][search_query])


#handle file not found