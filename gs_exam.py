from openerp.osv import osv,fields

class gs_exam(osv.osv):
    _name = 'gs.exam'
    _columns = {
        'id': fields.char('id', size=64 ),
        'module': fields.selection(selection=[('module1', 'Module1'),('module2', 'Module2'),('module3', 'Module3'),('module4', 'Module4'),('module5', 'Module5')], string='module', default='module1'),
        'salle': fields.char('salle', size=64,required=True ),
        'prof': fields.char('prof', size=64,required=True ),
        'dure': fields.float('dure'), 
        'date': fields.date('date'),     
       

        #Relation entre les models
  
        'ref_classe': fields.many2one('gs.classe','Classe',ondelete='cascade'),
        # 'ref_prof': fields.one2many('gs.prof','ref_exam',string='Prof'),
        # 'ref_departement': fields.many2one('prcinf.departement','Departement',ondelete='cascade'),
        #'ref_classe': fields.many2one('gs.exam','Exam',ondelete='cascade'),
        # 'ref_responsable': fields.many2one('prcinf.responsable','Responsable',ondelete='cascade'),
        # 'ref_salle': fields.many2one('prcinf.salle','Salle'),
       # 'ref_demande': fields.one2many('gs.demande','ref_etudiant',string='demande'),
        # 'ref_fournisseur': fields.many2one('prcinf.fournisseur','Fournisseur',ondelete='cascade'),
        # 'ref_stock': fields.many2one('prcinf.stock','Stock',ondelete='cascade'),
        # 'ref_reseau': fields.many2one('prcinf.reseau','Reseau',ondelete='cascade'),
    }
   
    

gs_exam()

