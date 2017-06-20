from app import app, db
from flask import abort, jsonify
from flask_sqlalchemy import SQLAlchemy as sa
from .models import Jadwal, Ruangan, Pengawas, Penjaga
from datetime import datetime

@app.route('/jadwal', methods=['GET'])
def jadwal():
	class Zone(tzinfo):
    def __init__(self,offset,isdst,name):
        self.offset = offset
        self.isdst = isdst
        self.name = name
    def utcoffset(self, dt):
        return timedelta(hours=self.offset) + self.dst(dt)
    def dst(self, dt):
            return timedelta(hours=1) if self.isdst else timedelta(0)
    def tzname(self,dt):
         return self.name
    GMT = Zone(7,False,'GMT')
	sekarang = datetime.now(GMT).strftime('%Y-%m-%d %H:%M:%S')
	print('getJadwal @', sekarang)
	# date_now = datetime.datetime.now().date()
	# schedule = Jadwal.query.filter(Jadwal.waktu_awal <= sekarang).filter(Jadwal.waktu_akhir >= sekarang).all()
	# schedule = db.session.query(Jadwal, Ruangan).filter(Jadwal.waktu_awal <= sekarang).filter(Jadwal.waktu_akhir >= sekarang).join(Ruangan.jadwal_ruangan).all()
	# jadwal_dict = []
	# for s in schedule:
	# 	jadwal_json = {
	# 		"id_jadwal": s[0].id_jadwal,
	# 		"waktu_awal": s[0].waktu_awal.strftime('%Y-%m-%d %H:%M:%S'),
	# 		"waktu_akhir": s[0].waktu_akhir.strftime('%Y-%m-%d %H:%M:%S'),
	# 		"nama_ruangan": s[1].nama_ruangan,
	# 		"lokasi_ruangan": s[1].lokasi,
	# 		"tipe_ruangan": s[1].tipe,
	# 	}	
	# 	jadwal_dict.append(jadwal_json)
	# 	# res_dict = []
	# 	print (s[1].nama_ruangan)
	# return jsonify(jadwal_dict)
	schedules = db.session.query(Jadwal, Ruangan)\
				.filter(Jadwal.waktu_awal <= sekarang)\
				.filter(Jadwal.waktu_akhir >= sekarang)\
				.join(Ruangan.jadwal_ruangan)\
				.all()
				# .filter(Penjaga.id_jadwal == Jadwal.id_jadwal)\
				# .filter(Penjaga.id_pengawas == Pengawas.id_pengawas)\
	schedule_list = []
	# pengawas_list = []
	schedule_id_jadwal = 0
	for schedule in schedules:
		print (schedule)
		schedule_dict = {
			'id_jadwal': schedule[0].id_jadwal,
			'waktu_awal': schedule[0].waktu_awal.strftime('%Y-%m-%d %H:%M:%S'),
			'waktu_akhir': schedule[0].waktu_akhir.strftime('%Y-%m-%d %H:%M:%S'),
			'nama_ruangan': schedule[1].nama_ruangan,
			'lokasi_ruangan': schedule[1].lokasi,
			'tipe_ruangan': schedule[1].tipe
			# 'pengawas': pengawas_list
		}
		# pengawas_dict = {
		# 	'nama': schedule[2].nama,
		# 	'nip': schedule[2].nip,
		# 	'status': schedule[2].status,
		# 	'rfid': schedule[2].rfid,
		# 	'absen': schedule[3].absen
		# }

		schedule_list.append(schedule_dict)

		# if schedule[0].id_jadwal == schedule_id_jadwal:
		# 	schedule_list.pop(len(schedule_list) - 1)
		# 	pengawas_list.append(pengawas_dict)
		# else :
		# 	pengawas_list.remove()
		# 	pengawas_list.append(pengawas_dict)
		# 	# 'nama_pengawas': schedule[2].nama,
		# 	# 'absen': schedule[3].absen
		# print (len(pengawas_list))
		# schedule_id_jadwal = schedule[0].id_jadwal
		#}
	for s in schedule_list:
		print(s)
		# pengawas_dict = {
		# 	'nama': schedule[2].nama,
		# 	'nip': schedule[2].nip,
		# 	'status': schedule[2].status,
		# 	'rfid': schedule[2].rfid,
		# 	'absen': schedule[3].absen
		# }

		pengawasan = db.session.query(Pengawas, Penjaga)\
					.filter(s.get('id_jadwal') == Penjaga.id_jadwal)\
					.filter(Penjaga.id_pengawas == Pengawas.id_pengawas)\
					.all();
		pengawas_list = []
		print (pengawasan)
		for p in pengawasan:
			pengawas_dict = {
				'nama': p[0].nama,
				'nip': p[0].nip,
				'status': p[0].status,
				'rfid': str(p[0].rfid),
				'absen': p[1].absen
			}
			pengawas_list.append(pengawas_dict)

		s.update(pengawas = pengawas_list)
	return jsonify(schedule_list)