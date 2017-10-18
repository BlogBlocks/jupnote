def randnoun():
    import random, heapq
    def main():
        with open('hashtag-nouns.txt') as fin:
            word, = heapq.nlargest(1, fin, key=lambda L: random.random())
            word = word.decode('utf-8')
    return word 