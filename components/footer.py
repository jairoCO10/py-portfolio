from fasthtml.common import *

def footer():
    return  Footer(
        Div( P("Jairo Cogollo"), cls="top-footer"
        ),
        Div( 
            Ul(
                Li(
                    A("Home",href="#home"), cls="footer_menu_list",),
                Li(
                    A("About",href="#about"), cls="footer_menu_list",),
                Li( 
                    A("Projects",href="#projects"), cls="footer_menu_list" ),
                Li(
                    A("Contact",href="#contact"),cls="footer_menu_list",),cls="footer-menu",
            ),
            cls="middle-footer"
        ),
        Div(
            Div(I(cls="uil uil-instagram"), cls="icon"),
            Div(I(cls="uil uil-linkedin-alt"),cls="icon"),
            Div(I(cls="uil uil-dribbble"),cls="icon"),
            Div(I(cls="uil uil-github-alt"),cls="icon"),
            cls="footer-social-icons"
        ),
        Div(
            P("Copyright © ",
                A(
                "Jairo Cogollo",
                href="#home",
                style="text-decoration: none;"
                ),
                " - All rights reserved"
            ),
            cls="bottom-footer"
        ),
    )
   