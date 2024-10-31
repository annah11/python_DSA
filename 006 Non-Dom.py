def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
    
    for k in range(n):
        print(k)

print_items(10)
# non dominant items O(n^2) +O(n)=O(n^2+n) == O(n^2) is dominat term and n is non dominat term so we drop non dominat term
