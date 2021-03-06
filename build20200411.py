# -*- coding=utf8 -*-
__author__ = "celian"
# date: 20200310
import random
import time
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

auto_setup(__file__)
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
ST.THRESHOLD = 0.9
time_list = [9.121231231241, 13.23234221, 22.3234404234, 32.43534223423, 26.3423423223, 59.231221212313, 45.32123123, 65.31231231,
             38.23242312312, 42.434566756564]
com_text_ed = ['分⁠钟⁠前⁠', '刚⁠刚⁠']
personal_num = 0
like_num = 0
view_all_num = 0
personal_mes = ["你的抖音拍摄的不错哦，是自己拍摄的还是团队运作的哈?", "你的抖音拍的好有趣呀，可以互粉一下不？", "你是天上派下来的小仙女吧，人间一般不会有你这么仙的？",
                "你的抖音拍摄的不错哦，是自己拍摄的还是团队运作的哈?", "你的抖音拍的好有趣呀，可以互粉一下不？"]
# ST.RBG = True
xy = poco.get_screen_size()
print(xy, type(xy))
x_pro = xy[0] / 1080
y_pro = xy[1] / 2080
start_app("com.ss.android.ugc.aweme")

start_time = time.time()
time.sleep(random.uniform(5, 10))


def close_prompts():
    """
    处理各种提示
    """
    ad = exists(Template(r"tpl1578550676487.png", record_pos=(-0.433, 0.473), resolution=(1080, 2246)))
    if ad:
        assert_exists(Template(r"tpl1578550676487.png", record_pos=(-0.433, 0.473), resolution=(1080, 2246)), "识别到广告")
        touch([790, 1499])
        time.sleep(0.52323123121)
        swipe([701 * x_pro, 1534 * y_pro], [537 * x_pro, 500 * y_pro])
    live_b = exists(Template(r"tpl1583994792867.png", record_pos=(-0.401, 0.514), resolution=(1080, 2246)))
    if live_b:
        assert_exists(Template(r"tpl1583994792867.png", record_pos=(-0.401, 0.514), resolution=(1080, 2246)),
                      "滑到直播了~往下滑")
        swipe([701 * x_pro, 1534 * y_pro], [537 * x_pro, 500 * y_pro])
#     re_friend = exists(Template(r"tpl1587603568240.png", record_pos=(0.021, -0.599), resolution=(1080, 2246)))
#     if re_friend:
#         assert_exists(Template(r"tpl1587603568240.png", record_pos=(0.021, -0.599), resolution=(1080, 2246)), "识别到好友推荐")
#         keyevent("BACK")
#     iget = exists(Template(r"tpl1578707054248.png", record_pos=(-0.006, 0.397), resolution=(1080, 2246)))
#     if iget:
#         assert_exists(Template(r"tpl1578707054248.png", record_pos=(-0.006, 0.397), resolution=(1080, 2246)),
#                       "关闭“我知道了”弹窗")
#         touch(iget)
#     keep_use = exists(Template(r"tpl1579482722575.png", record_pos=(-0.203, 0.161), resolution=(1080, 2246)))
#     if keep_use:
#         assert_exists(Template(r"tpl1579482722575.png", record_pos=(-0.203, 0.161), resolution=(1080, 2246)),
#                       "关闭“继续使用”弹窗")
#         touch(keep_use)
    #     wan = exists(Template(r"tpl1578724140152.png", record_pos=(-0.093, 0.619), resolution=(1080, 2246)))
    #     touch(wan) if wan else None
    #     time.sleep(0.13135423)
