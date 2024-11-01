from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to BrandMatch!</h1>"

@app.route('/about')
def about():
    return "<p>Products List</p>"

# Run the app
if __name__ == "__main__":
    app.run(debug=True)