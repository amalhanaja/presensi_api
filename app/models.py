from app import app, db
import hashlib

class Petugas(db.Model):
	__tablename__ = 'petugas'

	id_petugas = db.Column(db.Integer, primary_key=True)
	nip = db.Column(db.Integer, unique=True)
	nama = db.Column(db.String)
	password = db.Column(db.String)

	def __repr__(self):
		return '<Petugas %r>' % self.nip

	def verify_password(self, password):
		m = hashlib.md5(password.encode())
		diggest_password = m.hexdigest()
		print (diggest_password)
		return self.password == diggest_password

class Jadwal(db.Model):
	__tablename__ = 'jadwal'

	id_jadwal = db.Column(db.Integer, primary_key=True)
	id_ruangan = db.Column(db.Integer, db.ForeignKey('raungan.id_ruangan'))
	waktu_awal = db.Column(db.String)
	waktu_akhir = db.Column(db.String)

	# penjaga = db.relationship('Penjaga' , backref='jadwal', lazy='dynamic')

	def __repr__(self):
		return '<Jadwal %r>' % self.id_jadwal

class Ruangan(db.Model):
	__tablename__ = 'raungan'

	id_ruangan = db.Column(db.Integer, primary_key=True)
	nama_ruangan = db.Column(db.String(16))
	lokasi = db.Column(db.String(64))
	tipe = db.Column(db.String(250))

	jadwal_ruangan = db.relationship('Jadwal', backref='raungan', lazy='dynamic')

	def __repr__(self):
		return '<Ruangan %r>' % self.id_ruangan
class Pengawas(db.Model):
	__tablename__ = 'pengawas'

	id_pengawas =  db.Column(db.Integer, primary_key=True)
	nip = db.Column(db.Integer, unique = True)
	nama = db.Column(db.String(250))
	status = db.Column(db.String(32))
	rfid = db.Column(db.Integer)
	ruangan = db.Column(db.Integer)

	penjaga = db.relationship('Penjaga', backref='pengawas', lazy='dynamic')

	def __repr__(self):
		return '<Pengawas %r>' % self.id_pengawas

class Penjaga(db.Model):
	__tablename__ = 'penjaga'

	id_penjaga = db.Column(db.Integer, primary_key=True)
	id_jadwal = db.Column(db.Integer, db.ForeignKey('jadwal.id_jadwal'))
	id_pengawas = db.Column(db.Integer, db.ForeignKey('pengawas.id_pengawas'))
	absen = db.Column(db.Integer)

	jadwal_penjaga = db.relationship('Jadwal', backref='penjaga')

	def __repr__(self):
		return '<Penjaga %r>' % self.id_penjaga