#     w_a_min = exists(Template(r"tpl1578708311737.png", record_pos=(-0.188, 0.351), resolution=(1080, 2246)))
#     if w_a_min:
#         assert_exists(Template(r"tpl1578708311737.png", record_pos=(-0.188, 0.351), resolution=(1080, 2246)), "关闭弹窗")
#         touch(w_a_min)
#     later_times = exists(Template(r"tpl1578469894095.png", record_pos=(-0.19, 0.325), resolution=(1080, 2246)))
#     if later_times:
#         assert_exists(Template(r"tpl1578469894095.png", record_pos=(-0.19, 0.325), resolution=(1080, 2246)), "关闭弹窗")
#         touch(later_times)
#     cancel = exists(Template(r"tpl1578537687104.png", record_pos=(-0.19, 0.343), resolution=(1080, 2246)))
#     if cancel:
#         assert_exists(Template(r"tpl1578537687104.png", record_pos=(-0.19, 0.343), resolution=(1080, 2246)), "关闭弹窗")
#         touch(cancel)
    next_time = exists(Template(r"tpl1578471300734.png", record_pos=(-0.191, 0.33), resolution=(1080, 2246)))
    if next_time:
        assert_exists(Template(r"tpl1578471300734.png", record_pos=(-0.191, 0.33), resolution=(1080, 2246)), "关闭弹窗")
        touch(next_time)


def per_message_in_profile(per_num, per_mes, i, title):
    # 进入主页后进行私信的操作
    if exists(Template(r"tpl1582768862847.png", rgb=True, record_pos=(-0.447, 0.074), resolution=(1080, 2246))):
        assert_exists(Template(r"tpl1582768862847.png", rgb=True, record_pos=(-0.447, 0.074), resolution=(1080, 2246)),
                      "识别到性别男，返回")
    elif exists(Template(r"tpl1582771125790.png", rgb=True, record_pos=(-0.447, 0.352), resolution=(1080, 2246))):
        assert_exists(Template(r"tpl1582771125790.png", rgb=True, record_pos=(-0.447, 0.352), resolution=(1080, 2246)),
                      "识别到性别女")
        if exists(Template(r"tpl1583737795252.png", threshold=0.9, rgb=True, record_pos=(-0.331, 0.394),
                           resolution=(1080, 2246))):
            fans = poco(textMatches='粉丝')
            fans_num = fans.parent().child().get_text()
            if "w" in fans_num:
                fans_num = float(fans_num.replace("w", ""))
            else:
                fans_num = float(fans_num) / 10000
            if fans_num >= 50.0:
                p = poco(textMatches='作品.*').get_text()
                p_num = p.split(" ")
                p_num = p_num[1]
                if "w" in p_num:
                    p_num = int(p_num.replace("w", ""))
                else:
                    p_num = int(p_num) / 10000
                if p_num > 0:
                    assert_exists(Template(r"tpl1583737795252.png", threshold=0.9, rgb=True, record_pos=(-0.331, 0.394),
                                           resolution=(1080, 2246)), "识别到有作品，进行私信")
                    sleep(0.52312312)
                    like = poco(textMatches='获赞').parent().child()
                    liked = like.get_text()
                    sleep(0.3121212312)
                    if liked != "0":
                        log("有获赞，进行私信")
                        awame_id = poco(textMatches='抖音号：.*').get_text()
                        log("获取名字和ID")
                        gz = exists(Template(r"tpl1582699886448.png", record_pos=(0.094, -0.603), resolution=(1080, 2246)))
                        if gz:
                            touch(gz)
                            time.sleep(1.1234342345)
                        if exists(Template(r"tpl1582774228352.png", rgb=True, record_pos=(0.27, 0.051),
                                           resolution=(1080, 2246))):
                            touch(exists(Template(r"tpl1582774228352.png", rgb=True, record_pos=(0.27, 0.051),
                                                  resolution=(1080, 2246))))
                            time.sleep(0.6234342345)
                            keyevent("BACK")
                            time.sleep(0.732123123)
                        sixin = exists(
                            Template(r"tpl1582699919607.png", record_pos=(0.238, -0.605), resolution=(1080, 2246)))
                        if sixin:
                            touch(sixin)
                            time.sleep(1.23434234)

                            qx = exists(
                                Template(r"tpl1582700152176.png", record_pos=(0.129, 0.051), resolution=(1080, 2246)))
                            if qx:
                                touch(qx)
                                time.sleep(0.45324543)

                            touch(Template(r"tpl1582700289183.png", record_pos=(-0.217, 0.814), resolution=(1080, 2246)))
                            time.sleep(0.3233234)
                            text(per_mes[i])
                            time.sleep(0.1233234)
                            keyevent("DEL")
                            time.sleep(1.12321321)

                            touch(Template(r"tpl1587352197152.png", record_pos=(0.433, 0.819), resolution=(1080, 2246)))

                            with open("log.txt", "a", encoding="utf-8")as f:
                                if exists(Template(r"tpl1583724100277.png", record_pos=(-0.002, -0.153),
                                                   resolution=(1080, 2246))):
                                    log(title + awame_id + "  私信成功，有提示")
                                    f.write(title + "/" + awame_id + "  私信成功，有提示" + "\n")

                                else:
                                    log(title + awame_id + "  私信成功，无提示")
                                    f.write(title + "/" + awame_id + "  私信成功，无提示" + "\n")
                                    # 返回评论列表
                            log("私信完成，返回评论列表")
                            time.sleep(1.123123124)
                            keyevent("BACK")
                            per_num += 1
                            time.sleep(1.732123123)

    keyevent("BACK")
    time.sleep(1.032123123)
    return per_num


