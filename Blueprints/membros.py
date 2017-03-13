from flask import Blueprint,jsonify,request
from Model import Membros
import json



membros = Blueprint("membros",__name__)

@membros.route("/membros/")
def list_membros():
    listar_membros = json.loads(Membros.objects.to_json())
    return jsonify({"Membros":listar_membros})

@membros.route("/membros/<id>/",methods=["GET"])
def getMembros(id):
    m = json.loads(Membros.objects(id=id).to_json())
    data = {"Membro":m}
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

@membros.route("/membros/<id>/",methods=["PUT"])
def editarMembros(id):
    try:
        dados = request.get_json()
        m = Membros.objects(id=id).first()
        for key in dados.keys():
            setattr(m,key,dados[key])
        m.save()
        data = {"Mensagem":"Atualizado Membro com o ID %s"%id }
        return jsonify(data)
    except Exception as e:
        return jsonify({"mensagem": "Falhou ao atualizar : %s"%e})

@membros.route("/membros/<id>/",methods=["DELETE"])
def deletarMembros(id):
    m = Membros.objects(id=id)
    m.delete()
    data = {"Mensagem" : "Deletando Membro com o ID %s"%id}
    return jsonify(data)
