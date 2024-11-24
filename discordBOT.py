import os
from dhooks import Webhook, Embed

# Get the webhook URL from environment variable
WEBHOOK_URL = [os.getenv('WEBHOOK_MAIN'), os.getenv('WEBHOOK_OTHER1')]


for url in WEBHOOK_URL:
    hook = Webhook(url) 

    embed = Embed(
        color= 0x499957,
        timestamp='now'
    )

    hook.send('@everyone Nova obavestenja na CS-u!')

    image1 = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOmPtpzziqcXbG795QYLmYvJl6G6CcyKbKHA&s'
    image2 = 'https://github.com/studentAutomations/cs-baze/blob/main/cs-baze-nova-obavestenja.png'


    embed.add_field(name='Idi na sajt - ', value='https://cs.elfak.ni.ac.rs/nastava/')
    embed.add_field(name='Vidi obavestenja - ', value=image2)
    embed.set_footer(text='Elektronski Fakultet')
    embed.set_thumbnail(image1)

    hook.send(embed=embed)
