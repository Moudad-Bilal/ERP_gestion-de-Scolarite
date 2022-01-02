from openerp.osv import osv,fields

class gs_classe(osv.osv):
    _name = 'gs.classe'
    _columns = {
        'id': fields.char('id', size=64 ),
        'niveau': fields.selection(selection=[('ap1', 'AP1'),('ap2', 'AP2'),('ci1', 'Ci1'),('ci2', 'Ci2'),('ci3', 'Ci3')], string='niveau', default='AP1'),
        'filiere': fields.selection(selection=[('ap', 'AP'),('gc', 'GC'),('gi', 'GI'),('geer', 'GEER'),('g2e', 'G2e')], string='filiere', default='ap'),
        'emploi': fields.binary('emploi du temps'), 
           
       

        #Relation entre les models
        'ref_emploi': fields.many2one('gs.emploi','Emploi'),
        
        'ref_exam': fields.one2many('gs.exam','ref_classe',string='exam'),
      
    }
   
    

gs_classe()

