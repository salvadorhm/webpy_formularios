import web

urls = (
    '/', 'Index'
)

app = web.application(urls, globals())
render = web.template.render('views')

class Index:
    def GET(self):
        return render.index()

    def POST(self):
        formulario = web.input()
        return formulario.nombre

if __name__ == "__main__":
    app.run()
