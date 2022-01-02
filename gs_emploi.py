from openerp.osv import osv,fields

class gs_emploi(osv.osv):
    _name = 'gs.emploi'
    _columns = {
               
        'emploi': fields.binary('emploi du temps'),
        'date': fields.date('last update'),
           
       

        #Relation entre les models
        'ref_classe': fields.many2one('gs.classe','Classe'),
        'ref_exam': fields.one2many('gs.exam','ref_classe',string='exam'),
      
    }
   
    

gs_emploi()

