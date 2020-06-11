import hashlib

S = input()
print(hashlib.sha256(S.encode()).hexdigest())

'''
* 정리 * 
1. 주어진 문자열에 대한 단방향 암호화 해시 (SHA-256)
2. S.encode()
    - 문자열을 2진 숫자(바이트)로 바꾸어 저장
3. hashlib.sha256()
    - sha256형식으로 지정된 해시 객체 생성
4. hexdigest()
    - 이용하여 객체로부터 SHA256 해시에 대한 16진수 값 구함.
'''
