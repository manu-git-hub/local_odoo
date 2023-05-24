from odoo import models, fields

class CompanyGoal(models.Model):
    _name = 'company.goal'
    _description = 'Company Goals'

    name = fields.Char(string='Goal', required=True)
    description = fields.Text(string='Description')
    deadline = fields.Date(string='Deadline')
