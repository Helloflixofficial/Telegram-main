from telethon import TelegramClient
# Replace these with your API ID and API hash
api_id = 'API_ID'
api_hash = 'API_HASH'    
# Create the client and connect
client = TelegramClient('session_name', api_id, api_hash)
async def main():
    # Connect to Telegram
    await client.start()
    # Print information about the logged in user
    me = await client.get_me()
    print(f'Logged in as {me.first_name} ({me.username})')
# Run the main function
with client:
    client.loop.run_until_complete(main())

