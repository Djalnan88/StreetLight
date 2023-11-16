import random

card_name = [] # 카드 이름
card_type = [] # 카드 타입. 대답이 필요한 말의 타입과 카드의 타입을 비교해서 호감도를 결정한다.
cart_text = [] # 카드의 내용. script에서는 이 내용을 출력한다.
card_used = [] # 카드를 사용했는지 확인하기 위한 리스트. 카드를 사용하면 card_used에 카드의 인덱스가 추가된다. 매일 초기화되어야 한다.

item_name = [] # 아이템 이름
item_efec = [] # 아이템 효과

def get_card(name, type, text):
    card_name.append(name)
    card_type.append(type)
    cart_text.append(text)

def get_item(name, efec):
    item_name.append(name)
    item_efec.append(efec)

def choice_card(): # 대화에서 선택지가 나타날때 이 함수를 호출하여 나타날 선택지를 결정한다.
    u = [-1, -1, -1] # u[i]번째 카드가 선택지에 나타난다. 그 카드는 사용한 카드가 된다.
    for i in range(3):
        if u[i] == -1: # 카드가 사용되지 않았다면
            k = random.randint(0, len(card_name)) # 카드를 랜덤으로 선택한다.
            if len(card_name) == len(card_used): # 카드가 모두 사용되었다면
                break # 더 이상 카드를 선택하지 않는다. u[i]는 -1이 되고 script에서는 u[i]가 -1이면 "아무 말도 하지 않는다"는 선택지가 나타난다.
            if k not in card_used: # 카드가 사용되지 않았다면
                u[i] = k
                card_used.append(k)
            else:
                i -= 1
    return u

def diff_like(text_type): # 호감도를 결정하는 함수. script에서 호감도를 결정할때 이 함수를 호출한다.
    if text_type == card_type:
        return 10
    return -10