print("\nЗагружаю БД...")
import vk_api
import random
import threading
import sqlite3
import settings as st

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

vk = vk_api.VkApi(token=st.GROUP_TOKEN)
vk._auth_token()
vk.get_api()
longpoll = VkBotLongPoll(vk, st.GROUP_ID)

def send_message(user_id, text, keyboard=None, template=None):
	vk.method("messages.send", {"user_id": user_id, "message": text,
								"random_id": random.randint(-9223372036854775807, 9223372036854775807)})

def get_name(uid: int) -> str:
    data = vk.method("users.get", {"user_ids": uid})[0]
    return "{} {}".format(data["first_name"], data["last_name"])


conn = sqlite3.connect("data/data.db") # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()


def var(a , b):
	n = 0

	for i in b:
		if str(i) == str(a):
			n = 1
	if n == 1:
		return(True)
	else:
		return(False)

def add_admin(text, idd, lvl):
	if text == "admin+":
		sql = "SELECT admin FROM data WHERE user_id=?"
		for i in cursor.execute(sql, [(str(idd))]):
			msg = i[0]
		sql = f"UPDATE data SET admin={lvl} WHERE user_id=?"
		cursor.execute(sql, [(str(idd))])
		conn.commit()
		return("Уровень админ-меню был выдан: " + lvl)
	else:
		return("No command")


def sender():
	sql = "SELECT user_id FROM data"
	cursor.execute(sql)
	a = cursor.fetchall()
	return(a)

def adddata(id):
	sql = "SELECT user_id FROM data WHERE user_id=?"
	cursor.execute(sql, [(str(id))])
	b = cursor.fetchone()
	if b is None:
		params = (str(id), "1", "0")
		cursor.execute("INSERT INTO data VALUES (?, ?, ?)", params)
		conn.commit()
		print("Новый пользователь в базе!")
		 #text = "🔔Уведомление:\n👔Новый пользователь в базе данных!" + "\n⚙ID: " + str(id)
		# send_message(str(153285066), str(text))
	else:
		sql = "SELECT all_msg FROM data WHERE user_id=?"
		for i in cursor.execute(sql, [(str(id))]):
			msg = i[0]
		sql = f"UPDATE data SET all_msg={msg+1} WHERE user_id=?"
		cursor.execute(sql, [(str(id))])
		conn.commit()


def get_support(id):
	sql = "SELECT * FROM support"
	cursor.execute(sql)
	a = cursor.fetchall()
	if not a:
		return("В данный момент в поддержке нету вопросов.")
	else:
		for i in a:
			smg = "\nНомер тикета: " + str(i[0])
			smg = smg + "\nСуть вопроса: " + str(i[1] + "\n")
			send_message(id, smg)
		return("Список обращений в поддержке")

def send_support(id, idd, text):
	print(idd)
	sql = "SELECT user_id FROM support WHERE user_id=?"
	cursor.execute(sql, [str(idd)])
	a = cursor.fetchone()
	if a is not None:
		smg = "Ответ поддержки: \n\n" + str(text)
		send_message(idd, str(smg))
		sql = "DELETE FROM support WHERE user_id=?"
		cursor.execute(sql, [str(idd)])
		conn.commit()
		return("Сообщение отправлено")
	else:
		return("Пользователь не задавал вопрос!")

def write_support(id, text):
	sql = "SELECT user_id FROM support WHERE user_id=?"
	cursor.execute(sql, [str(id)])
	a = cursor.fetchone()
	if a is not None:
		return("Вы уже отправляли сообщение в поддержку. Новое вы сможете отправить после ответа!")
	else:
		params = (str(id), text)
		cursor.execute("INSERT INTO support VALUES (?, ?)", params)
		conn.commit()
		send_message(str(st.alert_id), str(st.alert_message + "\nЕго ID: " + str(id)+ str("(" + get_name(id) + ")")))
		return("Ваше сообщение отправленно в поддержку, ожидайте ответа!")


def admin_check(id):
	sql = "SELECT admin FROM data WHERE user_id=?"
	cursor.execute(sql, [str(id)])
	a = cursor.fetchall()
	b = a[0][0]
	if b == 1:
		return(1)
	elif b == 2:
		return(2)
	else:
		return(0)

def getstat():
	sql = "SELECT * FROM data WHERE user_id"
	cursor.execute(sql)
	b = cursor.fetchall()
	n = 0
	for i in b:
		n = n + 1
	#print(n)
	sql = "SELECT all_msg FROM data"
	cursor.execute(sql)
	c = cursor.fetchall()
	a = 0
	for tup in c:
		a += tup[0]
	smg = "Кол-во людей: " + str(n)
	smg = smg + "\nКол-во сообщений: " + str(a)
	return(smg)