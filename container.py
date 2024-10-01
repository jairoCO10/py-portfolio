from fasthtml.common import *
from components import navbar
from components import footer
from info  import info_me

def container():
    # Crear el contenedor principal con la clase "container"
    container = Div(
        # Crear el elemento <nav> con el id "header"
        navbar.nav(),
        main(),
        footer.footer(),
        cls="container",
    )
    return container


def main():
    response = info_me()
    lenguajes = response['Lenguajes']
    # Generar dinámicamente los spans para cada lenguaje
    lenguajes_html = Div(
        *[Span(lenguaje) for lenguaje in lenguajes], cls="skills-list"
    )
    dbs = response["db"]
    db_html = Div(
        *[Span(db) for db in dbs],  cls="skills-list"
    )
    frameworks = response["Frameworks"]
    frameworks_html = Div(
        *[Span(framework) for framework in frameworks],  cls="skills-list"
    )
    herramientas = response["Herramientas"]
    herramientas_html = Div(
        *[Span(herramienta) for herramienta in herramientas ],  cls="skills-list"
    )
    
    Infraestructura = response["Infraestructura"]
    Infraestructura_html = Div(
        *[Span(Infra) for Infra in Infraestructura ],  cls="skills-list"
    )


    


    return Main(
        Section(
            Div(
                Div( Span(response["nombre"]), cls="featured-text-card"),
                Div( P("I'm",Span(cls="typedText"), ), cls="featured-name"),
                Div( P(response["intro"]),
                cls="featured-text-info"  
                ),
                # Div(
                #     Button("Hire Me", cls="btn blue-btn"),
                #     Button("Download CV ",I(cls="uil uil-file-alt",), cls="btn"),
                #     cls="featured-text-btn"
                # ),
                Div(
                   Div( I(cls="uil uil-instagram"), cls="icon"),
                   Div( I(cls="uil uil-linkedin-alt"),cls="icon"),
                   Div( I(cls="uil uil-dribbble"),cls="icon"),
                   Div( I(cls="uil uil-github-alt"), cls="icon"),
                   cls="social_icons",
                ),
                
                # Div(
                #     A(P("Scroll Down"), I(cls="uil uil-mouse-alt"),cls="scroll-btn"),
                #    cls="scroll-icon-box",
                # ),
                cls="featured-text",
            ),
            Div(
                Div(
                    Div( Img(src= "image2.png", alt="avatar"), cls="image"),
                    cls="featured-image"
                ),
                cls="featured-text",
            ),
            cls="featured-box",
            id = "home"
        ),
        
        # -- -------------- ABOUT BOX ---------------- --
        Section(
            Div(
                H1("About Me"),
                cls="top-header"
            ),
            Div(
                Div(
                    Div(
                        H3(
                           "My introduction "
                        ),
                         P(response["introduccion"]
                            ),
                        P(
                            response["introduccion2"]
                         ),
                         Div(
                             Button(
                                 "Download CV ",
                                 I(cls="uil uil-import"),
                                 cls="btn"
                             ),
                             cls="about-btn"
                         ),
                        cls="about-info"
                    ),
                    cls="col"
                ),
                Div(
                    Div(
                        Div(
                            H3("Lenguajes"),
                            Div(
                                lenguajes_html,
                                cls="skills-list",
                            ),
                            cls="skills-header"
                        ),
                        
                        cls="skills-box"
                    ),
                    Div(
                        Div(
                            H3("Frameworks"),
                            Div(frameworks_html,
                                cls="skills-list",),
                            cls="skills-header"
                        ),
                        cls="skills-box"
                    ),
                    Div(
                        Div(
                            H3("Bases de Datos"),
                            Div(db_html,
                                cls="skills-list",),
                            cls="skills-header"
                        ),
                        cls="skills-box"
                    ),
                    Div(
                        Div(
                            H3("Herramientas:"),
                            Div(herramientas_html,
                                cls="skills-list",),
                            cls="skills-header"
                        ),
                        cls="skills-box"
                    ),
                    Div(                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
                        Div(
                            H3("Infraestructura y Seguridad:"),
                            Div(Infraestructura_html,
                                cls="skills-list",),
                            cls="skills-header"
                        ),
                        cls="skills-box"
                    ),
                    cls="col"
                ),
                cls="row"
            ),
            id="about",
            cls="section"
        ),
        
        # -- -------------- PROJECT BOX ---------------- --
        Section(
            Div(
                H1("Projects"),
                cls="top-header"
            ),
            Div(
                *data,
                cls="project-container"
            ),

            id="projects",
            cls="section",
            
        ),

        # -- -------------- CONTACT BOX ---------------- --
        cls="wrapper"
    )


projects = [
    {
        "icon": "uil uil-briefcase-alt",
        "title": "Completed",
        "label": "15+ Finished Projects",
        "clss": "project-box"
    },
    {
        "icon": "uil uil-laptop",
        "title": "In Progress",
        "label": "5 Ongoing Projects",
        "clss": "project-box"
    },
    {
        "icon": "uil uil-chart",
        "title": "Upcoming",
        "label": "3 Planned Projects",
        "clss": "project-box"
    },
    {
        "icon": "uil uil-chart",
        "title": "Upcoming",
        "label": "3 Planned Projects",
        "clss": "project-box"
    }
]

modal = Div(
    Div(
        Div(
            I(cls="uil uil-times modal-close"),  # Botón para cerrar
            H2("Project Details", id="modal-title"),
            P("", id="modal-description"),
            Div(id="modal-extra-info"),
            cls="modal-content"
        ),
        cls="modal-box"
    ),
    cls="modal",
    id="project-modal"
)

# Añadir el modal al final de la estructura HTML


# Función para crear los divs dinámicamente
def create_project_divs(projects):
    divs = []
    for idx, project in enumerate(projects):
        divs.append(
            Div(
                I(cls=project['icon']),
                H3(project['title']),
                Label(project['label']),
                cls=project['clss'],
                onclick=f"openModal({idx})"  # Llama a una función JS pasando el índice del proyecto
            )
        )
    return divs

# Crear la estructura HTML
data = create_project_divs(projects)

data.append(modal)


