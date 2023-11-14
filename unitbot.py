from telethon.sync import events
from telethon import TelegramClient
import time
import random
import configparser

config = configparser.ConfigParser()
config.read("settings.ini")
idd = 0


with TelegramClient(
    "foxx", config["Api"]["api_id"], config["Api"]["api_hash"]
) as client:


    @client.on(events.NewMessage(pattern=";chats", outgoing=True))
    async def chatss(event):
        liist = []
        async for dialog in client.iter_dialogs():
            gg = f"{dialog.name} : {dialog.id}"
            liist.append(gg)
        await event.delete()
        await event.respond("All your chats: ")
        await event.respond(str(liist))
        print(idd)

    @client.on(events.NewMessage(pattern=";repeater (\w+)", outgoing=True))
    async def set_id(event):
        global idd
        global text
        text = event.text[9:]
        idd = str(event.original_update.user_id)
        await event.delete()
        await client.send_message("me", f'Your choose is {idd}')

    @client.on(events.NewMessage(func=lambda e: e.is_private, incoming=True))
    async def repeater(event):
        user_from = await event.client.get_entity(event.from_id)
        if int(idd) == user_from.id:
            await event.respond(text)
        else:
            pass

    @client.on(events.NewMessage(pattern=";spam(?: |$)(.*)", outgoing=True))
    async def spam(event):
        await event.delete()
        get_text = event.text[6:]
        ldr = get_text.split(" ", 1)
        counter = int(ldr[0])
        mesg = ldr[1]
        for i in range(counter):
            await event.respond(mesg)

    @client.on(events.NewMessage(pattern=";ran (\w+)", outgoing=True))
    async def randomer(event):
        get_count = int(event.pattern_match.group(1))
        randomizee = random.randint(0, get_count)
        await event.edit(str(randomizee))

    @client.on(events.NewMessage(pattern=";mag(?: |$)(.*)", outgoing=True))
    async def magic_first(event):
        get_text = event.text[5:]
        dict = ""
        for i in get_text:
            if i == " ":
                dict += "•"
            await event.edit(f"{dict}{i}")
            dict = f"{dict}{i}\n"
            time.sleep(0.553)

    # @client.on(events.NewMessage(pattern=";mag(?: |$)(.*)", outgoing=True))
    # async def magic_second(event):
    #     get_text = event.text[5:]
    #     dict = ''
    #     for i in get_text:
    #         if i == ' ':
    #             dict += '.'
    #         await event.edit(f"{dict}{i}")
    #         dict = dict + i
    #         time.sleep(0.553)


    client.run_until_disconnected()
