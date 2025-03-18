input_text=input()

stack=[]
ans=''
check=False

for word in input_text:
    if word=='<':
        check=True
        for _ in range(len(stack)):
            ans+=stack.pop()
    
    stack.append(word)

    if word=='>':
        check=False
        for _ in range(len(stack)):
            ans+=stack.pop(0)
    
    if word==' ' and check==False:
        
        for i in range(len(stack)):
            if i==0:
                
                stack.pop()
                continue
            ans+=stack.pop()
        ans+=' '

if stack:
    
    for _ in range(len(stack)):
        ans+=stack.pop()


print(ans)
