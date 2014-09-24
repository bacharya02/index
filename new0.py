from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():

		a=2
		b=4
		d=str(a**b)

		return "<p>Hello World!</p><p>%s - %s</p>"%(d,a)

		return "Bikash!"
		
@app.route("/multiply")

def multiply():
		a=2
		b=4
		return str(a**b)
	
	
	
@app.route("/index")
def index():
	a=request.args.get('a',0,type=int)
	b=request.args.get('b',0,type=int)
	return str(a+b)



if __name__=="__main__":
	app.run()
	