from pyrogram import Client, filters
from pyrogram.types import messages_and_media
import requests,os


appId = "2475015"
appHash = "6491c2e4ed6df64cda458d1517117d13"
app = Client("vt_bot",api_id=appId,api_hash=appHash,bot_token="2072883509:AAHJyAOeVU1F9IppQE5u2qn7lH5CBpxYcwE")



@app.on_message(filters.text & filters.private)
def echo(client, message):
    fullName = message.from_user.first_name + " " + message.from_user.last_name
    if message.text == "/start":
        message.reply_text(f"Hlo {fullName} welcome to the VT_Premium Downloader bot.Please Provide a hash to get the file Contents.")
    else:
        apiKey ="805f16812921f8b6ba9d535cabf532930629f569e5f26051027000cf0234222a"
        url = f"https://www.virustotal.com/vtapi/v2/file/download?apikey={apiKey}&hash={message.text}"
        with requests.get(url, stream=True) as makeRequest:
            makeRequest.raise_for_status()
            if(makeRequest.status_code == 200):
                with open(message.from_user.first_name, 'wb') as file:
                    for chunk in makeRequest.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                        file.write(chunk)
                message.reply_document(message.from_user.first_name)
                os.remove(message.from_user.first_name)
            else:
                message.reply_text("Please provide a valid hash value")
        


app.run()