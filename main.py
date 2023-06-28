import telebot as telebot
from telebot.types import PhotoSize
from holiday_framer.get_texted_image import get_texted_from
import vars

bot = telebot.TeleBot(vars.bot_token)


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    userid = message.chat.id
    print(userid)
    print(message.chat)
    userpics = bot.get_user_profile_photos(userid)
    userpic = userpics.photos[0][-1]

    send_holiday(userpic, userid, message.from_user.username)

    bot.send_message(userid, "Просто скинь фото и расслабься – вот мой девиз.\n"
                             "(вы можете присылать любые фотографии, чтобы сделать их relaxing)")


@bot.message_handler(content_types=["photo"])
def photo_handle(message: telebot.types.Message):
    userid = message.chat.id
    print(userid)
    print(message.chat)
    # for k in dir(message):
    #     if getattr(message, k) is not None and k[0] != "_":
    #         print(k, ':', getattr(message, k))

    photosizes = message.photo
    photo = photosizes[-1]

    send_holiday(photo, userid, message.from_user.username)


def send_holiday(photo, chat_id, username="unknown"):
    path = f"avatars/{username}_{photo.file_unique_id}.png"
    save_photo(photo, path)
    send_photo(get_texted_from(path, "В ОТПУСКЕ", font="Geologica-Bold.ttf"), chat_id)


def save_photo(photo: PhotoSize, path: str):
    file_info = bot.get_file(photo.file_id)
    file = bot.download_file(file_info.file_path)
    with open(path, 'wb') as new_file:
        new_file.write(file)


def send_photo(photo, chat_id):
    bot.send_photo(chat_id, photo)


bot.infinity_polling(40)
