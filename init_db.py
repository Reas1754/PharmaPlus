from app import app, db
from database import Obat

# Inisialisasi database
with app.app_context():
    db.create_all()
    sample_data = [
        Obat(nama="Paracetamol", fungsi="Meredakan demam dan nyeri"),
        Obat(nama="Ibuprofen", fungsi="Anti-inflamasi dan pereda nyeri"),
        Obat(nama="Amoxicillin", fungsi="Antibiotik untuk infeksi bakteri"),
        Obat(nama="Cetirizine", fungsi="Mengurangi reaksi alergi"),
        Obat(nama="Omeprazole", fungsi="Mengatasi asam lambung berlebih"),
    ]
    db.session.bulk_save_objects(sample_data)
    db.session.commit()
    print("✅ Database berhasil diinisialisasi dengan data obat!")
