# _*_ coding: utf-8 _*_
{
    'name': 'Gestión de Alquiler de Películas',
    'version': '1.0',
    'summary': 'Módulo para gestionar el alquiler de películas, categorías y actores en Odoo',
    'author': 'Windsor',
    'category': 'Gestión',
    'depends': ['base'],  # Asegúrate de que dependencias como 'base' sean suficientes
    'data': [

        # Seguridad
        'security/ir.model.access.csv',  # Define los accesos a los modelos
        'security/security_groups.xml',  # Define los permisos de acceso

        # Vistas
        'views/pelicula_views.xml',
        'views/categoria_views.xml',
        'views/actor_views.xml',
        'views/menus.xml',
        'views/report_pelicula.xml',
        'views/actor_search.xml',
        'views/actor_kanban.xml',

        # Datos
        'data/categorias_data.xml',  # Datos iniciales de categorías
        'data/datos_ejemplo.xml',  # Otros datos de ejemplo para películas y actores
        'data/access_control.xml',  # Configuración de permisos de acceso (revisa si este archivo está bien configurado)

    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

