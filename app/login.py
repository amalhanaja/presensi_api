from app import app, auth, db
from flask import g, jsonify, abort
from .models import Petugas

@auth.verify_password
def verify_password(nip, password):
	#first try to authenticate by token
	print ('Authentication Petugas')
	#employee = Employee.verify_auth_token(nip)
	#if not employee:
		#try to authenticate with username and password
	petugas = Petugas.query.filter_by(nip = nip).first()
	if not petugas or not petugas.verify_password(password):
		print ('You\'re not Petugas Cannot Login')
		abort(400)
		return False
	#timestamp = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
	db.session.commit()
	#print (timestamp)
	g.petugas = petugas
	print (g.petugas)
	return True


@app.route('/login', methods=['GET'])
@auth.login_required
def login():
	#print (g.petugas)
	#print(g.petugas)
	return jsonify(	id_petugas = g.petugas.id_petugas,
					nip = g.petugas.nip,
					nama = g.petugas.nama
				)