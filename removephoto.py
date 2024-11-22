import os

# Specify the path to the photo you want to delete
photo_path = 'https://github.com/studentAutomations/cs-baze/blob/main/cs-baze-nova-obavestenja.png'  # Change this to the actual path of your photo

# Check if the file exists before attempting to delete it
if os.path.exists(photo_path):
    os.remove(photo_path)  # Delete the file
