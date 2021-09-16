from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("😋BOTS CHANNEL😇", url="https://t.me/KOT_BOTS")],
        [InlineKeyboardButton(
            "😈developer😈", url="https://t.me/KOT_FREE_DE_LA_HOYA_OFF")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
