from controllers.Main import *
from flask import Flask , render_template, redirect, request, url_for
from sys import *


app = Flask(__name__)


@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/list')
def listRoutes():
    return render_template('list.html', routes=controller.graphService.listEdge)


@app.route('/search')
def searchRoute():
    return render_template('search.html')


@app.route('/new')
def newRoute():
    return render_template('new.html')


@app.route('/add', methods=['POST', ])
def add():
    origin = request.form['origin']
    destiny = request.form['destiny']
    custo = request.form['custo']
    controller.refreshGraph(origin, destiny, custo)
    controller.fileService.writeFile(origin, destiny, custo)
    return redirect(url_for('home'))


@app.route('/calcpathgraph', methods=['POST', ])
def calcpathgraph():
    origin = Vertex(request.form['origin'])
    destiny = Vertex(request.form['destiny'])
    route, cost = controller.getRoute(origin.getId(), destiny.getId())
    return render_template('search.html', routes=route, cost=cost)


if __name__ == '__main__':
    args = []
    for param in sys.argv:
        args.append(param)
    name_file = 'assets/input-routes.csv'
    controller = Main(name_file)
    controller.initGraph()
    controller.drawGraph()
    app.run()
