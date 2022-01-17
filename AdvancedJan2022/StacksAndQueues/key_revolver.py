from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets_stack = [int(b) for b in input().split()] # back to front
locks_queue = deque(int(l) for l in input().split()) # shoot from the back
intelligence = int(input())

is_failed = False
bullets_shot = 0
while locks_queue:
    bullet = bullets_stack.pop()
    bullets_shot += 1
    lock = locks_queue.popleft()
    if bullet <= lock:
        print('Bang!')
    else:
        locks_queue.appendleft(lock)
        print('Ping!')

    if bullets_shot % barrel_size == 0 and bullets_stack:
        print('Reloading!')

    if not bullets_stack and locks_queue:
        is_failed = True
        break

if is_failed:
    print(f"Couldn't get through. Locks left: {len(locks_queue)}")
else:
    money_spent = bullets_shot * bullet_price
    money_earned = intelligence - money_spent
    print(f"{len(bullets_stack)} bullets left. Earned ${money_earned}")


