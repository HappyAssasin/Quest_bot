import telebot

bot = telebot.TeleBot('') # Token
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
keyboard3 = telebot.types.ReplyKeyboardMarkup(True)
keyboard4 = telebot.types.ReplyKeyboardMarkup(True)
keyboard5 = telebot.types.ReplyKeyboardMarkup(True)
keyboard6 = telebot.types.ReplyKeyboardMarkup(True)
keyboard7 = telebot.types.ReplyKeyboardMarkup(True)
keyboard3.row('Попытаться выйти из пещеры', 'Нож-закончить игру')
keyboard1.row('Взять колбасу', 'Попытаться выйти из пещеры', 'Нож-закончить игру')
keyboard2.row('Съесть колбасу', 'Оставить')
keyboard4.row('Использовать зажигалку', 'Идти на ощупь')
keyboard5.row('Конечно пошли вперед')
keyboard6.row('Конечно, пошли')
keyboard7.row('Левая', 'Правая', 'Прямо')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b> бот, "
                     "созданный для квествой игры.\nДля Ознакомления с правилами пропиши команду /info".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html')


@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id,
                     'Правила этой игры это твоя жизнь из-за твоего выбора будет-ли жить твой персонаж '
                     'или умрет для запуска введите команду /go')


@bot.message_handler(commands=['go'])
def go(message):
    peshera = open('peshera.webp', 'rb')
    bot.send_sticker(message.chat.id, peshera)
    bot.send_message(message.chat.id,
                     'Ты просыпаешься в темной пещере, рядом с тобой лежит твой зашарпанный рюкзак.\n'
                     'Ты решаешь осмотреть его внутри ты находишь нож, зажигалку, палку колбасы, пустая бутылка.\n'
                     'Ты проголодался.Что ты будешь делать?', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def question(message):
    eda = open('Foodbar20.webp', 'rb')
    edagolod = open('Foodbar15.webp', 'rb')
    kolbasa = open('kolbasa.webp', 'rb')
    zah = open('zah.webp', 'rb')
    if message.text.lower() == 'съесть колбасу':
        bot.send_message(message.chat.id, 'Ты съедаешь колбасу и полностью насыщаешься.\n'
                                          'Но теперь из-за сухой колбассы тебе хочется пить, '
                                          'нужно найти источник с водой\nЧто ты дальше будешь делать?', reply_markup=keyboard3)
        bot.send_sticker(message.chat.id, eda)
    elif message.text.lower() == 'оставить':
        bot.send_message(message.chat.id, 'Ты решаешь что лучше оставить колбасу на потом,'
                                          'бог знает сколько ты будешь находиться в этом подземелье\n'
                                          'Что ты дальше будешь делать?', reply_markup=keyboard3)
        bot.send_sticker(message.chat.id, edagolod)
    elif message.text.lower() == 'взять колбасу':
        bot.send_message(message.chat.id, 'Ты берешь колбасу и можешь решить есть ли тебе ее или нет', reply_markup=keyboard2)
        bot.send_sticker(message.chat.id, kolbasa)
    elif message.text.lower() == 'попытаться выйти из пещеры':
        bot.send_message(message.chat.id, 'Ты можешь воспользоваться зажигалкой или пойти на ощупь, '
                                          'но если идти найти без источника света можно причинить себе вред\n'
                                          'Как ты поступишь?', reply_markup=keyboard4)
        bot.send_sticker(message.chat.id, zah)
    elif message.text.lower() == 'использовать зажигалку':
        bot.send_message(message.chat.id, 'Непросветная тьма вдруг куда-то испарилась и теперь ты можешь'
                                          'идти не боясь споткнуться, но не забывай количество топлива не бесконечно\n'
                                          'Ну что идем?', reply_markup=keyboard5)
    elif message.text.lower() == 'идти на ощупь':
        bot.send_message(message.chat.id, 'Ты решаешь что можно не использовать зажигалку ведь топливо очень важно\n'
                                          'Ну что идем?', reply_markup=keyboard6)
    elif message.text.lower() == 'конечно пошли вперед':
        bot.send_message(message.chat.id, 'Идя относительно долго примерно час ты выходишь на перекресток, '
                                          'перед тобой три входа в каждую пещеру, какую ты выбирешь?', reply_markup=keyboard7)
    elif message.text.lower() == 'левая':
        bot.send_message(message.chat.id, 'Ты решаешь пойти на лево, пройдя немного дальше и зайдя в глубь пещеры ты '
                                          'слышишь звук воды, обрадовавшись ты идешь дальше и ты встаешь около уступа')
    elif message.text.lower() == 'правая':
        bot.send_message(message.chat.id, 'Ты выбираешь пойти вправо')
    elif message.text.lower() == 'прямо':
        bot.send_message(message.chat.id, 'Ты выбираешь пойти прямо')


bot.polling(none_stop=True)
