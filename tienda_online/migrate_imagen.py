"""
Agrega la columna imagen a productos sin borrar datos.
Ejecutar una sola vez: python migrate_imagen.py
"""

from sqlalchemy import text
from app import app
from models import db

with app.app_context():
    db.session.execute(text(
        "ALTER TABLE productos ADD COLUMN IF NOT EXISTS imagen VARCHAR(255)"
    ))
    db.session.commit()
    print("Columna imagen lista.")
