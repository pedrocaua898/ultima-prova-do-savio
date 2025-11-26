def obter_questoes(tema, dificuldade):

    base = {
        "Matemática": {
            "Fácil": [
                {"pergunta": "Quanto é 2 + 2?", "opcoes": ["3", "4", "5"], "correta": "4"},
                {"pergunta": "Quanto é 10 - 4?", "opcoes": ["6", "5", "7"], "correta": "6"},
                {"pergunta": "Quanto é 3 × 3?", "opcoes": ["6", "9", "12"], "correta": "9"},
            ],
            "Médio": [
                {"pergunta": "Quanto é 7 × 8?", "opcoes": ["48", "54", "56"], "correta": "56"},
                {"pergunta": "Qual é a raiz quadrada de 81?", "opcoes": ["9", "8", "7"], "correta": "9"},
                {"pergunta": "Quanto é 15 × 4?", "opcoes": ["60", "45", "55"], "correta": "60"},
            ],
            "Difícil": [
                {"pergunta": "Quanto é 12²?", "opcoes": ["124", "144", "128"], "correta": "144"},
                {"pergunta": "Quanto é 25% de 240?", "opcoes": ["40", "50", "60"], "correta": "60"},
                {"pergunta": "Resolva: (5 × 8) + (9 ÷ 3)", "opcoes": ["43", "49", "44"], "correta": "43"},
            ],
        },

        "Português": {
            "Fácil": [
                {"pergunta": "Qual é o plural de 'cão'?", "opcoes": ["cães", "cãos", "cãeses"], "correta": "cães"},
                {"pergunta": "Qual é o plural de 'pão'?", "opcoes": ["pães", "pãos", "pãoses"], "correta": "pães"},
                {"pergunta": "Qual é o aumentativo de 'casa'?", "opcoes": ["casão", "casa grande", "casarro"], "correta": "casarão"},
            ],
            "Médio": [
                {"pergunta": "Qual é o tempo verbal de 'eu comeria'?", "opcoes": ["Futuro", "Condicional", "Pretérito"], "correta": "Condicional"},
                {"pergunta": "Qual é o sujeito em 'As meninas correram'?", "opcoes": ["As meninas", "Correram", "Meninas"], "correta": "As meninas"},
                {"pergunta": "Qual é a classe de palavra de 'rapidamente'?", "opcoes": ["Adjetivo", "Advérbio", "Substantivo"], "correta": "Advérbio"},
            ],
            "Difícil": [
                {"pergunta": "O que é uma metáfora?", "opcoes": ["Comparação implícita", "Exagero", "Som parecido"], "correta": "Comparação implícita"},
                {"pergunta": "O que é uma oração subordinada?", "opcoes": ["Depende de outra", "É independente", "É uma frase curta"], "correta": "Depende de outra"},
                {"pergunta": "Em 'João, o médico, chegou', o termo entre vírgulas é:", "opcoes": ["Aposto", "Vocativo", "Adjunto"], "correta": "Aposto"},
            ],
        },

        "Geografia": {
            "Fácil": [
                {"pergunta": "Qual é o maior país do mundo?", "opcoes": ["China", "Rússia", "Canadá"], "correta": "Rússia"},
                {"pergunta": "Qual o país do Cristo Redentor?", "opcoes": ["Brasil", "Argentina", "Chile"], "correta": "Brasil"},
                {"pergunta": "Qual é o país mais populoso?", "opcoes": ["Índia", "China", "EUA"], "correta": "Índia"},
            ],
            "Médio": [
                {"pergunta": "Qual é o rio mais longo do Brasil?", "opcoes": ["Araguaia", "Amazonas", "Tietê"], "correta": "Amazonas"},
                {"pergunta": "Qual continente tem mais países?", "opcoes": ["África", "Ásia", "Europa"], "correta": "África"},
                {"pergunta": "Onde fica a Cordilheira dos Andes?", "opcoes": ["América do Sul", "América do Norte", "Europa"], "correta": "América do Sul"},
            ],
            "Difícil": [
                {"pergunta": "Qual o deserto mais seco do mundo?", "opcoes": ["Saara", "Atacama", "Gobi"], "correta": "Atacama"},
                {"pergunta": "A linha do Equador passa por quantos continentes?", "opcoes": ["3", "2", "4"], "correta": "3"},
                {"pergunta": "O ponto mais alto do mundo é:", "opcoes": ["Everest", "K2", "Kangchenjunga"], "correta": "Everest"},
            ],
        }
    }

    return base[tema][dificuldade]
