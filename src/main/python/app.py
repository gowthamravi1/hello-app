from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    
    app.logger.info('/')
    # Render default page template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)