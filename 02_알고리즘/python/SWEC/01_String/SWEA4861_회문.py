# 팰린드롬 여부에 따라 True, False 반환
def isPalindrome(lst):
    # print(lst)
    for i in range(len(lst)//2):
        if lst[i] != lst[-(1+i)]:
            return False
    return True


# M의 크기에 맞는 배열을 팰린드롬 여부체크로 보내는 함수
def palindrome(lst):
    for i in range(N-M+1):
        # 팰린드롬 여부를 체크해서  True일 경우, 해당 배열을 문자열로 바꾸어 반환하고 아니면 False(0)반환
        if isPalindrome(lst[i:M+i]):
            return ''.join(lst[i:M+i])
    return False


for t in range(1, 1+int(input())):
    N, M = map(int, input().split())
    arr = [list(input())for _ in range(N)]
    ans = 0
    for i in range(N):
        # 행 체크
        if palindrome(arr[i]):
            ans = palindrome(arr[i])
        # 열체크
        temp = []
        for j in range(N):
            temp.append(arr[j][i])
        if palindrome(temp):
            ans = palindrome(temp)

    print("#{} {}".format(t, ans))
