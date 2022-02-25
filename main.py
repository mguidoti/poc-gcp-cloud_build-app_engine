from flask import Flask, render_template

from datetime import datetime

# from utils.insert_to_bigquery import create, get_table, read_top_sales, insert_rows

from utils.helper import write, filter_data
from utils.crawler import scrape

app = Flask(__name__)


@app.route('/')
def root():
    # For the sake of example, use static information to inflate the template.
    # This will be replaced with real information in later steps.

    data = [(
            'Check List the journal of biodiversity data',
            'Check List',
            'acaralogia',
            '2021',
            '17',
            '6',
            '1751',
            '1754',
            'article',
            '10.15560/17.6.1751',
            'Pereira',
            'https://checklist.pensoft.net/article/75735/download/pdf/626829',
            'CheckList_17_6_1751-1754.pdf',
            'SCRAPED',
            str(datetime.now())
        )]


    new_data = scrape()
    # print(new_data)
    filtered_data = filter_data(new_data)
    # print(filtered_data)
    write(filtered_data)

    return render_template('index.html')


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)