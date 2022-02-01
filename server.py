from flask import Flask,render_template,request,redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route("/")
def my_home():
    return render_template("index.html")

@app.route("/<string:name_pag>")
def html(name_pag):
    return render_template(name_pag)
def write_file(data):
    with open("database.txt",mode='a') as database:
        email=data['email']
        subject=data['subject']
        message=data['message']
        file=database.write(f'\n{email},{subject},{message}')
 
def write_file_to_csv(data):
    with open("database.csv",mode='a',) as database2:
        email=data['email']
        subject=data['subject']
        message=data['message']
        csv_writer=csv.writer(database2,delimiter=',' , newline='', quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method=="POST":
        data=request.form.to_dict()
        write_file_to_csv(data)
        return redirect("/thankyou.html")
    else:
        return 'wrong'
