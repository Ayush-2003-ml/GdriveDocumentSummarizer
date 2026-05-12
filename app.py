import FileSummarizerService.file_summarizer_service as file_summarizer_service
from flask import Flask, render_template, send_file

app = Flask(__name__)

# default route
@app.route('/')
def index():

    _results = file_summarizer_service.FileSummarizerService().generate_summary()
    return render_template(
        "index.html",
        results = _results
    )

# summary csv download route
@app.route('/download')
def download():

    return send_file(
        "summaries.csv",
        as_attachment = True
    )


if __name__ == '__main__':
    app.run(debug = True)