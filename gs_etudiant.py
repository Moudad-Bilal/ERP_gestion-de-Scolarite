from openerp.osv import osv,fields

class gs_etudiant(osv.osv):
    _name = 'gs.etudiant'
    _columns = {
        'id': fields.char('Code', size=64 ),
        'name': fields.char('name', size=64,required=True ),
        'niveau': fields.selection(selection=[('ap1', 'AP1'),('ap2', 'AP2'),('ci1', 'Ci1'),('ci2', 'Ci2'),('ci3', 'Ci3')], string='niveau', default='AP1'),
        'filiere': fields.selection(selection=[('ap', 'AP'),('gc', 'GC'),('gi', 'GI'),('geer', 'GEER'),('g2e', 'G2e')], string='filiere', default='ap'),
        'email': fields.char('email', size=64,required=True ),
        'date_inscription': fields.date('Date d\'inscription'),     

        #Relation entre les models
        # 'ref_departement': fields.many2one('prcinf.departement','Departement',ondelete='cascade'),
        # 'ref_brand': fields.many2one('prcinf.brand','Marque',ondelete='cascade'),
        # 'ref_responsable': fields.many2one('prcinf.responsable','Responsable',ondelete='cascade'),
        # 'ref_salle': fields.many2one('prcinf.salle','Salle'),
        'ref_demande': fields.one2many('gs.demande','ref_etudiant',string='demande'),
        # 'ref_fournisseur': fields.many2one('prcinf.fournisseur','Fournisseur',ondelete='cascade'),
        # 'ref_stock': fields.many2one('prcinf.stock','Stock',ondelete='cascade'),
        # 'ref_reseau': fields.many2one('prcinf.reseau','Reseau',ondelete='cascade'),
    }
   
    

gs_etudiant()

