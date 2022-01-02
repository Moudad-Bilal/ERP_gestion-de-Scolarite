{
'name' : "GESTION DE SCOLARITE ENSAH",
'version' : '1.0',
'author' : 'YASSINE EL ACHABY, MOUDAD BILAL',
'category' : 'ENSAH ERP',
'sequence' :1,
'icon': "gs/static/src/img/download.png",
'description' : """
Module GESTION DE SCOLARITE ENSAH
=====================================================
Ce module couvre les éléments suivants:
------------------------------------------------------
* Gestion des etudiants
* Gestion des filieres
* Gestion des classes
* Gestion des demandes
""",
'website': 'http://www.ensah.ma',
'images' : [''],
'depends' : ['base'],
'data':['gs_etudiant_view.xml','gs_demande_view.xml','gs_exam_view.xml','gs_classe_view.xml','gs_typedemande_view.xml','gs_emploi_view.xml'],#,'gs_prof_view.xml'
'update_xml': [],
'js': ['static/src/js/main.js'],
'qweb' : [],
'css':['static/src/css/main.css'],
'demo': [],
'test': [],
'installable': True,
'auto_install': False,
}