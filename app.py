from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
     dane = {'tytul':'Strona Główna', 'tresc':'Witamy!'}
     return render_template('index.html', tytul=dane['tytul'], tresc=dane['tresc'])

	
@app.route("/about")
def about():
     dane = {'tytul':'O mnie', 'tresc':'Nazywam się Adrian Rosciszewski.'}
     return render_template('omnie.html', tytul=dane['tytul'], tresc=dane['tresc'])

@app.route('/info')
def info():
    posty = [
        {
         'author': {'username': 'Adrian'},
         'body': 'Piekny mamy dzis dzien.'
        },
        {
         'author': {'username': 'Patryk'},
         'body': 'Prawie w calej Polsce pada grad.'
    }]
    dane = {'tytul':'Dane', 'tresc':'Cos tam'}
    return render_template('info.html', tytul=dane['tytul'], tresc=dane['tresc'], posty=posty)
 
@app.route("/kontent")
def kontent():
     dane = {'tytul':'Content', 'tresc':'Duzo roznych rzeczy'}
     return render_template('kontent.html', tytul=dane['tytul'], tresc=dane['tresc'])
	
if __name__ == "__main__":
	app.run()
