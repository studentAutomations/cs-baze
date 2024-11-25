import os


photo_path = 'https://github.com/studentAutomations/cs-baze/blob/main/cs-baze-nova-obavestenja.png'  


if os.path.exists(photo_path):
    os.remove(photo_path)  
