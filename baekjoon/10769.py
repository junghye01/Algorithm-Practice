S=input()
happy=0
sad=0

for i in range(len(S)):
    collector=[]
    if S[i]==':':
        for j in range(3):
            if i+j<=len(S)-1:
                collector.append(S[i+j])
        result1="".join(collector)
        if result1==':-)':
            happy=happy+1
        elif result1==':-(':
            sad=sad+1
        else:
            continue

if happy==0 and sad==0:
    print('none')
elif happy>sad:
    print('happy')
elif happy<sad:
    print('sad')
elif happy==sad:
    print('unsure')