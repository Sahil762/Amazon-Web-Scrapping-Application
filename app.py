from flask import Flask, render_template, request
import pandas as pd
import scrape_ebay
import os

app = Flask(__name__)

@app.route('/')
def home():
    print("Current working directory:", os.getcwd())
    print("Files in the current directory:", os.listdir())
    print("Files in the templates directory:", os.listdir('templates'))
    
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    search_query = request.form['search_query']
    scrape_ebay.scrape-amazon(search_query)
    df = pd.read_excel('amazon_shoes_data.xlsx')
    return render_template('results.html', tables=[df.to_html(classes='data')], titles=df.columns.values)

if __name__ == '__main__':
    app.run(debug=True)
