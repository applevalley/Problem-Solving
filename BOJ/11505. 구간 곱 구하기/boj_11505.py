import sys


def init(left, right, node):
    if left == right:
        tree[node] = number_list[left]
        return
    else:
        mid = (left + right) // 2
        init(left, mid, node * 2)
        init(mid + 1, right, (node * 2) + 1)
        tree[node] = (tree[node * 2] * tree[(node * 2) + 1]) % 1000000007


def move(left, right, node, idx, value):
    if left == right == idx:
        tree[node] = value
        return tree[node]

    if left > idx or right < idx:
        return 0
    else:
        mid = (left + right) // 2
        move(left, mid, node * 2, idx, value)
        move(mid + 1, right, (node * 2) + 1, idx, value)
        tree[node] = (tree[node * 2] * tree[(node * 2) + 1]) % 1000000007


def tree_multiply(left, right, node, left_idx, right_idx):
    global count

    if right_idx < left or left_idx > right:
        return
    elif left_idx <= left and right_idx >= right:
        count *= tree[node]
        return
    elif left_idx <= right or left <= right_idx:
        mid = (left + right) // 2
        tree_multiply(left, mid, node * 2, left_idx, right_idx)
        tree_multiply(mid + 1, right, (node * 2) + 1, left_idx, right_idx)
        return


input = sys.stdin.readline
N, M, K = map(int, input().split())
number_list = [0] + [int(input()) for _ in range(N)]
tree = [0 for _ in range(4 * N)]

init(1, N, 1)

for i in range(M + K):
    target, b, c = map(int, input().split())
    if target == 1:
        move(1, N, 1, b, c)
    else:
        count = 1
        tree_multiply(1, N, 1, b, c)
        print(count % 1000000007)