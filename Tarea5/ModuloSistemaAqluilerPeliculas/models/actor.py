from odoo import models, fields
class Actor(models.Model):
    _name = 'alquiler.actor'
    _description = 'Actor'

    name = fields.Char(string="Nombre", required=True)
    nacionalidad = fields.Char(string="Nacionalidad")
    fecha_nacimiento = fields.Date(string="Fecha de Nacimiento")
    pelicula_ids = fields.Many2many('alquiler.pelicula', string="Películas")
