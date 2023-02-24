from telegram.ext import *

import keys


def start_command(update, context):
    # context.bot.send_message(chat_id=update.effective_chat.id, text="Hi, I'm a bot!")
    update.message.reply_text('Hello!')


def help_command(update, context):
    # context.bot.send_message(chat_id=update.effective_chat.id, text="Hi, I'm a bot!")
    update.message.reply_text('Tente digitar algo para eu responder!')


def custom_command(update, context):
    # context.bot.send_message(chat_id=update.effective_chat.id, text="Hi, I'm a bot!")
    update.message.reply_text('custom!')


def handle_response(text: str) -> str:
    if 'oi' in text:
        return 'Olá!'

    if 'como voce esta?' in text:
        return 'Eu estou bem! Obrigada por perguntar.'

    return 'Não sei, o que você pensa sobre isso?'


def handle_message(update, context):
    message_type = update.message.chat.type
    text = str(update.message.text).lower()
    response = ''

    print(f'User: {update.message.chat.id} in: {message_type} /n says: "{text}" ')

    if message_type == 'group':
        if '@the_yume_bot' in text:
            updated_text = text.replace('@the_yume_bot', '').strip()
            response = handle_response(updated_text)
    else:
        response = handle_response(text)

    update.message.reply_text(response)


def error(update, context):
    print(f'Update: {update} caused error: {context.error}')


if __name__ == '__main__':

    print('Starting up...')
    updater = Updater(keys.token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('custom', custom_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)

    updater.start_polling(1.0)
    updater.idle()