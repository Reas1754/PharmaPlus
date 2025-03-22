from flask_sqlalchemy import SQLAlchemy

# Buat instance database tanpa menghubungkan ke app Flask dulu
db = SQLAlchemy()

# Model Obat
class Obat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    fungsi = db.Column(db.String(255), nullable=False)
