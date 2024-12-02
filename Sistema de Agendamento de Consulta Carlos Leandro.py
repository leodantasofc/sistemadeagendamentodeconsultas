# Sistema Simples de Agendamento de Consultas

consultas = []

def menu():
    print("\n=== Sistema de Agendamento de Consultas ===")
    print("1. Criar nova consulta")
    print("2. Listar consultas")
    print("3. Editar consulta")
    print("4. Excluir consulta")
    print("5. Sair")
    return input("Escolha uma opção: ")

def criar_consulta():
    print("\n--- Criar Nova Consulta ---")
    paciente = input("Nome do Paciente: ")
    medico = input("Nome do Médico: ")
    data = input("Data (DD/MM/AAAA): ")
    horario = input("Horário (HH:MM): ")
    especialidade = input("Especialidade: ")
    consulta = {
        "paciente": paciente,
        "medico": medico,
        "data": data,
        "horario": horario,
        "especialidade": especialidade
    }
    consultas.append(consulta)
    print("Consulta criada com sucesso!")

def listar_consultas():
    print("\n--- Lista de Consultas ---")
    if not consultas:
        print("Nenhuma consulta agendada.")
    else:
        for idx, consulta in enumerate(consultas):
            print(f"\nID: {idx}")
            print(f"Paciente: {consulta['paciente']}")
            print(f"Médico: {consulta['medico']}")
            print(f"Data: {consulta['data']}")
            print(f"Horário: {consulta['horario']}")
            print(f"Especialidade: {consulta['especialidade']}")

def editar_consulta():
    listar_consultas()
    print("\n--- Editar Consulta ---")
    consulta_id = int(input("Digite o ID da consulta que deseja editar: "))
    if 0 <= consulta_id < len(consultas):
        print("Deixe em branco para manter o valor atual.")
        paciente = input(f"Novo Nome do Paciente ({consultas[consulta_id]['paciente']}): ")
        medico = input(f"Novo Nome do Médico ({consultas[consulta_id]['medico']}): ")
        data = input(f"Nova Data ({consultas[consulta_id]['data']}): ")
        horario = input(f"Novo Horário ({consultas[consulta_id]['horario']}): ")
        especialidade = input(f"Nova Especialidade ({consultas[consulta_id]['especialidade']}): ")

        if paciente: consultas[consulta_id]['paciente'] = paciente
        if medico: consultas[consulta_id]['medico'] = medico
        if data: consultas[consulta_id]['data'] = data
        if horario: consultas[consulta_id]['horario'] = horario
        if especialidade: consultas[consulta_id]['especialidade'] = especialidade

        print("Consulta atualizada com sucesso!")
    else:
        print("ID inválido.")

def excluir_consulta():
    listar_consultas()
    print("\n--- Excluir Consulta ---")
    consulta_id = int(input("Digite o ID da consulta que deseja excluir: "))
    if 0 <= consulta_id < len(consultas):
        consultas.pop(consulta_id)
        print("Consulta excluída com sucesso!")
    else:
        print("ID inválido.")

def main():
    while True:
        opcao = menu()
        if opcao == "1":
            criar_consulta()
        elif opcao == "2":
            listar_consultas()
        elif opcao == "3":
            editar_consulta()
        elif opcao == "4":
            excluir_consulta()
        elif opcao == "5":
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if _name_ == "_main_":
    main()