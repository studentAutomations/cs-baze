import os
from dhooks import Webhook, Embed, File

WEBHOOK_URL = [os.getenv('PB')]
for url in WEBHOOK_URL:
    hook = Webhook(url) 

    hook.send('**@everyone**')
    
    image2_path = 'cs-baze1-nova-obavestenja.png' 

    hook.send(file=File(image2_path, name='cs-baze1-nova-obavestenja.png'))

    hook.send('**>>> https://cs.elfak.ni.ac.rs/nastava/**')
