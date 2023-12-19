def TowerOfHanoi(n, source, auxilary, destination):
    if n == 1:
        print("Move disk 1 from source",source,"to destination",destination)
        return
    TowerOfHanoi(n-1, source, auxilary, destination)
    print("Move disk ",n, "from source ",source,"to destination ",destination)
    TowerOfHanoi(n-1, auxilary, destination, source)

TowerOfHanoi(3, 'A', 'B', 'C')

