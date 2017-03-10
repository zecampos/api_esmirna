from flask import Blueprint,jsonify,request
from Model import Membros
import json



membros = Blueprint("membros",__name__)

@membros.route("/membros/")
def list_membros():
    listar_membros = json.loads(Membros.objects.to_json())
    return jsonify({"Membros":listar_membros})

@membros.route("/membros/<int:id>/",methods=["GET"])
def getMembros(id):
    data = {"Mensagem":"Listando Membro com o ID %s"%id}
    return jsonify(data)

@membros.route("/membros/",methods=["POST"])
def postMembros():
    try:
        dados = request.get_json()
        m = Membros()
        for key in dados.keys():
            setattr(m,key,dados[key])
        m.save()
        return jsonify({"Mensagem":"Membro cadastrado com sucesso"})
    except Exception as e:
        return jsonify({"Mensagem":"Falhou ao cadastrar membro: %s"%e})

@membros.route("/membros/<int:id>/",methods=["PUT"])
def editarMembros(id):
    data = {"Mensagem":"Atualizando Membro com o ID %s"%id }
    return jsonify(data)

@membros.route("/membros/<int:id>/",methods=["DELETE"])
def deletarMembros(id):
    data = {"Mensagem" : "Deletando Membro com o ID %s"%id}
    return jsonify(data)
