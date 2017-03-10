from flask import Blueprint,jsonify

membros = Blueprint("membros",__name__)

@membros.route("/membros")
def list_membros():
    data = {"Mensagem":"Bem vindo a area de Membros"}
    return jsonify(data)

@membros.route("/membros/<int:id>/",methods=["GET"])
def getMembros(id):
    data = {"Mensagem":"Listando Membro com o ID %s"%id}
    return jsonify(data)

@membros.route("/membros/",methods=["POST"])
def postMembros():
    data = {"Mensagem":"Cadastrando Membro"}
    return jsonify(data)

@membros.route("/membros/<int:id>/",methods=["PUT"])
def editarMembros(id):
    data = {"Mensagem":"Atualizando Membro com o ID %s"%id }
    return jsonify(data)

@membros.route("/membros/<int:id>/",methods=["DELETE"])
def deletarMembros(id):
    data = {"Mensagem" : "Deletando Membro com o ID %s"%id}
    return jsonify(data)
