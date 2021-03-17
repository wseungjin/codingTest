
def bin(stones, k, high, low):
    if (low > high):
        return high

    mid = (high + low)//2

    length = 0
    for stone in stones:
        if length >= k:
            return bin(stones, k, mid-1, low)
        if mid > stone:
            length += 1
        else:
            length = 0
    return bin(stones, k, high, mid+1)


def solution(stones, k):

    low = 1
    high = 200000000
    stones.append(200000001)
    return bin(stones, k, high, low)


def main():
    print(solution([2, 1, 1, 1, 1], 4))


main()
