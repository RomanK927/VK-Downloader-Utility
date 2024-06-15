import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

# Ваш токен
TOKEN = 'vk1.a.R0w80lkqh_ILVT9_Mgm6Z0dC6HmYZeLwTA__8-TTvrEugELV8Am4pM28r75I_nvVRb2_0hihjAoBMs3v9SNT03C024AJOgiVjnREGgMno8N6soDJ5B-FbLl9UD9EUe4yw2hEiMbbG1dzf-Q8ZGTJWQ8OSQ9WaBPszkFXpV1ckPRVF_UUHOVKDtXnkNUGKqvmWjvExYBC_vV8rc11e4pGZg'

# ID вашей группы
GROUP_ID = 'club225877866'

vk_session = vk_api.VkApi(token=TOKEN)
longpoll = VkBotLongPoll(vk_session, GROUP_ID)

def send_message(user_id, message):
    vk_session.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': 0})

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.from_user:
            send_message(event.obj.from_id, "Извините, сейчас я не работаю")
