from flask import Flask
app = Flask(__name__)
#appには<Flask 'index'>という値が入っていて、これはindex.pyから拡張子を抜いた形で,
#Flaskがどのfileを見ればいいのかが識別できるようにしている

#ここからルーティング設定。/にアクセスすると、index()が実行されるようになっている。
@app.route("/") 
def index():
	return ('<h1>hello. world</h1>') #デフォルトがhtml形式なので自動で変換される

#ポート設定。デバッグモードをONに。
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80, debug=True)
	
	