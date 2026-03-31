import random
import time

def exibir_status(p1_nome, p1_hp, p2_nome, p2_hp):
    print("\n" + "="*30)
    print(f"{p1_nome.upper()}: {p1_hp} HP")
    print(f"{p2_nome.upper()}: {p2_hp} HP")
    print("="*30)

def batalha():
    # Status Iniciais
    pokemon = "Bulbasaur"
    hp_jogador = 100
    inimigo = "Squirtle"
    hp_inimigo = 100

    print(f"--- INÍCIO DA BATALHA: {pokemon} vs {inimigo} ---")

    while hp_jogador > 0 and hp_inimigo > 0:
        exibir_status(pokemon, hp_jogador, inimigo, hp_inimigo)
        
        print("O que você vai fazer?")
        print("1. Folha Navalha (Ataque)")
        print("2. Síntese (Cura)")
        print("3. Fugir")
        
        escolha = input("> ")

        # --- TURNO DO JOGADOR ---
        if escolha == "1":
            dano = random.randint(15, 25)
            # Chance de Crítico (20% de chance)
            if random.random() < 0.20:
                dano *= 2
                print("⭐ CRÍTICO! O golpe foi super efetivo!")
            
            hp_inimigo -= dano
            print(f"O {pokemon} usou Folha Navalha! {inimigo} perdeu {dano} HP.")
            
        elif escolha == "2":
            cura = random.randint(20, 30)
            hp_jogador += cura
            if hp_jogador > 100: hp_jogador = 100
            print(f"O {pokemon} usou Síntese e recuperou {cura} de vida!")
            
        elif escolha == "3":
            print("Você fugiu da luta como um mestre!")
            return # Sai da função e encerra o jogo
        
        else:
            print("Você hesitou e perdeu a vez!")

        # Verifica se o inimigo caiu
        if hp_inimigo <= 0:
            print(f"\n VITÓRIA! O {inimigo} desmaiou!")
            break

        # Pequena pausa para o jogador ler o que aconteceu
        time.sleep(1)

        # --- TURNO DO INIMIGO ---
        print(f"\nTurno do {inimigo}...")
        dano_inimigo = random.randint(12, 20)
        hp_jogador -= dano_inimigo
        print(f"O {inimigo} usou Bolhas! Você perdeu {dano_inimigo} HP.")

        # Verifica se o jogador caiu
        if hp_jogador <= 0:
            print("\n DERROTA! Seu Bulbasaur não aguenta mais lutar.")

# Iniciar o jogo
batalha()