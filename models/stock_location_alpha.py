from odoo import api, fields, models


class StockLocationAlpha(models.Model):
    _inherit = 'stock.location'

    posx = fields.Char('Corridor (X)', default=0, help="Optional localization details, for information purpose only")
    posy = fields.Char('Shelves (Y)', default=0, help="Optional localization details, for information purpose only")
    posz = fields.Char('Height (Z)', default=0, help="Optional localization details, for information purpose only")
