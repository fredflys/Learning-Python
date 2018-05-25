# 两个玩家玩游戏，并公布其中一个玩家的得分
def play(score0=0, score1=0, say=None):
    score0 += 10
    # say(score0, score1)
    f = say(score0, score1)  # 通过绑定变量记住上次函数的执行状态，否则就会丢失，每次都会创建新的frame
    score0 += 8
    # say(score0, score1)
    g = f(score0, score1)
    score1 += 80
    # say(score0, score1)
    g(score0, score1)


def announce_gain_for_player_0(previous_score):
    def say(score0, score1):
        gain = score0 - previous_score
        print('Player 0 gained ', gain)
        return announce_gain_for_player_0(score0)
    # 返回内层函数
    return say


def announce_gain(who, previous_score):
    def say(score0, score1):
        if who == 0:
            score_I_care_about = score0
        elif who == 1:
            score_I_care_about = score1
        gain = score_I_care_about - previous_score
        print('Player %s gained %s' % (who, gain) )
        return announce_gain(who, score_I_care_about)
    # 返回内层函数
    return say

# play(0, 0, announce_gain_for_player_0(0))


play(0, 0, announce_gain(0, 0))
