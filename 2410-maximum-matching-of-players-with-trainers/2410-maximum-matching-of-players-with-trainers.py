class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        
        players.sort()
        trainers.sort()
        matches = 0
        pp = len( players) - 1
        tp = len(trainers) - 1

        while pp >= 0 and  tp >= 0:

            if players[pp] <= trainers[tp]:
                pp -= 1
                tp -= 1
                matches += 1
            elif players[pp] > trainers[tp]:
                pp -= 1

        return matches 
        