import math
from collections import deque

for part in (1, 2):
    queue = deque([(0, 500, 50, 58, 0, 0, 0, True)])
    best_value = math.inf
    visited = set()
    while queue:
        mana_spend, *rest = queue.popleft()
        if tuple(rest) in visited:
            continue
        visited.add(tuple(rest))
        mana, p_hp, b_hp, shield, poison, recharge, player_turn = rest
        if player_turn and part == 2:
            p_hp -= 1
        if mana_spend >= best_value or p_hp <= 0 or mana < 0:
            continue
        if poison > 0:
            b_hp -= 3
        if b_hp <= 0:
            best_value = min(best_value, mana_spend)
            continue
        if recharge > 0:
            mana += 101
        if not player_turn:
            p_hp -= 2 if shield > 0 else 9
            queue.append((mana_spend, mana, p_hp, b_hp, shield-1, poison-1, recharge-1, True))
            continue
        queue.append((mana_spend+53, mana-53, p_hp, b_hp-4, shield-1, poison-1, recharge-1, False))
        queue.append((mana_spend+73, mana-73, p_hp+2, b_hp-2, shield-1, poison-1, recharge-1, False))
        if shield <= 1:
            queue.append((mana_spend+113, mana-113, p_hp, b_hp, 6, poison-1, recharge-1, False))
        if poison <= 1:
            queue.append((mana_spend+173, mana-173, p_hp, b_hp, shield-1, 6, recharge-1, False))
        if recharge <= 1:
            queue.append((mana_spend+229, mana-229, p_hp, b_hp, shield-1, poison-1, 5, False))
    
    print(f"Part {part}: {best_value}")

