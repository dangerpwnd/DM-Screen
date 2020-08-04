from db import db

# Background Helper Equipment/Tool/Proficiency
equipment_helper = db.Table('Background_has_Equipment',
    db.Column('equipment_id', db.Integer, db.ForeignKey('Equipment.id_equipment'), primary_key=True),
    db.Column('background_id', db.Integer, db.ForeignKey('Background.id_background'), primary_key=True)
)

tool_helper = db.Table('Background_has_Tools',
    db.Column('tool_id', db.Integer, db.ForeignKey('Tool.id_tool'), primary_key=True),
    db.Column('background_id', db.Integer, db.ForeignKey('Background.id_background'), primary_key=True)
)

proficiency_helper = db.Table('Background_has_Proficiencies',
    db.Column('proficiency_id', db.Integer, db.ForeignKey('Proficiency.id_proficiency'), primary_key=True),
    db.Column('background_id', db.Integer, db.ForeignKey('Background.id_background'), primary_key=True)
)
