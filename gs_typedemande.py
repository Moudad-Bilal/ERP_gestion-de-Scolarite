from openerp.osv import osv,fields

class gs_typedemande(osv.osv):
    _name = 'gs.typedemande'
    _columns = {
        'id': fields.char('id', size=64 ),        
        'name': fields.char('name', size=64,required=True ),
           
       

        #Relation entre les models
        'ref_demande': fields.one2many('gs.demande','ref_typedemande',string='demande'),

    }
   
    

gs_typedemande()

