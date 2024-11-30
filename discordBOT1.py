import os
from dhooks import Webhook, Embed, File

WEBHOOK_URL = [os.getenv('WEBHOOK_MAIN'), os.getenv('WEBHOOK_OTHER1')]
for url in WEBHOOK_URL:
    hook = Webhook(url) 

    hook.send('**@everyone CS je ažuriran!**')
    
    image2_path = 'cs-baze1-nova-obavestenja.png' 

    hook.send(file=File(image2_path, name='cs-baze1-nova-obavestenja.png'))

    hook.send('**>>> https://cs.elfak.ni.ac.rs/nastava/**')
