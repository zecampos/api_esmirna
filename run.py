from flask import Flask,jsonify

app = Flask(__name__)
@app.route("/")
def hello():
    return "Helo Wolrd"

@app.route("/membros/<int:id>/",methods=["GET"])
def getMembros(id):
    data = {"Mensagem":"Listando Membro com o ID %s"%id}
    return jsonify(data)

@app.route("/membros",methods=["POST"])
def postMembros(id):
    data = {"Mensagem":"Cadastrando Membro"}
    return jsonify(data)

@app.route("/membros/<int:id>/",methods=["PUT"])
def editarMembros(id):
    data = {"Mensagem":"Atualizando Membro com o ID %s"%id }
    return jsonify(data)

@app.route("/membros/<int:id>/",methods=["DELETE"])
def deletarMembros(id):
    data = {"Mensagem" : "Deletando Membro com o ID %s"%id}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)