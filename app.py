from flask import Flask, render_template, request
from data import locations,property_type
from prediction import prediction


## translatr flask to python object
app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/',methods=['GET','POST'])
def index_prediction():
    if request.method =='POST':
        data = request.form
        data = data.to_dict()
        data['humidity']= int(data['humidity'])
        data['wind'] = int(data['wind'])
        data['rain'] = int(data['rain'])
        data['clouds'] = int(data['clouds'])
        data['temp'] = int(data['temp'])
        hasil = prediction(data)
        #hasilIDR = hasil*3564.67
        return render_template('result.html',hasil_prediction=hasil)
    return render_template('prediction.html',data_location=locations,
    data_property=sorted(property_type))

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True,port=2704)



