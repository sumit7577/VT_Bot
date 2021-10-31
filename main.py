from pyrogram import Client, filters
from pyrogram.types import messages_and_media
import requests,os


appId = os.environ.get("appId")
appHash = os.environ.get("appHash")
app = Client("vt_bot",api_id=appId,api_hash=appHash,bot_token=os.environ.get("botToken"))



@app.on_message(filters.text & filters.private)
def echo(client, message):
    firstName = message.from_user.first_name
    lastName = message.from_user.last_name
    try:
        fullName = firstName+ " " + lastName
    except:
        fullName = firstName
    if message.text == "/start":
        message.reply_text(f"Hlo {fullName} welcome to the VT_Premium Downloader bot.Please Provide a hash to get the file Contents.")
    else:
        apiKey =os.environ.get("apiKey")
        url = f"https://www.virustotal.com/vtapi/v2/file/download?apikey={apiKey}&hash={message.text}"
        with requests.get(url, stream=True) as makeRequest:
            makeRequest.raise_for_status()
            if(makeRequest.status_code == 200):
                with open(firstName, 'wb') as file:
                    for chunk in makeRequest.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                        file.write(chunk)
                message.reply_document(message.from_user.first_name)
                os.remove(message.from_user.first_name)
            else:
                message.reply_text("Please provide a valid hash value")
        

if __name__ == "__main__":
    app.run()