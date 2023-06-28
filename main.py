import telebot as telebot
from PIL import Image
from telebot.types import PhotoSize
from holiday_framer.get_texted_image import get_texted_from
import vars
from io import BytesIO

bot = telebot.TeleBot(vars.bot_token)


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    userid = message.chat.id
    print(userid)
    print(message.chat)
    userpics = bot.get_user_profile_photos(userid)
    userpic = userpics.photos[0][-1]

    bot.send_message(userid, "Просто скинь фото и расслабься – вот мой девиз.\n"
                             "Отправив фотографию, вы получите надпись \"В\xA0ОТПУСКЕ\", "
                             "чтобы получить кастомную надпись отправьте фото с текстом под ним.")
    send_holiday(userpic, userid, message.from_user.username)


@bot.message_handler(content_types=["photo"])
def photo_handle(message: telebot.types.Message):
    userid = message.chat.id
    print(userid)
    print(message.chat)
    print(message)
    # for k in dir(message):
    #     if getattr(message, k) is not None and k[0] != "_":
    #         print(k, ':', getattr(message, k))

    photosizes = message.photo
    photo = photosizes[-1]

    if message.caption:
        send_holiday(photo, userid, message.from_user.username, message.caption)
    else:
        send_holiday(photo, userid, message.from_user.username)


def send_holiday(photo, chat_id, username="unknown", text="В ОТПУСКЕ"):
    path = f"avatars/{username}_{photo.file_unique_id}.png"
    save_photo(photo, path)
    try:
        texted_photo = get_texted_from(path, text, font="Geologica-Bold.ttf")
        send_photo(texted_photo, chat_id)
        send_photo_old(texted_photo, chat_id)
    except Exception as e:
        bot.send_message(chat_id, "Что-то пошло не так.")
        raise e


def save_photo(photo: PhotoSize, path: str):
    file_info = bot.get_file(photo.file_id)
    file = bot.download_file(file_info.file_path)
    with open(path, 'wb') as new_file:
        new_file.write(file)


def send_photo(photo: Image.Image, chat_id):
    byte_io = BytesIO()
    photo.save(byte_io, 'png')
    byte_io.seek(0)
    bot.send_document(chat_id, byte_io, visible_file_name="high-res.png")


def send_photo_old(photo, chat_id):
    bot.send_photo(chat_id, photo)


bot.infinity_polling(40)