def watch_issue():
    """
    浏览热搜话题
    :return:
    """
    poco(descMatches='搜索').click()
    sleep(1.1252325231)
    for j in range(3):
        hot_issue = exists(Template(r"tpl1586309456991.png", record_pos=(-0.132, -0.574), resolution=(1080, 2246)))
        if hot_issue:
            touch(hot_issue)
            sleep(2.4234212342)
            issue = exists(Template(r"tpl1587884103801.png", rgb=True, record_pos=(-0.352, -0.354), resolution=(1080, 2246)))
            if issue:
                touch(issue)
            else:
                poco(descMatches='视频封面').click()
                sleep(2.323213432467)
            view_num = 0
            for i in range(3):
                # 随机点赞评论
                sleep(random.choice(time_list))
                if view_num in [0, ]:
                    touch([liked_button[0], liked_button[1]-80])
                swipe([690, 1717], [693, 550])
                view_num += 1
            keyevent("BACK")
            sleep(1.322524232)
            touch(Template(r"tpl1586339535355.png", record_pos=(0.281, -0.885), resolution=(1080, 2246)))
            sleep(2.314541231)
    keyevent("BACK")
    sleep(1.322524232)
    keyevent("BACK")
    sleep(1.322524232)


def watch_same_city():
    """
    浏览一下同城视频
    :return:
    """
    poco(textMatches='同城').click()
    yh = exists(Template(r"tpl1585732936373.png", record_pos=(-0.192, 0.329), resolution=(1080, 2246)))
    if yh:
        touch(yh)
        sleep(2.212314123123)
    location = exists(Template(r"tpl1586592994250.png", record_pos=(-0.33, -0.761), resolution=(1080, 2246)))
    if location:
        touch([location[0] + 100, location[1] + 500])
    for i in range(5):
        sleep(random.choice(time_list))
        swipe([690 * x_pro, 1717 * y_pro], [693 * x_pro, 550 * y_pro])

    keyevent("BACK")
    sleep(1.322524232)
    touch(Template(r"tpl1586593658450.png", record_pos=(-0.396, 0.819), resolution=(1080, 2246)))
    sleep(3.31231231234)
    try:
        poco(textMatches='推荐').click()
    except:
        pass


def watch_follow(personal_num):
    """
    浏览关注
    :param personal_num:
    :return:
    """
    touch(follow_button)
    sleep(3.23423523453)
    swipe([602,1478], [504,1150])
    not_follow = exists(Template(r"tpl1587870176479.png", record_pos=(0.006, 0.022), resolution=(1080, 2246)))
    if not_follow:
        poco(textMatches='推荐').click()
    else:
        for i in range(8):
            personal_num = like_and_comment_in_view(personal_num, 1.0, 100.0, 1.0)
            
    return personal_num


