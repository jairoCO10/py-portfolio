from fasthtml.common import *

def nav():
    return  Nav(
            # Crear el div con la clase "nav-logo"
            Div(P("Jairo", cls="nav-name"),Span("."),cls="nav-logo"),
            Div(
                Ul(
                    Li(
                        A("Home",href="#home",cls="nav-link active-link"),
                        Div(cls="circle"),
                        cls="nav_list",
                    ),
                    Li(
                        A("about",href="#about",cls="nav-link active-link"),
                        Div(cls="circle"),
                        cls="nav_list",
                    ),
                    Li(
                        A("projects",href="#projects",cls="nav-link active-link"),
                        Div(cls="circle"),
                        cls="nav_list",
                    ),
                    Li(
                        A("contact",href="#contact",cls="nav-link active-link"),
                        Div(cls="circle"),
                        cls="nav_list",
                    ),
                    Li(
                        A("Blogs",href="blogs",cls="nav-link active-link"),
                        Div(cls="circle"),
                        cls="nav_list",
                    ),
                    cls="nav_menu_list",

                ),
                id="myNavMenu",
                cls="nav-menu"

            ),
            Div(
                Button(
                    "Download CV",
                    I(cls="uil uil-file-alt"),
                    cls="btn"),
                cls="nav-button"
            ),
            Div(
                I(
                    cls="uil uil-bars",
                    onclick=("myMenuFunction()")
                  ),
                cls="nav-menu-btn"
            ),
            id="header",
        )

