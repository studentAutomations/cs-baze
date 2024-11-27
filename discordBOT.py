import os
from dhooks import Webhook, Embed, File


WEBHOOK_URL = [os.getenv('PROBA')]


for url in WEBHOOK_URL:
    hook = Webhook(url) 

    hook.send('**@everyone Nova obavestenja na CS-u!**')
    
    image2_path = 'https://github.com/studentAutomations/cs-baze/blob/56a5a7e9c6bd1cfc790f9b9985ba4879a0c723fd/cs-baze-nova-obavestenja.png'  
    
    hook.send(file=File(image2_path, name='cs-baze-nova-obavestenja.png'))

    hook.send('**>>> https://cs.elfak.ni.ac.rs/nastava/**')
