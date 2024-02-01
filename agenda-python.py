
def adicionar_contato(contatos, nome, telefone, email):
  if any(
    contato["nome"] == nome 
    or contato["telefone"] == telefone
    or contato["email"] == email
    for contato in contatos):
    print("Você já tem esse contato salvo em sua agenda!")
    return False

  if "@" not in email:
    print("Email invalido!")
    return False
      
  contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
  contatos.append(contato)
  print(f"Contato do {nome} adicionado com sucesso!")
  return True

def alterar_contato(contatos, indice_contato, novo_nome, novo_telefone, novo_email):
  
  try: 
    indice_ajustado = int(indice_contato) -1
  except Exception as err:
    print(f"O opção incorreta! Erro {err}")
  
  if 0 <=indice_ajustado < len(contatos):
    contato_atual = contatos[indice_ajustado]

    if (contato_atual["nome"] == novo_nome and
      contato_atual["telefone"] == novo_telefone and
      contato_atual["email"] == novo_email):
      print("Esses contato já existe!")
      return False     
    contato_atual["nome"] = novo_nome
    contato_atual["telefone"] = novo_telefone
    contato_atual["email"] = novo_email
    print(f"Contato número {indice_contato} atualizada para: \n {novo_nome} - {novo_telefone} - {novo_email}")
    return True 
  else:
    print("Esse contato não existe!")
    return False 

def listar_contatos(contatos):
  if contatos :
    print("\nMinha lista de contatos:")
    for indice, contato in enumerate(contatos, start=1):
      favorito = "✓" if contato["favorito"] else " "
      nome_contato = contato["nome"]
      tel_contato = contato["telefone"]
      email_contato = contato["email"]
      print(f"{indice}. {nome_contato} - Cel:{tel_contato} - Email:{email_contato} - Favorito[{favorito}]")
    return True
  else:
    print("\nNão existem contatos na sua agenda!")
    return False
  
def listar_favoritos(contatos):
  if any(contato["favorito"] == True for contato in contatos) :
    print("\nMinha lista de contatos favoritos:")
    for indice, contato in enumerate(contatos, start=1):
      if contato["favorito"] == True:
        favorito = "✓" if contato["favorito"] else " "
        nome_contato = contato["nome"]
        tel_contato = contato["telefone"]
        email_contato = contato["email"]
        print(f"{indice}. {nome_contato} - Cel:{tel_contato} - Email:{email_contato} - Favorito[{favorito}]")
    return True
  else:
    print("\nSua agenda não tem contatos marcados com favoritos!")
    return False
  
def listar_nao_favoritos(contatos):
  if any(contato["favorito"] == False for contato in contatos) :
    print("\nMeus contatos que ainda não são favoritos:")
    for indice, contato in enumerate(contatos, start=1):
      if contato["favorito"] == False:
        favorito = "✓" if contato["favorito"] else " "
        nome_contato = contato["nome"]
        tel_contato = contato["telefone"]
        email_contato = contato["email"]
        print(f"{indice}. {nome_contato} - Cel:{tel_contato} - Email:{email_contato} - Favorito[{favorito}]")
    return True
  else:
    print("\nTodos os seus contatos são favoritos nesse momento!")
  return False

def adicionar_favoritos(contatos, indice_contato):
  indice_ajustado = int(indice_contato) - 1
  if indice_ajustado >= 0 and indice_ajustado < len(contatos):
    if contatos[indice_ajustado]["favorito"] == True:
      print("Este contato já é favorito!")
      return False
    else:
      contatos[indice_ajustado]["favorito"] = True 
      print("Contato adicionado aos favoritos!") 
      return True
  else:
    print("Este contato não exite!")
    return False
  
def desmarcar_favoritos(contatos, indice_contato):
  indice_ajustado = int(indice_contato) - 1
  if indice_ajustado >= 0 and indice_ajustado < len(contatos):
      if contatos[indice_ajustado]["favorito"] == False:
        print("Este contato não é favorito!")
      else:
        contatos[indice_ajustado]["favorito"] = False
        print(f"Este contato foi removido dos favoritos!")
      return True
  else:
    print("Este contato não exite!")
    return False

def remover_contato(contatos, indice_contato):
  indice_ajustado = int(indice_contato) - 1
  if indice_ajustado >= 0 and indice_ajustado < len(contatos):
    contato = contatos[indice_ajustado]
    if contato["favorito"]== True:
      contato_remover = input("Este contato é um favorito, deseja realmente removê-lo ? Digite S para SIM ou N para NÃO ")
      if contato_remover.upper() == "S" or contato_remover.upper()== "SIM":
        contatos.pop(indice_ajustado)
        print("O Contato foi removido da sua agenda!")
      else:
        print("Voce será redirecionado para o Menu da Agenda!")
        return
    else:
        contatos.pop(indice_ajustado)
        print("O Contato foi removido da sua agenda!")
        return
  else:
    print("Este contato não existe!")  
    return False
  
def validar_indice_contato(contatos, indice_contato):
  indice_ajustato = int(indice_contato) - 1
  if 0 <= indice_ajustato < len(contatos) :
    print("* * *")
    return True
  else: 
    print("Este contato não existe")
    return False

def finalizar_agenda():
  print("Agenda Finalizada!!")
  return
  
contatos = []
while True: 
  print("Minha Agenda de Contatos")
  print("\nEscolha as opções abaixo:")
  print("1. Adicionar um novo contato")
  print("2. Listar todos os contatos")
  print("3. Alterar um contato existente")
  print("4. Marcar um contato como Favorito")
  print("5. Listar contatos favoritos")
  print("6. Retirar dos favoritos")
  print("7. Remover um contato")
  print("8. Sair da agenda")

  opcao = input("\nDigite a opção desejada: ")

  if opcao == "1":
    print("\nPreecha dos dados do contato:")
    nome = input("Preencha o nome ")
    telefone = input("Preencha o telefone ")
    email = input("Preencha o email ")
    adicionar_contato(contatos, nome, telefone,email)
  elif opcao == "2":
    listar_contatos(contatos)  
  elif opcao == "3":
    listar_contatos(contatos)
    indice_contato= input("Digite o número do contato qual deseja alterar: ")
    valida_indice = validar_indice_contato(contatos, indice_contato)
    if valida_indice :
      novo_nome = input("Digite o nome: ")
      novo_telefone = input("Digite o telefone")
      novo_email = input("Digite o email: ")
      alterar_contato(contatos, indice_contato, novo_nome, novo_telefone, novo_email)
    else:
      print("Digite novamente")
  elif opcao == "4":
    listar_nao_favoritos(contatos)
    indice_contato = input("Digite o número do contato que deseja adicionar aos favoritos: ")
    adicionar_favoritos(contatos, indice_contato)
  elif opcao == "5":
    listar_favoritos(contatos)
  elif opcao == "6":
    listar_favoritos(contatos)
    indice_contato = input("Digite o número do contato que deseja remover dos favoritos: ")
    desmarcar_favoritos(contatos, indice_contato)
  elif opcao == "7":
    listar_contatos(contatos)
    indice_contato = input("Deseje o número do contato que deseja remover: ")
    remover_contato(contatos, indice_contato)  
  elif opcao == "8":
    finalizar_agenda()
    break

