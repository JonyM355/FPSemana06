import json

class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.vida_maxima = vida

    def atacar(self, inimigo):
        inimigo.vida -= self.ataque
        print(f"{self.nome} Ataca {inimigo.nome} e Causa {self.ataque} de Dano!")

    def __str__(self):
        return f"{self.nome} {self.vida}"

class Guerreiro(Personagem):
    def especial(self, inimigo):
        inimigo.vida -= 30
        print(f"{self.nome} Usa Golpe Poderoso em {inimigo.nome} e Causa 30 de Dano!")
    pass

class Mago(Personagem):
    def especial(self):
        self.vida = min(self.vida + 25, self.vida_maxima)
        print(f"{self.nome} usa Cura e Ganha 25 Pontos de Vida!")

class Arqueiro(Personagem):
    def especial(self, inimigos):
        for i in inimigos:
            if i == self:
                i.vida = i.vida
            else:
                i.vida -= 15
        print(f"{self.nome} usa Chuva de Flechas e Causa 15 a Todos os Inimigos!")
    pass

def importar_personagens(caminho):
    try:   
        with open(caminho, "r", encoding='utf-8') as file:
            dados = json.load(file)

            personagens = []
            for dado in dados:
                classe = dado.get("classe")
                if classe == 'Guerreiro':
                    personagem = Guerreiro(dado["nome"], dado["vida"], dado["ataque"])
                elif classe == 'Mago':
                    personagem = Mago(dado["nome"], dado["vida"], dado["ataque"])
                elif classe == 'Arqueiro':
                    personagem = Arqueiro(dado["nome"], dado["vida"], dado["ataque"])
                else:
                    raise ValueError(f"Classe Desconhecida: {classe}")
            
                personagens.append(personagem)
            
            return personagens, len(personagens)
    
    except FileNotFoundError:
        print("Não encontrou")
        return [], 0
    
    """
        Função que importa personagens a partir de um ficheiro JSON.
        O ficheiro contém uma lista de personagens com informações de nome, vida, ataque e classe.
        - caminho: Caminho para o ficheiro JSON que contém os dados dos personagens.
        Retorna:
        - lista de personagens.
        - quantidade total de personagens importados.
    """
    pass

def ordenar_personagens_por_vida(personagens):
    return sorted(personagens, key=lambda personagem: personagem.vida)

    """
        Função que ordena a lista de personagens de acordo com os pontos de vida (do menor para o maior).
        - personagens: Lista de personagens.
        Retorna:
        - lista de personagens ordenada por vida.
    """
    pass

personagens, num_personagens = importar_personagens('personagens.json')
print(f"{num_personagens} Personagens Entram em Batalha!")

personagens = ordenar_personagens_por_vida(personagens)

print(personagens[0])
print(personagens[1])
print(personagens[2])

personagens[0].atacar(personagens[1])
print(personagens[1])

personagens[1].atacar(personagens[2])
print(personagens[2])

personagens[2].atacar(personagens[0])
print(personagens[0])

personagens[0].especial()
print(personagens[0])

personagens[1].especial([personagens[0], personagens[1]])
print(personagens[0])
print(personagens[1])

personagens[2].especial(personagens[1])
print(personagens[1])