from django.db import connection
from django.conf import settings
from django.template import Template, Context
import os


# def terminal_width():
#     """
#     Function to compute the terminal width.
#     WARNING: This is not my code, but I've been using it forever and
#     I don't remember where it came from.
#     """
    # width = 0
    # try:
    #     import struct, fcntl, termios
    #     s = struct.pack('HHHH', 0, 0, 0, 0)
    #     x = fcntl.ioctl(1, termios.TIOCGWINSZ, s)
    #     width = struct.unpack('HHHH', x)[1]
    # except:
    #     pass
    # if width <= 0:
    #     try:
    #         width = int(os.environ['COLUMNS'])
    #     except:
    #         pass
    # if width <= 0:
    #     width = 80
    # return width


class SQLLogToConsoleMiddleware:
    def process_response(self, request, response):
        if settings.DEBUG and connection.queries:
            time = sum([float(q['time']) for q in connection.queries])
            t = Template("{% for sql in sqllog %}{{sql.sql|safe}}{% if not forloop.last %}\n\n{% endif %}{% endfor %}")
            print(t.render(Context({'sqllog':connection.queries,'count':len(connection.queries),'time':time})))
            with open('SQLscript.txt', 'a') as sqlcodefile:
                sqlcodefile.write(t.render(Context({'sqllog':connection.queries,'count':len(connection.queries),'time':time})))
            sqlcodefile.close()
        return response