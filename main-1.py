from telethon.sync import TelegramClient
from telethon.sessions import StringSession

# Replace these with your actual API ID and API hash
api_id = '28244'
api_hash = '719bdb2fc4fdb2078f006'

# You can replace the session string with an empty string if you don't have a session yet
session_string = 'session_string = 'AQGu-pcAnvO0m0foETxKLe86q7dXckJX7sdNvp7Ncs0XoOtlc15OuanM4IB6LZws7gK4z43UEaAgzF_JODXxIqU9uHolqu5qRUql7CQlLNsheBjd1BopKuSE-uSSyo1VQIEx'  # Leave empty if creating a new session

if session_string:
    client = TelegramClient(StringSession(session_string), api_id, api_hash)
else:
    client = TelegramClient('anon', api_id, api_hash)

async def main():
    # Connect to Telegram
    await client.start()
    print("Client Created")

    # If you don't have a session, it will prompt you to enter the phone number
    # and code received via SMS or Telegram.
    if not session_string:
        print("Logging in...")
        await client.sign_in(phone='YOUR_PHONE_NUMBER')  # Enter your phone number here
        code = input('Enter the code: ')
        await client.sign_in(code=code)
    
    # Once logged in, print the session string to reuse it later
    print("Session string:", client.session.save())

    # You can now use the client for any Telegram operations
    me = await client.get_me()
    print(me.stringify())

with client:
    client.loop.run_until_complete(main())
