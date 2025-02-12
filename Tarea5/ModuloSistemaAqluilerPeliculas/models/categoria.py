from odoo import models, fields

class Categoria(models.Model):
    _name = 'alquiler.categoria'
    _description = 'Categoría de Película'

    name = fields.Char(string="Nombre", required=True)
    descripcion = fields.Text(string="Descripción")
    categoria_id = fields.Many2one('alquiler.categoria', string="Categoría")

    

