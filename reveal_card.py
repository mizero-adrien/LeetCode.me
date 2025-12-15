from collections import deque
from typing import List

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()                      # sort the deck
        q = deque()                      # create an empty queue

        for card in reversed(deck):      # go from biggest to smallest
            if q:                        
                q.appendleft(q.pop())    # reverse of move top → bottom
            q.appendleft(card)           # put current card on top

        return list(q)