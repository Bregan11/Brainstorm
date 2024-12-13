import telebot
import pandas as pd
import os

API_TOKEN = '7581804716:AAHnDr6xL4cDb_iaTadHMxe8wZ_ljzwYwsw'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Введите группу:")

@bot.message_handler(func=lambda message: True)
def send_group_data(message):
    group = message.text
    try:
        for root, dirs, files in os.walk("CSV"):
            for file in files:
                if file.endswith('.csv'):
                    file_path = os.path.join(root, file)
                    df = pd.read_csv(file_path, header=None)
                    filtered_data = df[df[1].str.contains(group, na=False)]
                    
                    if not filtered_data.empty:
                        response = f"Данные из файла: {file.replace('.csv', '')}\n"
                        for index, row in filtered_data.iterrows():
                            response += f"{row[0]} {row[1]} {row[2]}\n"
                        bot.send_message(message.chat.id, response)
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка: {e}")

bot.polling()
