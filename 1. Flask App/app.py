from flask import Flask, request, render_template #import your libraries

app = Flask(__name__) #define your app

@app.route('/', methods=['GET']) #this confirms the URL end which will run this bit of code
def method_show_index():

    #render_Template 'renders' your html templates, and you pass it the html filename and any Python values you wish to pass
    return render_template('index.html', value_to_use="What will you add?")

@app.route('/calc', methods=['POST']) #this confirms the URL end is being 'called' in your form
def method_add():

    #retreive values from your form
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    
    #insert your logic here
    value_to_use = num1 + num2

    #render_Template 'renders' your html templates, and you pass it the html filename and any Python values you wish to pass
    return render_template('index.html', value_to_use=value_to_use)
   
    
if __name__ == '__main__': #debugging function
    app.run(debug=True)