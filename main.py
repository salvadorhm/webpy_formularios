import web

urls = (
    '/', 'Index'
)
app = web.application(urls, globals())

class Index:
    def GET(self):
        pagina = "<html><body>hola</body></html>"
        return pagina

if __name__ == "__main__":
    app.run()
