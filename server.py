import os
import json

import sanic
from sanic import Sanic
from sanic import response

import telegram
from telegram.ext import Updater

bot = Updater(token='', request_kwargs={
    'proxy_url': 'socks5://95.216.224.183:1080/'})  #TODO load

web_path = "web/"
assests_path = web_path + "assests/"

app = Sanic()

app.static('/assests', assests_path)

app.static('/style.css', web_path+"style.css", name='css')
app.static('/script.js',  web_path+"script.js", name='js')


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

        msg = "Новый запрос по форме обратной связи!\nИмя: '{}', телефон: {}\nIP-адресс отправителя: {}".format(
            name, phone, request.ip
        )
        result = bot.bot.send_message(chat_id="-356071675", text=msg)  #TODO config

    except Exception as e:
        return response.json({'result': 'На сервере произошла ошибка {} :('.format(e)})
    else:
        if result:
            return response.json({'result': 'Скоро с Вами свяжутся!'})
        else:
            return response.json({'result': 'Не удалось отправить данные :('})




def start():
    ip = '0.0.0.0'
    app.run(host=ip, port=80)


if __name__ == "__main__":
    start()
