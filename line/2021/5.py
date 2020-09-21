def cardScore(cards):
    totalScore : 
    for card in cards:
        if card > 9

def solution(cards):
    nowGame = 0
    dealerScore = 0
    playerScore = 0
    for currentCardCount in range len(cards):
        if nowGame == 0 or nowGame == 2:
            playerScore = playerScore + cardScore(card)
        elif  nowGame == 1 or nowGame == 3:
            dealerScore = dealerScore + cardScore(card) 
        else:
            if playerScore == 21:
                
        
        
    
def main():
    
    print(solution([12, 7, 11, 6, 2, 12]	))
    # print(solution([1, 4, 10, 6, 9, 1, 8, 13]	))

    # print(solution([10, 13, 10, 1, 2, 3, 4, 5, 6, 2]	))
    # print(solution([3, 3, 3, 3, 3, 3, 3, 3, 3, 3]	))

    
main()