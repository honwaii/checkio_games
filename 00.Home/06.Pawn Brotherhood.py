def safe_pawns():
    coordinates = input()

coordinates = {"b4", "c4", "d4", "e4", "f4", "g4", "e5"}
safe_pawn =[]
coordinates=list(coordinates)
for i in range(len(coordinates)):
    a=list(coordinates[i])

    x_left=chr(ord(a[0])-1)
    y_left=int(a[1])-1
    if a[0] == 'a':
        x_left='b'
    if y_left==0:
        y_left=1

    x_right=chr(ord(a[0])+1)
    y_right=int(a[1])-1
    if a[0] == 'h':
        x_right='g'
    if y_right==0:
        y_right=1

    coordinate1=''.join((str(x_left),str(y_left)))
    coordinate2=''.join((str(x_right),str(y_right)))

    if (coordinate1 in coordinates) or (coordinate2 in coordinates):
        safe_pawn.append(coordinates[i])
        print(coordinates[i],coordinate1,coordinate2)

print(safe_pawn,len(safe_pawn ))


