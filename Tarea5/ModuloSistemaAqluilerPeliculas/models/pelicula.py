from odoo import models, fields

class Pelicula(models.Model):
    _name = 'alquiler.pelicula'
    _description = 'Película'

    name = fields.Char(string="Título", required=True)
    descripcion = fields.Text(string="Descripción")
    fecha_estreno = fields.Date(string="Fecha de Estreno")
    duracion = fields.Integer(string="Duración (minutos)")
    categoria_id = fields.Many2one('alquiler.categoria', string="Categoría")
    actor_ids = fields.Many2many('alquiler.actor', string="Actores")
    estado = fields.Selection([
        ('disponible', 'Disponible'),
        ('alquilado', 'Alquilado'),
        ('reservado', 'Reservado')
    ], string="Estado", default='disponible')
    
    # Agregamos el campo de tipo de película
    tipo_pelicula = fields.Selection([
        ('accion', 'Acción'),
        ('comedia', 'Comedia'),
        ('drama', 'Drama'),
        ('terror', 'Terror')
    ], string="Tipo de Película", required=True, default='accion', help="Selecciona el tipo de la película.")
