x = int(input())
array = list(map(int, input().split()))

# dp 테이블 100까지 설정이 맞는지?
# 맞다. 인덱스 값이 아니라 그냥 메모리 100개를 만드는 거기에
dp = [0] * 100
dp[0] = array[0]
dp[1] = max(array[0], array[1])

# for문 x까지 범위가 맞는지? x+1인가? x로 하고 마지막에 x-1를 출력하면 된다.
# return  안해도 되는가? 네 함수가 아니기에
for i in range(2, x):
    dp[i] = max(dp[i - 1], dp[i - 2] + array[i])

print(dp[x - 1])
