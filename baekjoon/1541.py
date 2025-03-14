import re


text=input()

result=0

# -가 등장하면 그 이후의 숫자들은 한 번에 처리해서 빼는 게 최솟값

split_text=text.split('-')

result+=sum(map(int,split_text[0].split('+')))

for group_text in split_text[1:]:
    result-=sum(map(int,group_text.split('+')))


print(result)