def comment():
    """
    评论
    """
    comment_list = ["你骗狗！！！", "骗狗进来杀", "就不@我家狗子过来看了", "哦豁~~", "就，挺突然的", "喜欢", "恕我直言", "赞了啊"]
    poco(descMatches='^评论.*').click()
    # 往下滑 浏览浏览评论
    for i in range(2):
        sleep(5.13468937694)
        swipe([690 * x_pro, 1717 * y_pro], [693 * x_pro, 550 * y_pro])
        long_click = exists(Template(r"tpl1588900433923.png", threshold=0.9, rgb=True, record_pos=(-0.319, 0.103), resolution=(1080, 2246)))

        if long_click:
            keyevent("BACK")
    sleep(2.21215478)
    poco(textMatches='.*精彩评论吧').click()
    sleep(2.3456623112)
    text(random.choice(comment_list))
    sleep(0.1233234)
    keyevent("DEL")
    n = random.choice(range(8))
    face = poco(descMatches='^\[.*\]')
    face_all = face.parent().parent()
    face_all.child()[n].click()
    send_bu = exists(Template(r"tpl1585731333569.png", record_pos=(0.422, 0.543), resolution=(1080, 2246)))
    if send_bu:
        touch(send_bu)
    keyevent("BACK")
    sleep(2.325323135)
#     swipe([690 * x_pro, 1717 * y_pro], [693 * x_pro, 550 * y_pro])

    
def per_mess(per_num):
    """
    在主页点开评论页面进行操作

    """
    poco(descMatches='^评论.*').click()
    time.sleep(2.123123123)
    if exists(Template(r"tpl1583829617112.png", record_pos=(0.001, -0.536), resolution=(1080, 2246))):
        assert_exists(Template(r"tpl1583829617112.png", record_pos=(0.001, -0.536), resolution=(1080, 2246)),
                      "没有评论，返回，刷下一条视频")
        keyevent("BACK")
        time.sleep(0.032123123)
        keyevent("BACK")
        time.sleep(0.032123123)
        keyevent("BACK")
        time.sleep(0.032123123)
    else:
        comment_num = poco(textMatches='.*评论').get_text()
        if comment_num != "暂无评论":
            comment_num = comment_num.split(" ")[0]
            if "w" in comment_num:
                comment_num = float(comment_num.replace('w', ''))
            else:
                comment_num = int(comment_num) / 10000
            if comment_num > 0.01:
                swipe([690 * x_pro, 1717 * y_pro], [693 * x_pro, 550 * y_pro])
                time.sleep(1.54323312)
                for i in range(random.randint(0, 5)):
                    sleep(2.311111)
                    try:
                        co = poco(textMatches='.*分⁠钟⁠前⁠').parent()
                        co_p = co.parent()
                        co_pp = co_p.parent()
                        co_text = poco(co_pp.get_name()).child(co_p.get_name())[1].child().child()[4].get_text()
                        if "@" not in co_text:
                            for j in com_text_ed:
                                if j in co_text:
                                    poco(co_pp.get_name()).child(co_p.get_name())[1].child().child()[2].click()
                                    sleep(0.634241231)
                                    assert_exists(Template(r"tpl1583984257428.png", record_pos=(0.432, -0.121),
                                                           resolution=(1080, 2246)), "评论点赞")
                                    time.sleep(0.8312124212)
                                    #                                 ti = poco(textMatches='.*分⁠钟⁠前⁠').parent()
                                    tit = poco(co_pp.get_name()).child(co_p.get_name())[1].child().child()[0]
                                    title = tit.get_text()
                                    tit.click()
                                    time.sleep(1.634572342)
                                    assert_exists(Template(r"tpl1583984298780.png", record_pos=(-0.404, -0.317),
                                                           resolution=(1080, 2246)), "进入点赞对象主页")

                                    personal_num = per_message_in_profile(per_num, personal_mes, i, title)
                                    log(str(personal_num))
                                    if personal_num >= 20:
                                        break
                                    n_time = time.time()
                                    r_time = n_time - start_time
                                    if r_time > 3550:
                                        break
                                    swipe([690 * x_pro, 1717 * y_pro], [693 * x_pro, 550 * y_pro])
                    except:
                        pass
                    try:
                        co = poco(textMatches='.*刚⁠刚⁠').parent()
                        co_p = co.parent()
                        co_pp = co_p.parent()
                        co_text = poco(co_pp.get_name()).child(co_p.get_name())[1].child().child()[4].get_text()
                        for j in com_text_ed:
                            if j in co_text:
                                poco(co_pp.get_name()).child(co_p.get_name())[1].child().child()[2].click()
                                sleep(0.634241231)
                                assert_exists(Template(r"tpl1583984257428.png", record_pos=(0.432, -0.121),
                                                       resolution=(1080, 2246)), "评论点赞")
                                time.sleep(0.8312124212)
                                #                                 ti = poco(textMatches='.*分⁠钟⁠前⁠').parent()
                                tit = poco(co_pp.get_name()).child(co_p.get_name())[1].child().child()[0]
                                title = tit.get_text()
                                tit.click()
                                time.sleep(1.634572342)
                                assert_exists(Template(r"tpl1583984298780.png", record_pos=(-0.404, -0.317),
                                                       resolution=(1080, 2246)), "进入点赞对象主页")

                                per_num = per_message_in_profile(per_num, personal_mes, i, title)
                                log(str(per_num))
                                if per_num >= 20:
                                    break
                                n_time = time.time()
                                r_time = n_time - start_time
                                if r_time > 3550:
                                    break
                                swipe([690 * x_pro, 1717 * y_pro], [693 * x_pro, 550 * y_pro])
                    except:
                        pass
                    swipe([690 * x_pro, 1717 * y_pro], [693 * x_pro, 550 * y_pro])
                    long_click = exists(Template(r"tpl1588900433923.png", threshold=0.9, rgb=True, record_pos=(-0.319, 0.103), resolution=(1080, 2246)))
                    if long_click:
                        keyevent("BACK")
                    time.sleep(0.13468937694)
    # 滑下一条抖音
    keyevent("BACK")
    time.sleep(1.432123123)
    swipe([701 * x_pro, 1534 * y_pro], [537 * x_pro, 500 * y_pro])
    log("滑下一条抖音")
    log(str(per_num))
    return per_num


