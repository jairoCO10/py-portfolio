from fasthtml.common import *
from components import navbar
from components import footer

def container():
    # Crear el contenedor principal con la clase "container"
    container = Div(
        # Crear el elemento <nav> con el id "header"
        navbar.nav(),
        footer.footer(),
        cls="container",
    )
    return container


def main(args=None):
    return Main(
         Section(
            Div(Div( Span("Jairo Cogollo"), cls="featured-text-card"),),
            cls="featured-box",
            id = "home"
             
         ),

        cls="wrapper"
    )