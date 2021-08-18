seq = 'ATGCGACTACGATCGAGGGCCAT'
new_seq = ""
for i in seq:
    if i == "T":
        new_seq += "U"
    else:
        new_seq += i
print(new_seq)
