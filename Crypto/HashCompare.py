#Compare hash

hash1 = list("20f911e5355d2acb45ac64997f65c09ddfcee9a5f733fd87880a543011f1542f")
hash2 = list("deb865ddc0ba5cc7e38db5f01ea0670399931874ec47cca9310ec1bc2a50a1c6")
ct = 0
print(len(hash1))
print(len(hash2))

for i in range(len(hash1) - 1):
    if hash1[i] == hash2[i]:
        ct += 1
        print(f"index: {i} symbol {hash1[1]} - {hash2[i]}")