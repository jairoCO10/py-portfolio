
const projects = [
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
    }
];

function openModal(idx) {
    const project = projects[idx];

    // Asignar la información al modal
    document.getElementById('modal-title').innerText = project.title;
    document.getElementById('modal-description').innerText = project.label;

    // Mostrar el modal
    document.getElementById('project-modal').style.display = 'block';
}

// Función para cerrar el modal
function closeModal() {
    document.getElementById('project-modal').style.display = 'none';
}

// Asignar el evento de clic al botón de cierre una vez que el DOM esté listo
document.addEventListener("DOMContentLoaded", function () {
    const closeButton = document.querySelector('.modal-close');
    if (closeButton) {
        closeButton.addEventListener('click', closeModal);
    }
});

// También se puede cerrar el modal si se hace clic fuera de la caja
window.onclick = function (event) {
    const modal = document.getElementById('project-modal');
    if (event.target == modal) {
        modal.style.display = 'none';
    }
}
