import sanic
from sanic import Sanic
from sanic import response

web_path = "web/"
assests_path = web_path + "assests/"

app = Sanic()

app.static('/assests', assests_path)

app.static('/style.css', web_path+"style.css", name='css')
app.static('/script.js',  web_path+"script.js", name='js')

@app.route("/")
async def index(request):
    return response.redirect('/landing')

@app.route("/landing")
async def reader_page(request):
    return response.html(open(os.path.abspath(web_path+'landing.html'), encoding='utf-8').read())


def start():
    ip = '0.0.0.0'
    app.run(host=ip, port=80)

if __name__ == "__main__":
    app.start()
