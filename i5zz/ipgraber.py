import random
logo = ("""

                     ██████╗  ██╗ ███████╗ ███████╗ ███████╗ 
                    ██╔═══██╗ ██║ ██╔════╝ ╚══███╔╝ ╚══███╔╝ 
                    ██║██╗██║ ██║ ███████╗   ███╔╝    ███╔╝  
                    ██║██║██║ ██║ ╚════██║  ███╔╝    ███╔╝   
                    ╚█║████╔╝ ██║ ███████║ ███████╗ ███████╗ 
                     ╚╝╚═══╝  ╚═╝ ╚══════╝ ╚══════╝ ╚══════╝ 
                     FOLLOW ME ON INSTAGRAM FOR MORE LIKE THAT @i5zz

""")
print(logo)
try:
  d = 0
  w = 0
  how = (int(input("[+] how many ips u want? : ")))
except:
  while True:
    o = open("list.txt", "a+")
    num1 = random.randint(1, 200)
    num2 = random.randint(1, 200)
    num3 = random.randint(1, 200)
    num4 = random.randint(1, 200)
    num5 = random.randint(1, 200)
    ip = (str(f"{num1}.{num2}.{num3}.{num4}"))
    o.write(ip + "\n")
    w += 1
    print(f"[+] DONE SAVE IPS IN FILE {w}")
    o.close()
  w = 0
  exit()

while w < how:
 o = open("list.txt", "a+")
 num1 = random.randint(1,200)
 num2 = random.randint(1,200)
 num3 = random.randint(1,200)
 num4 = random.randint(1,200)
 num5 = random.randint(1,200)
 ip = (str(f"{num1}.{num2}.{num3}.{num4}"))
 o.write(ip+"\n")
 w += 1
 print(f"[+] DONE SAVE IPS IN FILE {w}")
 o.close()
print("[#] thx for using this Tool ")