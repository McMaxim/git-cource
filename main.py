import requests
from bs4 import BeautifulSoup
from telegram.ext import Updater, CommandHandler
import telegram

def get_price(update, context):
    if len(context.args) == 0:
        update.message.reply_text("Пожалуйста, укажите артикул набора LEGO.")
        return

    article = context.args[0]
    search_url = f"https://www.bricklink.com/v2/search.page?q={article}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    link = soup.find("a", class_="thumbnail-thumb")

    if link is None:
        update.message.reply_text("Набор с таким артикулом не найден на BrickLink.")
        return


    if price_element is None:
        update.message.reply_text("Цена для этого набора не найдена.")
        return

    price = price_element.text.strip()
    update.message.reply_text(f"Цена набора LEGO с артикулом {article}: {price}")

def main():
    api_token = '5991231785:AAHn6ckEEZihHIPuCiKzsiFAlVIs8_Sy0hQ'
    updater = Updater(api_token, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('price', get_price))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()