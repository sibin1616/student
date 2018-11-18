from flask import Flask, render_template,request
from data import student
app=Flask(__name__)
getstudent=student()
@app.route('/send',methods=['GET','POST'])
def send():
    if(request.method=='POST'):
        getName=request.form['name']
        
        getName1=request.form['mobile']
        
        getName2=request.form['email']
       
        getName3=request.form['subject']
        
        getName4=request.form['messsage']
        return render_template('result.html',newname=getName,newname1=getName1,newname2=getName2,newname3=getName3,newname4=getName4)

@app.route('/')
def index():
    return render_template('home.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact')
def contac():
    return render_template('contact.html')
@app.route('/slist')
def slist():
    return render_template('slist.html',mylist=getstudent)
if(__name__=='__main__'):
    app.run(debug=True)