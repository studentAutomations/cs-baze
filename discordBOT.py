import os
from dhooks import Webhook, Embed, File

image2_path = 'cs-baze-nova-obavestenja.png'

WEBHOOK_URL = [os.getenv('PB')]
for url in WEBHOOK_URL:
    hook = Webhook(url)

    embed = Embed(
        description="**[CS link - click here -](https://cs.elfak.ni.ac.rs/nastava/mod/forum/view.php?id=104)**",
        color=0x3498DB
    )

    embed.set_image(url="attachment://cs-baze-nova-obavestenja.png")
    file = File(image2_path, name="cs-baze-nova-obavestenja.png")
    hook.send("@everyone 📢 Baze", embed=embed, file=file)
