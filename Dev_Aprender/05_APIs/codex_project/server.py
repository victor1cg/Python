#
# TODO https://www.youtube.com/watch?v=NKJV0ekmo4U&ab_channel=TheCodex

from flask import Flask, render_template

#initialize application STANDARD
app = Flask (__name__)

#routing
@app.route('/')         #creating a route on our server that is just single slash - HOME (Local Host)
def home():
    return 'Hello My Blog '

@app.route('/about')         #another page 
def about():
    return 'The About page'

#* Posso usar diretamente o codigo, ou melhor aind chamar o arquivo HTML;
""" @app.route('/blog')
def blog():                     
    return '''
    <html>
    <head> <h2>Victor Blog </h2></head><br>
    <body> I am Victor, the author of this blog </body>
    </html>
    ''' """
@app.route('/blog')
def blog():                     
    return render_template('blog.html', author = 'Bob', sunny=True) #author é a variavel que eu passei no HTML.

#* Creating a lot pages
@app.route('/blog/<blog_id>')
def blogpost(blog_id):
    return 'This is blogpost number ' + str(blog_id)

#! Testing the app
if __name__ == '__main__':  
    app.run()