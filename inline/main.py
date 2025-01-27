from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

def start(update, context):
    keyboard = [
        [InlineKeyboardButton("Option 1", callback_data='1')],
        [InlineKeyboardButton("Option 2", callback_data='2')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('ကျေးဇူးပြု၍ ရွေးချယ်ပါ။', reply_markup=reply_markup)

def button(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=f"ရွေးချယ်ထားသော option: {query.data}")

def main():
    updater = Updater("8183331435:AAHy1T7DkaF2rK10mwTBZCAop1etgfXb008", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()