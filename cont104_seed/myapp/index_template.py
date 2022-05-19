from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") 
def index():
	return render_template('index.html')
#templatesディレクトリ内の上記のファイル(index.htmlファイル)がレンダリングされる仕組み。

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80, debug=True)
	
	