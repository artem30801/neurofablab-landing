import os
import json
import configparser

import sanic
from sanic import Sanic
from sanic import response

import telegram
from telegram.ext import Updater

import sql_interact

config = configparser.ConfigParser()
config.read("config.ini")

token = config["TELEGRAM"]["token"]
dialog_id = config["TELEGRAM"]["dialog_id"]
proxy = config["TELEGRAM"]["proxy"]

bot = Updater(token=token, request_kwargs={'proxy_url': proxy})
web_path = "web/"
assests_path = web_path + "assests/"

app = Sanic()

app.static('/assests', assests_path)

app.static('/style.css', web_path+"style.css", name='css')
app.static('/script.js',  web_path+"script.js", name='js')
app.static('/robots.txt',  web_path+"robots.txt", name='robots')


@app.route("/")
async def index(request):
    return response.html(open(os.path.abspath(web_path+'landing.html'), encoding='utf-8').read())


@app.route("/landing")
async def reader_page(request):
    return response.redirect('/')


@app.route("/writeback", methods=["POST", ])
async def writeback(request):
    try:
        args = json.loads(request.body)
        name, phone = args.get("name"), args.get("phone")

        msg = "Новый запрос по форме обратной связи!\nИмя: '{}'; Телефон: {}\nIP-адресс отправителя: {}".format(
            name, phone, request.ip
        )

        sql_interact.insert_writeback(name, phone)

        result = bot.bot.send_message(chat_id=dialog_id, text=msg)

    except Exception as e:
        return response.json({'result': 'На сервере произошла ошибка {} :(\n'
                                        'Пожалуйста, сообщите нам об этом!'.format(e)})
    else:
        if result:
            return response.json({'result': 'Мы перезвоним Вам в ближайшее время!'})
        else:
            return response.json({'result': 'Не удалось отправить данные :('})


def start():
    ip = '0.0.0.0'
    app.run(host=ip, port=80)


if __name__ == "__main__":
    start()
