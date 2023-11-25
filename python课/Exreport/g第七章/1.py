# 手算111瓶，电脑算的113瓶，不知道为啥
def Mai(ping,gai,shui):
    if gai<3 and ping<2:
        return shui
    else:
        shui_new=ping//2+gai//3
        ping=ping%2+shui_new
        gai=gai%3+shui_new
        shui=shui+shui_new
        return Mai(ping,gai,shui)
ping1=20
gai1=20
shui1=20
shui_total=Mai(ping1,gai1,shui1)
print(shui_total)


def Mai(ping,gai,shui):
    if gai < 3 and ping<2:
        return shui
    else:
        shui_new=ping//2+gai//3
        ping=ping%2+shui_new
        gai=gai%3+shui_new
        shui=shui+shui_new
        return Mai(ping,gai,shui)
ping1=20
gai1=20
shui1=20
shui_total=Mai(ping1,gai1,shui1)
print(shui_total)