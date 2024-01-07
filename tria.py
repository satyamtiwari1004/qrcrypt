import os
path="C:/QrCrypt"+"/2018-02-24/img.png"
head, tail = os.path.split(path)
if not os.path.exists(head):
    os.makedirs(head)
print(head)
