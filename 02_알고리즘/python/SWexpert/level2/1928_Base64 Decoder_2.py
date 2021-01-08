def Base64(s):
    for i in range(len(s)//4):
        # 4개의 문자씩 끊기.
        b64 = s[i*4:(i+1)*4]
        b256 = 0

        # 4개의 문자열을 6bit씩 shift연산
        for j in range(4):
            n = trans(b64[j])
            b256 = (b256 << 6) + n
            # print(n, b256)

        # 0 X ff : byte변수의 값을 출력
        print(chr((b256 >> 16) & 0xff), end="")
        print(chr((b256 >> 8) & 0xff), end="")
        print(chr(b256 & 0xff), end="")


def trans(s):
    if ('A' <= s and s <= 'Z'):
        n = ord(s) - ord('A')
    elif ('a' <= s and s <= 'z'):
        n = ord(s) - ord('a') + 26
    elif ('0' <= s and s <= '9'):
        n = ord(s) - ord('0') + 52
    elif (s == '+'):
        n = 62
    elif (s == '/'):
        n = 63
    return n


for t in range(1, 1+int(input())):
    sentence = input()
    print("#{}".format(t), end=" ")
    Base64(sentence)

'''
1.
trans 함수에서 계산을 저렇게 계산을 한건 표1과 같이 Encoding을 하기 위한 계산.
T로 예를들면 ord('T'): 84이고, 표1의 T 값은 19인 것을 확인이 가능하다. 이때 ord('A'): 65로 
ord('T') - ord('A')를 하면, 표와 같은 계산이 가능했다.
'''
