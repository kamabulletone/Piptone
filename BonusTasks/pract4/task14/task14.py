
def printClassE(arg):
    res = str(arg.__class__)
    res = res.split("<class '__main__.", 1)[1]
    print("<" + res[:len(res) - 2] + ">")

def printClassO(arg):
    res = str(arg.__class__)
    res = res.split("<class '__main__.", 1)[1]
    print("</" + res[:len(res) - 2] + ">")


class HTML(object):
    def __init__(self):
        pass
    def __enter__(self):
        printClassE(self)
        return self
    def __exit__(self, type, value, traceback):
        printClassO(self)

    def body(self):
        return body()
    def div(self):
        return div()
    def p(self, arg):
        print("<p>" + arg + "</p>")

class body:
    def __init__(self):
        pass
    def __enter__(self):
        printClassE(self)
        return self
    def __exit__(self, type, value, traceback):
        printClassO(self)

class div:
    def __init__(self):
        pass
    def __enter__(self):
        printClassE(self)
        return self
    def __exit__(self, type, value, traceback):
        printClassO(self)





html = HTML()
with html.body():
    with html.div():
        with html.div():
            html.p('Первая строка.')
            html.p('Вторая строка.')
        with html.div():
            html.p('Третья строка.')