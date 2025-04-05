import re

def gerar_resposta(mensagem):
    msg = mensagem.strip().lower()

    # Categorias com múltiplas possibilidades
    saudacoes = ['oi', 'olá', 'e aí', 'opa', 'fala', 'bom dia', 'boa tarde', 'boa noite']
    agradecimentos = ['obrigado', 'valeu', 'agradecido', 'gratidão']
    despedidas = ['tchau', 'até mais', 'falou', 'adeus']
    insegurancas = ['nervoso', 'ansioso', 'medo', 'vergonha', 'travar']
    duvidas_iniciais = ['o que falar', 'não sei o que dizer', 'como começo', 'começar conversa']

    # Detecção de intenção
    if any(p in msg for p in saudacoes):
        return 'Oi! Pronto pra encantar corações? Manda sua dúvida ou situação que eu tô aqui.'

    if any(p in msg for p in agradecimentos):
        return 'Tamo junto! Vai com tudo, porque carisma você já tem.'

    if any(p in msg for p in despedidas):
        return 'Se cuida! Lembre-se: quem confia no próprio brilho, ilumina qualquer lugar.'

    if any(p in msg for p in insegurancas):
        return 'É normal ficar assim! Respira, acredita no teu valor e manda uma abordagem leve e sincera.'

    if any(p in msg for p in duvidas_iniciais):
        return 'Tenta algo natural tipo: "Vi seu perfil e curti muito sua vibe, posso te conhecer melhor?"'

    # Análise semântica mais geral
    if 'conquistar' in msg or 'chamar atenção' in msg:
        return 'Mostre interesse verdadeiro. Elogie o que você realmente achou legal, e mantenha o papo leve!'

    if 'ela não responde' in msg or 'ele não responde' in msg:
        return 'Dá um tempo e respeita o silêncio. Às vezes o momento da pessoa não bate com o seu. Mas continua sendo você!'

    if 'gosto de alguém' in msg or 'tô apaixonado' in msg:
        return 'Aproveita esse sentimento! Demonstra aos poucos, com carinho e respeito, e vê se o interesse é recíproco.'

    if 'terminamos' in msg or 'fiquei solteiro' in msg:
        return 'É dolorido, mas também é recomeço. Foca em se cuidar, se redescobrir. O amor próprio vem primeiro.'

    if 'cantada' in msg or 'manda uma' in msg:
        return 'Aqui vai uma das boas: "Seu nome é Google? Porque tem tudo o que eu procuro."'

    if 'me ajuda' in msg or 'preciso de ajuda' in msg:
        return 'Claro! Me conta o que tá rolando e a gente resolve junto com estilo e carinho.'

    if re.search(r'(quem\s+é\s+você|qual\s+seu\s+nome)', msg):
        return 'Sou o Assistente do Murilo, seu aliado pra lidar com o coração e soltar o charme com classe.'

    return 'Não entendi direito... Mas se for amor, insegurança ou paquera, me explica melhor que eu te ajudo com gosto!'