def like_and_comment_in_view(personal_num, liked_min, liked_max, commented):
    """
    浏览过程这点赞和评论的判断逻辑

    """
    like_bu = poco(descMatches='.*选中.*')
    liked_num_text = like_bu.child()[1].get_text()
    comment_bu = poco(descMatches='^评论.*')
    comment_num_text = comment_bu.child()[1].get_text()
    if "w" in liked_num_text:
        if liked_min < float(liked_num_text[:-1]) < liked_max:
            # 只点赞不评论
            sleep(random.choice(time_list[:4]))
            like_bu.click()
            sleep(1.3567855634234)
        elif float(liked_num_text[:-1]) > liked_max:
            # 点赞+评论
            sleep(random.choice(time_list[5:]))
            like_bu.click()
            sleep(1.3567855634234)
            comment()
        elif float(liked_num_text[:-1]) > 200.0:
            # 去主页
            touch(avatar)
            sleep(2.543656435)
            swipe([671, 1673], [619, 677])
            poco(descMatches='^视频[0-9]').click()
            for i in range(3):
                sleep(random.choice(time_list[:4]))
                rand_num = random.random()
                if rand_num > 0.5:
                    like_bu.click()
                swipe([701 * x_pro, 1534 * y_pro], [537 * x_pro, 500 * y_pro])
                # 视频量
            pass
        if "w" in comment_num_text:
            # 点赞超过30万，评论超过2万，去评论找人私信
            if liked_min < float(liked_num_text[:-1]) and float(comment_num_text[:-1]) > commented:
                # 满足条件还要随机是否要去私信 0和1
                rand_num = random.random()
                if rand_num > 0.5:
                    # 挑选评论进行私信
                    personal_num = per_mess(personal_num)
                
    swipe([701 * x_pro, 1534 * y_pro], [537 * x_pro, 500 * y_pro])
    return personal_num


