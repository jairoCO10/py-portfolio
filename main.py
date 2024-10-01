from fasthtml.common import *
from container import *
from style import *
from page import blog
# Add the HighlightJS built-in header
hdrs = (HighlightJS(langs=['python', 'javascript', 'html', 'css']),)

app, rt = fast_app()


def create_page():
    html = common.Html(
        common.Head(StyleX('styles.css'),
                    Link(rel="stylesheet",
                         href = "https://unicons.iconscout.com/release/v4.0.8/css/line.css"),
                    ScriptX('main.js', 'modal.js')),
                   
        common.Body(container(),
                     ),  # Body con el contenido principal
    )
    return html

@rt('/')
def get(req):
    return create_page()


@rt('/blogs')
def get(req):
    return blog.container()

serve()