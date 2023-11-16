# 이 파일에 게임 스크립트를 입력합니다.
init python:
    import eve

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"
image streetlight = "images/streetlight.jpg"
image girl cry = "images/girlcry.jpg"
define girl_image = ["images/girlsmile.jpg","images/girlsmile1.jpg","images/girlsmile2.jpg","images/girlsmile3.jpg","images/girlsmile4.jpg","images/girlsmile5.jpg","images/girlsmile6.jpg","images/girlsmile7.jpg"]

# scene expression girl_image[0]:
#     zoom 0.5  화면에 맞추려면 이렇게 써야됨

# 게임에서 사용할 캐릭터를 정의합니다.
define pimsi = Character('주인공', color="#c8ffc8")
define himsi = Character('???', color="#26ff00")
define h = Character('미가연', color="#26ff00")
define ajm = Character('술집 아주머니', color="#ff5500")
define nar = Character('', color="#0400ff")
define player_name = "플레이어이름"
define p = Character("player_name", dynamic=True, color="#c8ffc8")

$ like = 0
$ liver = 0
# 여기에서부터 게임이 시작합니다.
label start:
    jump day0
    return

label day0:
    centered "프롤로그"
    # 게임 시작 배경
    pimsi "그토록 원했던 D대학교에 입학했어!!"
    pimsi "드디어 마음대로 밤새서 게임도 하고 술도 먹고"
    pimsi "그리고 또..."
    pimsi "꿈에 그리던 여자친구도 만드는 거야!!!"
    pimsi "어? 내일은 수강신청 날이네."
    pimsi "오늘은 일찍 자야지!"
    pimsi "..."
    "쾅" with vpunch
    pimsi "앗! 수강신청에 늦겠다!"

    # 수강신청 배경
    nar "앞으로 당신의 선택에 따라 수업을 진행하게 됩니다."
    nar "각 수업을 통해 운명의 그녀와 가까워질 수도 멀어질 수도 있습니다."
    nar "수업들이 겹치지 않도록 좋은 시간표 만들어 주세요!!"

    # 술집 배경
    pimsi "드디어 대학교 와서 처음 먹어보는 술."
    pimsi "오늘은 수강신청도 성공했으니 달리는 거야!!!"
    # 아주머니 얼굴
    ajm "신분증 좀 보여주세요"
    # 아주머니 얼굴 사라짐
    # 신분증 사진
    $ player_name = renpy.input("이름을 입력하세요.")
    # 신분증 사진 사라짐
    # 술집 배경 사라짐
    
    # 밤의 길 배경
    p "으으... 어지러워"
    nar "술이 취해 정신을 못 차리는 [p]."
    nar "가로등 아래 낯선 여자가 서있다."
    nar "낯선 여자를 본 [p]. 그는 가로등 불빛 아래 그녀에게 다가간다…"
    p "저기... 엇..."
    scene expression girl_image[0]
    # 얼굴이 안보이는 여자 얼굴
    p "(가로등 빛이 너무 빛나서 얼굴이 보이지 않아)"
    "쿵" with vpunch
    p "으악!"
    himdi "죄송합니다. 괜찮으신가요?"
    "누군가와 부딫힌 [p]는 눈을 떠보니 가로등 빛에 휩싸여 있는 낯선 여자가 보인다."
    p "아... 괜찮아요."
    p "전 신입생 [p]입니다."
    himsi "안녕하세요. 저는 [h]에요."
    "너무 밝은 가로등 빛에 [h]의 얼굴이 보이지 않는다."
    "하지만 [p]는 [h]에게 마음의 끌림을 느낀다."
    # 배경 사라짐
    # 얼굴이 안보이는 여자 얼굴 사라짐

    return

label day1:
    centered "day1"
    p "으윽 머리야..."
    p "어제는 분명 그녀랑..."
    p "아 맞다! 수업 가야지!"
    return

label day2:

    return

label day3:

    return

label day4:

    return

label day5:

    return

label day6:
    
    return

label day7:

    return

label happy:

    return

label bad:
    
    return

label normal1:

    return

label normal2:

    return

label good:

    return
