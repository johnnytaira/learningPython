class RockPaperScissors:

    def rockPaperScissors(self):
        while True:
            resp = input("Quer jogar? ")
            if resp != "yes":
                break
            else:
                player1 = input("Jogador 1, escolha: ")
                player2 = input("Jogador 2, escolha: ")
                if (player1 == "scissors" and player2 == "paper") or (player1 =="paper" and player2 =="rock") or (player1=="rock" and player2 == "scissors"):
                    print("Jogador 1 ganhou!")
                elif player1 == player2:
                    print("Empatou!")
                else:
                    print("Jogador 2 ganhou!")
