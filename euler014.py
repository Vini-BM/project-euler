from functions import collatz_sequence_len

max_len = 1
values = {1:1}
for i in range(50000,1000000):
    seq_len = collatz_sequence_len(i,values)
    if seq_len > max_len:
        max_len = seq_len
        num_max = i

print(max_len, num_max)