def only_watch_issue(like_bu):
    """
    只浏览热点，热搜榜
    :return:
    """
    issue = []
    poco(descMatches='搜索').click()
    sleep(1.1252325231)
    # 热搜榜上浏览几个话题
    for j in range(3):
        hot_issue = exists(Template(r"tpl1589017048067.png", record_pos=(-0.133, -0.119), resolution=(1080, 2246)))
        if hot_issue:
            touch(hot_issue)
            ca = poco(textMatches='取消')
            watched_issue = ca.parent().child()[0].child().get_text()
            if watched_issue in issue:
                keyevent("BACK")
                touch([hot_issue[0]-150, hot_issue[1]+120])
            sleep(5.1346786754354)
            swipe([521, 1756], [424, 702])
            poco(descMatches='视频封面').click()
            sleep(5.12346786786)
            w = exists(Template(r"tpl1586857296293.png", record_pos=(0.447, 0.049), resolution=(1080, 2246)))
            """
            浏览过程
            """
            if w:
                for t in range(random.choice([3, 4, 5])):
                    sleep(random.choice(time_list[5:]))
                    rand_num = random.random()
                    if rand_num > 0.5:
                        touch([like_bu[0], like_bu[1]-80])
                        sleep(1.3567855634234)
                    swipe([390, 1487], [693, 550])
            else:
                for t in range(random.choice([1, 2, 3])):
                    sleep(random.choice(time_list[:5]))
                    rand_num = random.random()
                    if rand_num > 0.5:
                        touch([like_bu[0], like_bu[1]-80])
                        sleep(1.3567855634234)
                    swipe([690, 1487], [693, 550])
            keyevent("BACK")
            sleep(1.322524232)
            ca = poco(textMatches='取消')
            watched_issue = ca.parent().child()[0].child().get_text()
            if watched_issue not in issue:
                issue.append(watched_issue)
            keyevent("BACK")
            sleep(1.322524232)
            
    # 热点榜
    touch(Template(r"tpl1586852248417.png", record_pos=(-0.137, -0.271), resolution=(1080, 2246)))
    issue_no = [Template(r"tpl1586854489061.png", record_pos=(-0.429, 0.01), resolution=(1080, 2246)),
                Template(r"tpl1586854584271.png", record_pos=(-0.427, 0.144), resolution=(1080, 2246)),
                Template(r"tpl1586854594485.png", record_pos=(-0.431, 0.278), resolution=(1080, 2246))]
    for i in issue_no:
        # 按顺序浏览热点榜
        point1 = exists(i)
        if point1:
            if issue_no.index(i) < 3:
                touch([point1[0]+400, point1[1]])
            else:
                touch([point1[0]-100, point1[1]])
            w = exists(Template(r"tpl1586857296293.png", record_pos=(0.447, 0.049), resolution=(1080, 2246)))
            if w:
                for t in range(random.choice([3, 4, 2])):
                    sleep(random.choice(time_list[5:]))
                    rang_num = random.random()
                    if rang_num > 0.5:
                        touch(like_bu)
                        sleep(1.3567855634234)
                    swipe([690, 1487], [693, 550])
            else:
                for t in range(random.choice([1, 2, 1])):
                    sleep(random.choice(time_list[:5]))
                    rand_num = random.random()
                    if rand_num > 0.5:
                        touch(like_bu)
                        sleep(1.3567855634234)
                    swipe([690, 1487], [693, 550])
            # 返回榜单首页
            keyevent("BACK")
            sleep(1.322524232)
    # 进入热点完整榜
    touch(Template(r"tpl1589188197607.png", record_pos=(0.016, 0.481), resolution=(1080, 2246)))
    sleep(3.35646767568)
    issue_no2= [Template(r"tpl1589182037502.png", record_pos=(-0.436, 0.273), resolution=(1080, 2246)),
                Template(r"tpl1589182049510.png", record_pos=(-0.433, 0.409), resolution=(1080, 2246)), 
                Template(r"tpl1589182060442.png", record_pos=(-0.439, 0.54), resolution=(1080, 2246)), 
                Template(r"tpl1589182069142.png", record_pos=(-0.435, 0.673), resolution=(1080, 2246)), 
                Template(r"tpl1589182078144.png", record_pos=(-0.436, 0.806), resolution=(1080, 2246)),
                Template(r"tpl1589188574269.png", record_pos=(-0.418, 0.619), resolution=(1080, 2246)),
                Template(r"tpl1589188600057.png", record_pos=(-0.431, 0.748), resolution=(1080, 2246))]
    for i in random.sample(issue_no2, 3):
        point1 = exists(i)
        if point1:
            if issue_no.index(i) < 3:
                touch([point1[0]+400, point1[1]])
            else:
                touch([point1[0]-100, point1[1]])
            w = exists(Template(r"tpl1586857296293.png", record_pos=(0.447, 0.049), resolution=(1080, 2246)))
            if w:
                for t in range(random.choice([3, 4, 2])):
                    sleep(random.choice(time_list[5:]))
                    rang_num = random.random()
                    if rang_num > 0.5:
                        touch(like_bu)
                        sleep(1.3567855634234)
                    swipe([690, 1487], [693, 550])
            else:
                for t in range(random.choice([1, 2, 1])):
                    sleep(random.choice(time_list[:5]))
                    rand_num = random.random()
                    if rand_num > 0.5:
                        touch(like_bu)
                        sleep(1.3567855634234)
                    swipe([690, 1487], [693, 550])
            # 返回榜单首页
            keyevent("BACK")
            sleep(1.322524232)


