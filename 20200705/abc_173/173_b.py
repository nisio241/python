n = int(input())
s = [input() for i in range(n)]
print('AC x %d' % (s.count('AC')))
print('WA x %d' % (s.count('WA')))
print('TLE x %d' % (s.count('TLE')))
print('RE x %d' % (s.count('RE')))
