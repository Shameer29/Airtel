from flask import *  
   
app = Flask(__name__)  
  
@app.route('/')
def Welcome():
    return 'Welcome' 
  
@app.route('/Process')  
def librarion():  
    return 'Process1'  
  
  
@app.route('/user/<name>')  
def user(name):  
    if name == '/':  
        return redirect(url_for('/'))  
    if name == 'Process':  
        return redirect(url_for('Process'))  
if __name__ =='__main__':  
    app.run(debug = True)  