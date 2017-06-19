from app import app, db
from flask import abort, jsonify
from flask_sqlalchemy import SQLAlchemy as sa
from .models import Jadwal, Ruangan, Pengawas, Penjaga
from datetime import datetime

@app.route('/absen/<rfid>', methods=['GET'])
def absen(rfid):
	kueri = db.session.query(Penjaga, Pengawas).filter(Pengawas.rfid == rfid)\
				.filter(Pengawas.id_pengawas == Penjaga.id_pengawas)\
				.first()
	if not kueri:
		abort(400)

	print(kueri)
	kueri[0].absen = 1
	db.session.commit()
	return 'YA';