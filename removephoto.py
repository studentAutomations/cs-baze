import os


photo_path = 'https://github.com/studentAutomations/cs-baze/blob/56a5a7e9c6bd1cfc790f9b9985ba4879a0c723fd/cs-baze-nova-obavestenja.png'  


if os.path.exists(photo_path):
    os.remove(photo_path)  
