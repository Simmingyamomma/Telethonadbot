import random
import asyncio
from telethon.sync import TelegramClient, events

API_ID = 29193610  # Replace with your API ID
API_HASH = ''  # Replace with your API hash
PHONE_NUMBER = ''
SESSION_FILE = 'IMPORTANT_SESSION'
GROUP_IDS = []  # Add the group IDs to the list

async def send_message(client, group_id, message):
    await client.send_message(group_id, message)
    print(f"Message sent to -> {group_id}")

async def main():
    client = TelegramClient(SESSION_FILE, API_ID, API_HASH)
    await client.start(phone=PHONE_NUMBER)
    print("Press enter to start sending messages...")
    input()

    while True:
        try:
            # Send the message to the groups
            message = "Your Text"
            for group_id in GROUP_IDS:
                await send_message(client, group_id, message)

            # Generate random wait time between 50 and 120 minutes
            wait_time = random.randint(50, 90)
            print(f"Waiting for {wait_time} minutes...")
            await asyncio.sleep(wait_time * 60)

        except KeyboardInterrupt:
            print("Program stopped.")
            break

    await client.disconnect()

asyncio.run(main())