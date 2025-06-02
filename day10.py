N=int(input('enter a number:'))

if N%3==0 and N%5==0:
    print('fizze and buzze')
elif N%3==0:
    print('fizze')
elif N%5==0:
    print('buzze ')