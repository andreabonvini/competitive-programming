import sys
T = int(sys.stdin.readline().strip())
for i in range(T):
    N = int(sys.stdin.readline().strip())
    lydia_path = list(sys.stdin.readline().strip())
    my_path = ['S' if step == 'E' else 'E' for step in lydia_path]
    my_path = ''.join(my_path)
    print('Case #{}: {}'.format(i+1,my_path))