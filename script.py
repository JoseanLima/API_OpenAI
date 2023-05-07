import openai

# Leitura da variável de ambiente
from get_env import print_env

# Recebendo o resultado da função
env = print_env(['API_KEY'])

# ---
# Configuração do ambiente
# ---

# Atribuindo o valor para variável openai.api_key
openai.api_key = env['API_KEY']

# ---
# Definindo modelo de linguagem da OpenAI do GPT-3
# ---

model_engine = 'text-davinci-003'

# ---
# Desenvolvendo o Programa
# ---

while True:
    prompt = input('Manda a pergunta: ')

    # Configuranção a geração da resposta
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,  # Quantas palavras podem vir na resposta
        temperature=0.5,  # Quanto pode infererir e firmar em conhecimentos sólidos
    )

    response = completion.choices[0].text
    print(response)
