from telethon import TelegramClient, events

# API credentials from https://my.telegram.org
api_id = '27900774'
api_hash = '690cef4b522a52ad7bf63ba5251dcf35'
source_channel = 'Avibum'  # Channel you want to scrape messages from
your_channel = 'AVIATORPREDICTORBYWHYRANDOM'  # Channel where you want to post messages

# Create the client and log in using your Telegram account
client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    message = event.message.message

    # Check for bet and cashout odds
    if "place a bet" in message and "cash out" in message:
        lines = message.splitlines()
        bet_line = [line for line in lines if "place a bet" in line][0]
        cashout_line = [line for line in lines if "cash out" in line][0]

        # Scrape the odds
        bet_odds = bet_line.split()[-1]  # e.g., "1.47x"
        cashout_odds = cashout_line.split()[-1]  # e.g., "1.50x"

        # Robotic message with context and emojis
        robotic_message = (
            f"🤖 **BETTING UPDATE INITIATED** 🤖\n\n"
            f"🔍 Detected new odds data:\n\n"
            f"💰 **Place Bet**: `{bet_odds}`\n"
            f"📈 **Cashout**: `{cashout_odds}`\n\n"
            f"🛠 Processing... Please follow the advised parameters. 📊\n"
            f"⚙️ Data analyzed: Odds collected from trusted bot systems.\n"
            f"⚠️ Maximum safe risk advised! Proceed with caution! ⚠️\n"
            f"🚀 Good luck, Pilot! 🎮"
        )

        # Post odds message to your channel
        await client.send_message(your_channel, robotic_message)

    # Check for login and game registration link (e.g., "ATTENTION Login possible")
    elif "ATTENTION" in message and "Login possible" in message:
        # Robotic message for login notice
        login_message = (
            f"🤖 **BETTING ANALYSIS POSSIBLE** 🤖\n\n"
            f"⚠️ **ATTENTION** ⚠️\n\n"
            f"🕹️ **Login available** for game registration!\n\n"
            f"🛠 Begin analysis, check game opportunities. 🛠\n"
            f"⚙️ System preparing the best strategy for maximum profit! 🚀\n"
            f"📡 Stay tuned, and good luck, Commander!"
        )

        # Post login and game registration message to your channel
        await client.send_message(your_channel, login_message)

# Start the client
client.start()
client.run_until_disconnected()
