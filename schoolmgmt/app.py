from flask import Flask, render_template, abort

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# Register an error handler for an exception class
@app.errorhandler(Exception)
def internal_server_error(error):
    app.logger.error(f"An unhandled error occurred: {error}")
    if request.is_json:
        return jsonify(message="An internal server error occurred."), 500
    return render_template('500.html'), 500

@app.route("/")
def hello():
    return "Hello, World!"


@app.route('/app/data/<name>', methods=['GET'])
def getData(name):
	return '{}'.format(name)
