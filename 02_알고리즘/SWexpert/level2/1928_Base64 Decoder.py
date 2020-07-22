import base64

for t in range(1, 1+int(input())):
    print("#{} {}".format(t, base64.b64decode(input()).decode("UTF-8")))

'''
사실 encode, decode 라이브러리가 생각이 나서 
이 부분은 base 64 형태로 인코딩, 디코딩 하는 것을 찾아보고 풀었다.
그래서 금방 풀기는 했는데, 실제로 구현할 수 있지 않을까 싶어 C언어를 참조하면서
python으로 구현해보았다.(Base64_Decoder_2.py 파일에 다시 풀어봄.)
'''
