values = {r: i for i, r in enumerate("23456789TJQKA", start=2)}

def hand_rank(hand):
    ranks = sorted([values[c[0]] for c in hand], reverse=True)
    suits = [c[1] for c in hand]

    from collections import Counter
    counts = Counter(ranks)
    count_values = sorted(counts.values(), reverse=True)
    unique_ranks = sorted(counts.keys(), reverse=True)

    is_flush = len(set(suits)) == 1
    is_straight = (len(unique_ranks) == 5 and
                   max(unique_ranks) - min(unique_ranks) == 4)

    if sorted(ranks) == [14, 5, 4, 3, 2]:
        is_straight = True
        ranks = [5, 4, 3, 2, 1]

    if is_straight and is_flush:
        return (8, ranks)
    if count_values == [4, 1]:
        four = [r for r in counts if counts[r] == 4][0]
        kicker = [r for r in counts if counts[r] == 1][0]
        return (7, [four, kicker])
    if count_values == [3, 2]:
        three = [r for r in counts if counts[r] == 3][0]
        pair = [r for r in counts if counts[r] == 2][0]
        return (6, [three, pair])
    if is_flush:
        return (5, ranks)
    if is_straight:
        return (4, ranks)
    if count_values == [3, 1, 1]:
        three = [r for r in counts if counts[r] == 3][0]
        kickers = sorted([r for r in counts if counts[r] == 1], reverse=True)
        return (3, [three] + kickers)
    if count_values == [2, 2, 1]:
        pairs = sorted([r for r in counts if counts[r] == 2], reverse=True)
        kicker = [r for r in counts if counts[r] == 1][0]
        return (2, pairs + [kicker])
    if count_values == [2, 1, 1, 1]:
        pair = [r for r in counts if counts[r] == 2][0]
        kickers = sorted([r for r in counts if counts[r] == 1], reverse=True)
        return (1, [pair] + kickers)
    return (0, ranks)

def compare(h1, h2):
    return hand_rank(h1) > hand_rank(h2)

count = 0
with open("0054_poker.txt") as f:
    for line in f:
        cards = line.strip().split()
        p1 = cards[:5]
        p2 = cards[5:]
        if compare(p1, p2):
            count += 1

print(count)
