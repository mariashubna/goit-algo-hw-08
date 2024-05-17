import heapq

cables_length = [4, 7, 2, 9, 5, 1, 12]


def joining(cables):
    heapq.heapify(cables)
    
    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        new_cable = first + second
        heapq.heappush(cables, new_cable)
        print(f"Шляхом з'єднання найменших наявних кабелів {first} та {second} отримаємо {new_cable}")

    return cables[0]

print(joining(cables_length))
