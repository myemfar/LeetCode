class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant, dire = [], []
        for i, party in enumerate(senate):
            if party == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        while radiant and dire:
            r = radiant.pop(0)
            d = dire.pop(0)
            if r < d:
                radiant.append(r + len(senate))
            else:
                dire.append(d + len(senate))
        return "Radiant" if radiant else "Dire"