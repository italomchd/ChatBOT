import openai

# Acesso API OpenAI GPT
client = openai.OpenAI(
    api_key = ("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"),
)

# Lista de Mensagens contém o historico para guiar a IA. Iniciamos apresentando o problema para que a IA posso responder as perguntas baseadas pela URL
lista_mensagens = [
    {"role": "system", "content": 'Você é um chatbot. Acesse : https://www.pg.unicamp.br/norma/31594/0. E responda as dúvidas sobre o Vestibular Unicamp 2024.'},
    ]

# Boas vindas e explica como funciona o ChatBOT, além de aprensentar a URL para mais informações
print("\nBem-vindo ao ChatBOT VU2024\nAqui você pode tirar suas dúvidas sobre o Vestibular Unicamp\nPara mais informações acesse: https://www.pg.unicamp.br/norma/31594/0\nPara sair digite 'SAIR'\n")

# Funçao responsavél por fazer todo o processamento, baseado na mensagem enviada e na lista de mensagens salvas. O ChatGPT avaliar qual a resposta da pergunta feita.
def enviar_mensagem(mensagem, lista_mensagens=[]):
    lista_mensagens.append(
        {"role": "user", "content": mensagem}
        ) # Adiciona a mensagem enviada na lista.
    resposta = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = lista_mensagens,
    ) # Resposta ChatGPT
    lista_mensagens.append({"role": "assistant", "content": resposta.choices[0].message.content}) # Resposta é adicionada a lista.

    return resposta.choices[0].message.content # Retorna resposta ChatGPT

# Loop para o ChatBOT  
while True:
    texto = input("Escreva aqui sua dúvida: ") # Entrada na mensagem
    if texto == "SAIR": # Termino Loop
        break
    else:
        resposta = enviar_mensagem(texto, lista_mensagens) # Resposta ChatBOT
        print("\nChatbot:", resposta, "\n")

