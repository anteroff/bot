print("Bot by: voxdox")
print("Version: 1.0.0")

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import random
import time
import traceback
import json
import threading
import bibl as bb
import settings as st
import answers as an

CALLBACK_TYPES = ('show_snackbar', 'open_link', 'open_app')

vk = vk_api.VkApi(token=st.GROUP_TOKEN)
vk._auth_token()
st.GROUP_TOKEN
vk.get_api()
longpoll = VkBotLongPoll(vk, st.GROUP_ID)


def get_name(uid: int) -> str:
    data = vk.method("users.get", {"user_ids": uid})[0]
    return "{}".format(data["first_name"])


def send_message(user_id, text, keyboard=None, template=None):
    vk.method("messages.send", {"user_id": user_id, "message": text,
                                "random_id": random.randint(-9223372036854775807, 9223372036854775807),
                                "keyboard": keyboard, "template": template})


def rasilka(text):
    data = bb.sender()
    for i in data:
        try:
            send_message(str(i[0]), str(text))
            time.sleep(1)
        except Exception as E:
            pass


while True:
    try:
        try:
            messages = vk.method("messages.getConversations", {"offset": 0, "count": 5, "filter": "unanswered"})
            if messages["count"] >= 1:
                id = messages["items"][0]["last_message"]["from_id"]
                body = messages["items"][0]["last_message"]["text"]

                if bb.var(body.lower(), ["меню"]) == True:
                    keyboard = VkKeyboard(one_time=False, inline=False)
                    keyboard.add_button("✅ Подключить ✅", color=VkKeyboardColor.PRIMARY)
                    keyboard.add_line()
                    keyboard.add_button("🆘 Помощь 🆘", color=VkKeyboardColor.POSITIVE)
                    keyboard.add_button("📊 Статистика 📊", color=VkKeyboardColor.POSITIVE)
                    if bb.admin_check(id) >= 1:
                        keyboard.add_line()
                        keyboard.add_button("Админ", color=VkKeyboardColor.NEGATIVE)
                    vk.method("messages.send", {"peer_id": id, "message": "Меню", "keyboard": keyboard.get_keyboard(),
                                                "random_id": random.randint(1, 2147483647)})


                elif body.lower() == "✅ подключить ✅":
                    keyboard = VkKeyboard(one_time=False, inline=False)
                    keyboard.add_button("💥 На свою 💥", color=VkKeyboardColor.PRIMARY)
                    keyboard.add_button("💥 На чужую 💥", color=VkKeyboardColor.PRIMARY)
                    keyboard.add_line()
                    keyboard.add_button("Меню", color=VkKeyboardColor.NEGATIVE)
                    vk.method("messages.send", {"peer_id": id, "message": "На какую страницу вы бы хотели подключить уведомления?",
                                                "keyboard": keyboard.get_keyboard(),
                                                "random_id": random.randint(1, 2147483647)})

                elif body.lower() == "💥 на свою 💥":
                    keyboard = VkKeyboard(one_time=False, inline=False)
                    keyboard.add_button("⚡ Оплатить вручную ⚡", color=VkKeyboardColor.POSITIVE)
                    keyboard.add_line()
                    keyboard.add_openlink_button("⚡ Оплатить по ссылке ⚡","https://qiwi.com/n/WOVEN765/")
                    keyboard.add_line()
                    keyboard.add_button("Меню", color=VkKeyboardColor.NEGATIVE)
                    vk.method("messages.send", {"peer_id": id, "message": "Отлично, ваш профиль соответствует всем требованиям для подключения!\n \nК сожалению, процесс подключения является платным, цена по скидке составляет: 99₽",
                                                "keyboard": keyboard.get_keyboard(),
                                                "random_id": random.randint(1, 2147483647)})

                elif body.lower() == "💥 на чужую 💥":
                    keyboard = VkKeyboard(one_time=False, inline=False)
                    keyboard.add_button("⚡ Оплатить вручную ⚡ ", color=VkKeyboardColor.POSITIVE)
                    keyboard.add_line()
                    keyboard.add_openlink_button("⚡ Оплатить по ссылке ⚡","https://qiwi.com/n/WOVEN765/")
                    keyboard.add_line()
                    keyboard.add_button("Меню", color=VkKeyboardColor.NEGATIVE)
                    vk.method("messages.send", {"peer_id": id, "message": "Подключение к чужой странице\n \nК сожалению, процесс подключения является платным, цена по скидке составляет: 99₽",
                                                "keyboard": keyboard.get_keyboard(),
                                                "random_id": random.randint(1, 2147483647)})


                elif body.lower() == "📋 наши гарантии":
                    keyboard = VkKeyboard(one_time=False, inline=False)
                    keyboard.add_button("Почему нам стоит доверять?", color=VkKeyboardColor.POSITIVE)
                    keyboard.add_button("Уникальность чита", color=VkKeyboardColor.POSITIVE)
                    keyboard.add_line()
                    keyboard.add_button("Самое главное", color=VkKeyboardColor.PRIMARY)
                    keyboard.add_button("Это ничего не доказывает", color=VkKeyboardColor.PRIMARY)
                    keyboard.add_line()
                    keyboard.add_button("Меню", color=VkKeyboardColor.NEGATIVE)
                    vk.method("messages.send", {"peer_id": id, "message": "Открыл Вам вкладку наших гарантий📋",
                                                "keyboard": keyboard.get_keyboard(),
                                                "random_id": random.randint(1, 2147483647)})


                elif body.lower() == "🔒 могу ли получить бан?":
                    keyboard = VkKeyboard(one_time=False, inline=False)
                    keyboard.add_button("Получу ли я бан за это?", color=VkKeyboardColor.POSITIVE)
                    keyboard.add_button("Чит сейчас работает?", color=VkKeyboardColor.POSITIVE)
                    keyboard.add_line()
                    keyboard.add_button("Проверить актуальность чита", color=VkKeyboardColor.PRIMARY)
                    keyboard.add_button("Возможен ли бан по железу", color=VkKeyboardColor.PRIMARY)
                    keyboard.add_line()
                    keyboard.add_button("Меню", color=VkKeyboardColor.NEGATIVE)
                    vk.method("messages.send",
                              {"peer_id": id, "message": "Открыл Вам вкладку информации о шансах получения бана🔒",
                               "keyboard": keyboard.get_keyboard(), "random_id": random.randint(1, 2147483647)})

                elif body.lower() == "📚 информация":
                    keyboard = VkKeyboard(one_time=False, inline=False)
                    keyboard.add_button("О нас", color=VkKeyboardColor.POSITIVE)
                    keyboard.add_button("Часы работы", color=VkKeyboardColor.PRIMARY)
                    keyboard.add_line()
                    keyboard.add_openlink_button("Наш сайт", "https://valoranthacks.ru/")
                    keyboard.add_openlink_button("Отзывы", "https://vk.com/topic-194483303_41632413")
                    keyboard.add_line()
                    keyboard.add_button("Меню", color=VkKeyboardColor.NEGATIVE)
                    vk.method("messages.send", {"peer_id": id, "message": "Открыл Вам вкладку информации📚",
                                                "keyboard": keyboard.get_keyboard(),
                                                "random_id": random.randint(1, 2147483647)})


                elif body.lower() == "🆘 помощь 🆘":
                    keyboard = VkKeyboard(one_time=False, inline=False)
                    keyboard.add_button("Связаться с тех.поддержкой", color=VkKeyboardColor.POSITIVE)
                    keyboard.add_button("FAQ", color=VkKeyboardColor.POSITIVE)
                    keyboard.add_line()
                    keyboard.add_button("Оплатил, но уведомления не приходят", color=VkKeyboardColor.PRIMARY)
                    keyboard.add_line()
                    keyboard.add_button("Меню", color=VkKeyboardColor.NEGATIVE)
                    vk.method("messages.send", {"peer_id": id, "message": "Помощь",
                                                "keyboard": keyboard.get_keyboard(),
                                                "random_id": random.randint(1, 2147483647)})


                elif body.lower() == "товары":
                    keyboard = VkKeyboard(one_time=False, inline=False)
                    keyboard.add_openlink_button("💰 MultiHack",
                                                 "https://vk.com/market-194483303?w=product-194483303_4605104%2Fquery")
                    keyboard.add_openlink_button("💰 WallHack",
                                                 "https://vk.com/market-194483303?w=product-194483303_4605084%2Fquery")
                    keyboard.add_line()
                    keyboard.add_openlink_button("💰 BonnyHop",
                                                 "https://vk.com/market-194483303?w=product-194483303_4605055%2Fquery")
                    keyboard.add_openlink_button("💰 Аккаунт VALORANT",
                                                 "https://vk.com/market-194483303?w=product-194483303_4605280%2Fquery")
                    keyboard.add_line()
                    keyboard.add_button("Меню", color=VkKeyboardColor.NEGATIVE)
                    vk.method("messages.send", {"peer_id": id, "message": get_name(id) + ", держите список товаров!",
                                                "keyboard": keyboard.get_keyboard(),
                                                "random_id": random.randint(1, 2147483647)})


                elif body.lower() == "не могу оплатить на сайте":
                    vk.method("messages.send", {"peer_id": id, "message": an.button_nobuysite,
                                                "random_id": random.randint(1, 2147483647)})

                elif body.lower() == "⚡ оплатить вручную ⚡":
                    vk.method("messages.send",
                              {"peer_id": id, "message": an.button_buydeve, "random_id": random.randint(1, 2147483647)})

                elif body.lower() == "почему нам стоит доверять?":
                    vk.method("messages.send", {"peer_id": id, "message": an.button_garantii,
                                                "random_id": random.randint(1, 2147483647)})

                elif body.lower() == "проблемы с читом":
                    vk.method("messages.send", {"peer_id": id, "message": an.button_trablecheat,
                                                "random_id": random.randint(1, 2147483647)})

                elif body.lower() == "оплатил, но уведомления не приходят":
                    vk.method("messages.send",
                              {"peer_id": id, "message": an.button_nocheat, "random_id": random.randint(1, 2147483647)})

                elif body.lower() == "faq":
                    vk.method("messages.send",
                              {"peer_id": id, "message": an.button_faq, "random_id": random.randint(1, 2147483647)})

                elif body.lower() == "связаться с тех.поддержкой":
                    vk.method("messages.send",
                              {"peer_id": id, "message": an.button_support, "random_id": random.randint(1, 2147483647)})

                # elif body.lower() == "часы работы":
                # 	vk.method("messages.send", {"peer_id": id, "message": an., "random_id": random.randint(1, 2147483647)})

                elif body.lower() == "о нас":
                    vk.method("messages.send",
                              {"peer_id": id, "message": an.button_onas, "random_id": random.randint(1, 2147483647)})

                elif body.lower() == "возможен ли бан по железу":
                    vk.method("messages.send",
                              {"peer_id": id, "message": an.button_hardban, "random_id": random.randint(1, 2147483647)})

                elif body.lower() == "проверить актуальность чита":
                    vk.method("messages.send", {"peer_id": id, "message": an.button_cheackstatus,
                                                "random_id": random.randint(1, 2147483647)})

                elif body.lower() == "чит сейчас работает?":
                    vk.method("messages.send",
                              {"peer_id": id, "message": an.button_status, "random_id": random.randint(1, 2147483647)})

                elif body.lower() == "получу ли я бан за это?":
                    vk.method("messages.send",
                              {"peer_id": id, "message": an.button_whatban, "random_id": random.randint(1, 2147483647)})

                elif body.lower() == "часы работы":
                    vk.method("messages.send",
                              {"peer_id": id, "message": an.button_work, "random_id": random.randint(1, 2147483647)})

                elif body.lower() == "уникальность чита":
                    vk.method("messages.send", {"peer_id": id, "message": an.button_unikcheat,
                                                "random_id": random.randint(1, 2147483647)})

                elif body.lower() == "самое главное":
                    vk.method("messages.send",
                              {"peer_id": id, "message": an.button_glavnoe, "random_id": random.randint(1, 2147483647)})

                elif body.lower() == "это ничего не доказывает":
                    vk.method("messages.send",
                              {"peer_id": id, "message": an.button_dokva, "random_id": random.randint(1, 2147483647)})
                # ------------------------------------ADMIN---------------------------------

                elif body.lower() == "админ1325465":
                    keyboard = VkKeyboard(one_time=False, inline=False)
                    if bb.admin_check(id) >= 0:
                        keyboard.add_button("Сообщения в поддержке1325465", color=VkKeyboardColor.POSITIVE)
                        if bb.admin_check(id) == 2:
                            keyboard.add_button("Статистика1", color=VkKeyboardColor.POSITIVE)
                        keyboard.add_line()
                        keyboard.add_button("Меню", color=VkKeyboardColor.NEGATIVE)
                        vk.method("messages.send",
                                  {"peer_id": id, "message": "Админ меню", "keyboard": keyboard.get_keyboard(),
                                   "random_id": random.randint(1, 2147483647)})
                    else:
                        vk.method("messages.send", {"peer_id": id, "message": "Вы не администратор!",
                                                    "random_id": random.randint(1, 2147483647)})


                elif body.lower() == "статистика1":
                    if bb.admin_check(id) == 0:
                        vk.method("messages.send",
                                  {"peer_id": id, "message": bb.getstat(), "random_id": random.randint(1, 2147483647)})
                    else:
                        vk.method("messages.send", {"peer_id": id, "message": "Вы не администратор!",
                                                    "random_id": random.randint(1, 2147483647)})

                elif body.lower() == "📊 статистика 📊":
                    if bb.admin_check(id) == 1:
                        keyboard.add_button("Просмотреть всех гостей", color=VkKeyboardColor.POSITIVE)
                        keyboard.add_line()
                        keyboard.add_button("Меню", color=VkKeyboardColor.NEGATIVE)
                        vk.method("messages.send",
                                  {"peer_id": id, "message": "Статистика за сегодня:\n--Посещений вашей страницы: 19\n--Посещений от противоположного пола: 13\n", "random_id": random.randint(1, 2147483647)})
                    else:
                        vk.method("messages.send", {"peer_id": id, "message": "Вы не подключили уведомления!",
                                                    "random_id": random.randint(1, 2147483647)})

                elif body.lower() == "просмотреть всех гостей":
                    keyboard.add_button("Меню", color=VkKeyboardColor.NEGATIVE)
                    vk.method("messages.send",
                              {"peer_id": id,
                               "message": "asdadsad",
                               "random_id": random.randint(1, 2147483647)})


                elif body.lower() == "сообщения в поддержке1325465":
                    if int(bb.admin_check(id)) >= 0:
                        vk.method("messages.send", {"peer_id": id, "message": bb.get_support(id),
                                                    "random_id": random.randint(1, 2147483647)})
                    else:
                        vk.method("messages.send", {"peer_id": id, "message": "Вы не администратор!",
                                                    "random_id": random.randint(1, 2147483647)})


                elif str(body.lower()).split()[0] == "рассылка":
                    if bb.admin_check(id) == 0:
                        n = str(body).splitlines()
                        n.pop(0)
                        text = ''
                        for i in n:
                            text = text + "\n" + str(i)
                        rasilka(text)
                    else:
                        vk.method("messages.send", {"peer_id": id,
                                                    "message": "Уровень админ, не соотвествует требованиям данной функции",
                                                    "random_id": random.randint(1, 2147483647)})


                elif body.split()[0] == "admin+" and len(body.split()) == 3:
                    if bb.admin_check(id) == 0:
                        vk.method("messages.send", {"peer_id": id,
                                                    "message": bb.add_admin(str(body.split()[0]), str(body.split()[1]),
                                                                            str(body.split()[2])),
                                                    "random_id": random.randint(1, 2147483647)})
                    else:
                        vk.method("messages.send", {"peer_id": id,
                                                    "message": "Вы не администратор, или ваш уровень не достаточно высок для использования данной команды!",
                                                    "random_id": random.randint(1, 2147483647)})

                elif str(body.lower()).split()[0] == "ответ":
                    if int(bb.admin_check(id)) >= 0:
                        n = str(body).splitlines()
                        n.pop(0)
                        text = n
                        n = n[0]
                        vk.method("messages.send", {"peer_id": id,
                                                    "message": bb.send_support(str(id), str(body.lower()).split()[1],
                                                                               str(n)),
                                                    "random_id": random.randint(1, 2147483647)})
                    else:
                        vk.method("messages.send", {"peer_id": id, "message": "Вы не администратор!",
                                                    "random_id": random.randint(1, 2147483647)})
                # ---------------------------------PROCHEE-----------------------------------
                elif str(body.lower()).split()[0] == "поддержка":
                    n = str(body).splitlines()
                    n.pop(0)
                    text = n
                    n = n[0]
                    vk.method("messages.send", {"peer_id": id, "message": bb.write_support(id, n),
                                                "random_id": random.randint(1, 2147483647)})

                elif body.lower()[0] == "!":
                    text = body[1:]
                    bb.send_message(st.alert_id, text + "\n\nФорма от: " + str("(" + bb.get_name(id) + ")"))
                    vk.method("messages.send", {"peer_id": id, "message": "Форма отправлена!",
                                                "random_id": random.randint(1, 2147483647)})

                else:
                    keyboard = VkKeyboard(one_time=False, inline=False)
                    keyboard.add_button("Меню", color=VkKeyboardColor.NEGATIVE)
                    vk.method("messages.send", {"peer_id": id, "message": get_name(
                        id) + ", команда не найдена или неправильно написана. Попробуйте заново или перейдите в меню",
                                                "keyboard": keyboard.get_keyboard(),
                                                "random_id": random.randint(1, 2147483647)})
                bb.adddata(id)
        except Exception as E:
            vk.method("messages.markAsRead",
                      {"peer_id": id, "message": str(an.gm), "random_id": random.randint(1, 2147483647)})
    except Exception as E:
        print("Error")
