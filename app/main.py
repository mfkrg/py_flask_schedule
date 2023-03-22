from flask import Flask, Response
from cache import get_cached_schedule, cache_schedule
from schedule_gen import schedule_png_gen

app = Flask(__name__)

@app.route('/schedule/<group>')
def schedule(group):
    png_image = get_cached_schedule(group)
    if png_image:
        return Response(png_image, mimetype='image/png')
    else:
        html_file = f'schedules/{group}.html'
        schedule_png_gen(html_file, group)
        png = get_cached_schedule(group)
        return Response(png, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True, port=8800)