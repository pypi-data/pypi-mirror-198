"""
Run the example code in the documentation online
"""
from functools import partial
from os import path, listdir

from pywebio import start_server
from pywebio.platform import config
from pywebio.session import local as session_local, info as session_info

##########################################
# Pre-import modules for demo
import time  # lgtm [py/unused-import]
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *
from pywebio_battery import *

##########################################


def t(eng, chinese):
    """return English or Chinese text according to the user's browser language"""
    return chinese if 'zh' in session_info.user_language else eng


here_dir = path.dirname(path.abspath(__file__))


def gen_snippets(code):
    code = code.replace('# ..demo-only', '')
    code = '\n'.join(i for i in code.splitlines() if '# ..doc-only' not in i)

    parts = code.split('\n## ----\n')
    for p in parts:
        yield p.strip('\n')


def run_code(code, scope):
    with use_scope(scope):
        try:
            """
            Remember that at module level, globals and locals are the same dictionary. 
            If exec gets two separate objects as globals and locals, 
            the code will be executed as if it were embedded in a class definition.
            https://docs.python.org/3/library/functions.html#exec
            """
            exec(code, session_local.globals)
        except Exception as e:
            toast('Exception occurred: "%s:%s"' % (type(e).__name__, e), color='error')


IMPORT_CODE = """from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *

def main():
    %s

start_server(main, port=8080, debug=True)
"""


def copytoclipboard(code):
    code = IMPORT_CODE % code.replace('\n', '\n    ')
    run_js("writeText(text)", text=code)
    toast('The code has been copied to the clipboard')


def handle_code(code, title):
    run_js("""
    window.writeText = function(text) {
        const input = document.createElement('textarea');
        input.style.opacity  = 0;
        input.style.position = 'absolute';
        input.style.left = '-100000px';
        document.body.appendChild(input);

        input.value = text;
        input.select();
        input.setSelectionRange(0, text.length);
        document.execCommand('copy');
        document.body.removeChild(input);
        return true;
    }
    """)
    session_local.globals = dict(globals())
    if title:
        put_markdown('## %s' % title)

    for p in gen_snippets(code):
        with use_scope() as scope:
            put_code(p, 'python')

            put_buttons([t('Run', '运行'), t("Copy to clipboard", '复制代码')], onclick=[
                partial(run_code, code=p, scope=scope),
                partial(copytoclipboard, code=p)
            ])

        put_markdown('----')


def get_app():
    """PyWebIO demos from document

    Run the demos from the document online.
    """
    app = {}
    try:
        demos = listdir(path.join(here_dir, 'doc_demos'))
    except Exception:
        demos = []

    for name in demos:
        code = open(path.join(here_dir, 'doc_demos', name)).read()
        title, code = code.split('\n\n', 1)
        app[name] = partial(handle_code, code=code, title=title)
        app[name] = config(title=name, description=title)(app[name])

    return app


main = get_app()
if __name__ == '__main__':
    start_server(main, debug=True, port=8080)
