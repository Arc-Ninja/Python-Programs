def toh(n,sor,dest,aux):
    if n==1:
        print(f"Move disk 1 from {sor} to {dest}")
        return
    toh(n-1,sor,aux,dest)
    print(f"Move disk {n} from {sor} to {dest}")
    toh(n-1,aux,dest,sor)

toh(3,'A','B','C')
    


