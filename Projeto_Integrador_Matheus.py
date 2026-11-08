
import json
import os

ARQUIVO = "alunos.json"

# Carregar alunos cadastrados
def carregar_alunos():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return [
        {
            "nome": "João Silva",
            "matricula": "001",
            "curso": "ADS",
            "email": "joao@gmail.com"
        },
        {
            "nome": "Maria Souza",
            "matricula": "002",
            "curso": "Engenharia de Software",
            "email": "maria@gmail.com"
        }
    ]


def salvar_alunos():
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(alunos, arquivo, ensure_ascii=False, indent=4)


alunos = carregar_alunos()
salvar_alunos()


# Menu principal
while True:
    print("\n===== SISTEMA DE CADASTRO DE ALUNOS =====")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Editar aluno")
    print("4 - Excluir aluno")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ").strip()
        matricula = input("Matrícula: ").strip()
        curso = input("Curso: ").strip()
        email = input("E-mail: ").strip()

        if not nome or not matricula or not curso or not email:
            print("Preencha todos os campos!")
        elif any(a["matricula"] == matricula for a in alunos):
            print("Matrícula já cadastrada!")
        elif "@" not in email:
            print("E-mail inválido!")
        else:
            alunos.append({
                "nome": nome,
                "matricula": matricula,
                "curso": curso,
                "email": email
            })
            salvar_alunos()
            print("Aluno cadastrado com sucesso!")

    elif opcao == "2":
        print("\n===== ALUNOS CADASTRADOS =====")
        if not alunos:
            print("Nenhum aluno cadastrado.")
        else:
            for aluno in alunos:
                print("----------------------")
                print("Nome:", aluno["nome"])
                print("Matrícula:", aluno["matricula"])
                print("Curso:", aluno["curso"])
                print("E-mail:", aluno["email"])

    elif opcao == "3":
        matricula = input("Matrícula do aluno: ")
        encontrado = False

        for aluno in alunos:
            if aluno["matricula"] == matricula:
                nome = input("Novo nome (Enter para manter): ")
                curso = input("Novo curso (Enter para manter): ")
                email = input("Novo e-mail (Enter para manter): ")

                if nome:
                    aluno["nome"] = nome
                if curso:
                    aluno["curso"] = curso
                if email:
                    if "@" not in email:
                        print("E-mail inválido!")
                        break
                    aluno["email"] = email

                salvar_alunos()
                print("Cadastro atualizado!")
                encontrado = True
                break

        if not encontrado:
            print("Aluno não encontrado.")

    elif opcao == "4":
        matricula = input("Matrícula para excluir: ")
        encontrado = False

        for aluno in alunos:
            if aluno["matricula"] == matricula:
                confirmacao = input("Confirma exclusão? (s/n): ")
                if confirmacao.lower() == "s":
                    alunos.remove(aluno)
                    salvar_alunos()
                    print("Aluno excluído!")
                else:
                    print("Exclusão cancelada.")
                encontrado = True
                break

        if not encontrado:
            print("Aluno não encontrado.")

    elif opcao == "5":
        print("Sistema encerrado!")
        break

    else:
        print("Opção inválida!")
