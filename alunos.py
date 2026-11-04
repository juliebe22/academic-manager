from database import alunos_collection
from bson.objectid import ObjectId


# CREATE - Cadastrar aluno
def cadastrar_aluno(dados):

    resultado = alunos_collection.insert_one(dados)

    return resultado.inserted_id


# READ - Consultar alunos
def listar_alunos(filtro=None):

    if filtro is None:
        filtro = {}

    alunos = alunos_collection.find(filtro).sort("nome", 1)

    return list(alunos)


# UPDATE - Atualizar aluno
def atualizar_aluno(id_aluno, dados):

    resultado = alunos_collection.update_one(
        {"_id": ObjectId(id_aluno)},
        {"$set": dados}
    )

    return resultado.modified_count


# DELETE - Excluir aluno
def excluir_aluno(id_aluno):

    resultado = alunos_collection.delete_one(
        {"_id": ObjectId(id_aluno)}
    )

    return resultado.deleted_count