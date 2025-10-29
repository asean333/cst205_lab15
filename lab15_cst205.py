#from flask import Flask
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def hello():
    return     '''
    <h1>Hello World!</h1>
    <p>Anthony Cervantes : LOVEMUFFIN (League Of Villainous Evildoers Maniacally United For Frightening Investments in Naughtiness)</p>
    <p>Annalise Sean : LASER (Light Amplification by Stimulated Emission of Radiation)</p>
'''
# I don't have anyone elses' contacts and the people I'd asked in class weren't sure at the time ^^;


@app.route('/annalise')
def annalise():
    return render_template('template.html')

if __name__ == '__main__':
    app.run(debug=True)