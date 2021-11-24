from pyrogram import Client, idle

api_id = 8245524

api_hash = "b4ee2d8b7c4cb8fff5a572a0ff75bb19"

plugins = dict(

    root="plugins",

    include=[

        "vc.player",

        "ping",

        "sysinfo"

    ]

)

app = Client("tgvc", api_id, api_hash, plugins=plugins)

app.start()

print('>>> USERBOT STARTED')

idle()

app.stop()

print('\n>>> USERBOT STOPPED')

