from flask import Flask , render_template ,url_for , request , redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template("index.html")

#important
@app.route('/<string:page_name>')
def html_page(page_name):

    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return "did not save to database"
    else:
        return "something went wrong"


def write_to_file(data):
    with open('database.txt', mode='a') as database: #with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        message = data["message"]
        subject = data["subject"]
        file = database.write(f" \n {email},{message},{subject}")

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:

        email = data["email"]
        message= data["message"]
        subject= data["subject"]
        csv_writer = csv.writer(database2,delimiter="," , quotechar='"' ,quoting= csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,message,subject])

