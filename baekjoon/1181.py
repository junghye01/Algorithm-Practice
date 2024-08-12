import sys
n=int(sys.stdin.readline())
data=[sys.stdin.readline().strip() for i in range(n)]

data=set(data)
data=list(data)

tmp=[[len(x),x] for x in data]

tmp.sort(key=lambda x:(x[0],x[1]))
print("### 정렬 결과 ###")
for len_word, word in tmp:
    print(word)

#result=sorted(tmp)
#print("### 정렬 결과 ###")
#for len_word, word in result:
 #   print(word)
