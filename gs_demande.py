from openerp.osv import osv,fields

class gs_demande(osv.osv):
    _name = 'gs.demande'
    _columns = {
        'id':fields.char('id', size=128 ),
        #'type': fields.selection(selection=[('demande_de_stage', 'Demande_de_stage'),('attestation_de_poursuite_etudes', 'Attestation_de_poursuite_etudes '),('releve_de_notes','Releve_de_notes')], string='Type'),
        'date': fields.date('Date demande'),  
        'reponse': fields.binary('reponse  demande'),      

        #Relation entre les models
        'ref_typedemande': fields.many2one('gs.typedemande','Type'),
        
        'ref_etudiant': fields.many2one('gs.etudiant','Etudiant'),
         
      
    }

gs_demande()

