from flask import *
from os.path import exists

H = 'l-hidden'
N = 'none'
E = 'المعلومات المدخلة غير صحيحة'
R = 'مكتملة'
BN1 = 'الموافقة على الطلب'
BN2 = 'اضافة جديد'
T1 = 'خطأ : البيانات المدخلة غير مكتملة'
T2 = 'خطأ : رمز الخدمة تم استخدامه مسبقا'
T3 = 'تم اضافة البيانات بنجاح'

app = Flask(__name__)
@app.route('/', methods = ['GET','POST'])
@app.route('/Home/SickLeave', methods = ['GET','POST'])
def home():
	if request.method == 'POST':
		ID = request.form['RIDN']
		if exists(str(ID)+'.txt'):
			if request.form != 'RIDN':
				file = open(str(ID)+'.txt','r')
				D = file.readlines()
				return render_template('Index.html', PDF=N, INF=H, RIDN=ID, PFNA=D[2], SDA=D[10], TIT=R)
		else:
			return redirect(url_for('error'))
	elif request.method == 'GET':
		return render_template('Index.html', PDF=N, INR=H)

@app.route('/Home/<id>')
def doc(id):
	file = open(str(id)+'.txt','r')
	D = file.readlines()
	return render_template('Index.html', HID=H, INF=H, INR=H, INE=H, RIDN=id, PFNE=D[1], PFNA=D[2], PIDN=D[3], NOD=D[4], DEFR=D[5], DETO=D[6], DAFR=D[7], DATO=D[8], SDE=D[9], SDA=D[10], GE=D[11], GA=D[12], DOBE=D[13], DOBA=D[14], DEEX=D[15], DAEX=D[16], HFNE=D[17], HFNA=D[18], JNE=D[19], JNA=D[20], JPE=D[21], JPA=D[22])

@app.route('/Home/Error')
def error():
	return render_template('Index.html', PDF=N, INF=H, INE=H, TIT=E)
	
@app.route('/Home/Input', methods = ['GET','POST'])
@app.route('/Home/Login')
def input():
	if request.method == 'POST':
		  D0 = request.form['RIDN']
		  D1 = request.form['PFNE']
		  D2 = request.form['PFNA']
		  D3 = request.form['PIDN']
		  D4 = request.form['NOD']
		  D5 = request.form['DEFR']
		  D6 = request.form['DETO']
		  D7 = request.form['DAFR']
		  D8 = request.form['DATO']
		  D9 = request.form['SDE']
		  D10 = request.form['SDA']
		  D11 = request.form['GE']
		  D12 = request.form['GA']
		  D13 = request.form['DOBE']
		  D14 = request.form['DOBA']
		  D15 = request.form['DEEX']
		  D16 = request.form['DAEX']
		  D17 = request.form['HFNE']
		  D18 = request.form['HFNA']
		  D19 = request.form['JNE']
		  D20 = request.form['JNA']
		  D21 = request.form['JPE']
		  D22 = request.form['JPA']
		  if str(D1 and D2 and D3 and D4 and D5 and D6 and D7 and D8 and D9 and D10 and D11 and D12 and D13 and D14 and D15 and D16 and D17 and D18) == '':
		  	if exists(str(D0)+'.txt'):
		  		return render_template('Input.html', HID=H, HID2=H, TIT=T2)
		  	else:
		  		return render_template('Input.html', HID=H, HID2=H, TIT=T1)
		  else:
			  if not exists(str(D0)+'.txt'):
				  Lines = [str(D0), str(D1), str(D2), str(D3), str(D4), str(D5), str(D6), str(D7), str(D8), str(D9), str(D10), str(D11), str(D12), str(D13), str(D14), str(D15), str(D16), str(D17), str(D18), str(D19), str(D20), str(D21), str(D22)]
				  file = open(str(D0)+'.txt','w')
				  file.write('\n'.join(Lines))
				  file.close()
				  return render_template('Input.html', HID=H, TIT=T3)
	return render_template('Input.html', HID1=H)
	
if __name__ == '__main__':
    app.run(port=5005,debug=True)