try:
    poco(textMatches='推荐').click()
except:
    pass
close_prompts()
# 先获取主页面各种按钮的坐标
# 同城，消息，关注，点赞，评论，分享，搜索
# 同城
same_city_position = poco(textMatches='同城').get_position()
same_city_button = [same_city_position[0] * xy[0], same_city_position[1] * xy[1]]
# 消息
message_position = poco(textMatches='消息').get_position()
message_button = [message_position[0] * xy[0], message_position[1] * xy[1]]
# 关注
follow_position = poco(textMatches='关注').get_position()
follow_button = [follow_position[0] * xy[0], follow_position[1] * xy[1]]
# 分享
share_position = poco(descMatches='^分享.*').get_position()
share_button = [share_position[0] * xy[0], share_position[1] * xy[1]]
# 搜索
search_position = poco(descMatches='搜索').get_position()
search_button = [search_position[0] * xy[0], search_position[1] * xy[1]]
# 评论按钮坐标
comm_position = poco(descMatches='^评论.*').get_position()
comm_button = [comm_position[0] * xy[0], comm_position[1] * xy[1]]
# 点赞按钮坐标
liked_position = poco(descMatches='.*选中.*').get_position()
liked_button = [liked_position[0] * xy[0], liked_position[1] * xy[1]]
# 头像坐标
title = poco("com.ss.android.ugc.aweme:id/title").get_text()
avatar = poco(descMatches=title[1:])

rand_num = random.random()
if rand_num > 0.4:
    while True:
        # 检查弹窗
        close_prompts()
        # 普通刷视频模式
        # 判断视频热度然后进行点赞评论
        # 浏览过程中随机点赞评论
        print(rand_num)
        personal_num = like_and_comment_in_view(personal_num, 30.0, 100.0, 2.0)
        # 下一条视频
#         swipe([701 * x_pro, 1534 * y_pro], [537 * x_pro, 500 * y_pro])
        view_all_num += 1
        if view_all_num == random.choice(range(5, 10)):
            rand_num = random.random()
            if rand_num > 0.5:
                watch_issue()
        elif view_all_num == random.choice(range(10, 15)):
            rand_num = random.random()
            if rand_num > 0.5:
                watch_same_city()
        elif view_all_num == random.choice(range(15, 25)):
            rand_num = random.random()
            if rand_num > 0.5:
                personal_num = watch_follow(personal_num)
        # 到指定视频量之后随机进入相应功能
        if personal_num >= 20:
            break
        # 查看时间
        n_time = time.time()
        r_time = n_time - start_time
        if r_time > 3600:
            break
else:
    only_watch_issue(liked_button)
time.sleep(1)
log("运行完毕")
stop_app("com.ss.android.ugc.aweme")
time.sleep(1)
keyevent("HOME")

# exists(Template(r"tpl1586918347303.png", record_pos=(-0.339, 0.683), resolution=(1080, 2246)))
# exists(Template(r"tpl1587603568240.png", record_pos=(0.021, -0.599), resolution=(1080, 2246)))
# exists(Template(r"tpl1589009679469.png", record_pos=(-0.023, -0.123), resolution=(1080, 2246)))

