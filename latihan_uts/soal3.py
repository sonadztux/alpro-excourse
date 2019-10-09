kuis = 70
uts = 60
uas = 65
na = ((kuis*0.20)+(uts*0.30)+(uas*0.30))

if na > 80:
    print('A')
elif 75 <= 80 and na > 75:
    print('B')
elif na <= 75 and na > 70:
    print('C')
elif na <= 70 and na > 60:
    print('D')
else:
    print('E')

# Guess the output and explain the algorithm !
