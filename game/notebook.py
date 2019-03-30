import matplotlib.pyplot as plt
import ctypes
import random
import time
from numba.decorators import jit

number = 5
area_range_max = 25
area_range_min = 1


def get_key(ky):
    return bool(ctypes.windll.user32.GetAsyncKeyState(ky) & 0x8000)


@jit
def realtime_graph(xgm, ygm, xm, ym, enemy_x, enemy_y):
    plt.plot(xgm, ygm, c="grey", marker="s", markersize=10)
    plt.plot(xm, ym, c="navy", marker="o", markersize=10)
    plt.scatter(enemy_x, enemy_y, c="gold", marker="X", s=100)
    plt.xticks(color="None")
    plt.yticks(color="None")
    plt.tick_params(length=0)
    plt.xlim([area_range_min-1, area_range_max+1])    # x軸範囲
    plt.ylim([area_range_min-1, area_range_max+1])    # y軸範囲
    plt.pause(0.001)     # 更新時間間隔
    plt.clf()           # 画面初期化


def enemies_generator(enemy_num):  # 任意の数のenemy生成
    def enemy_generate():
        # enemy_random_list = random.randrange(area_range_min, area_range_max+1), selector = random.randrange(-1, 1+1)
        return [random.randrange(area_range_min, area_range_max+1), random.randrange(-1, 1+1)]

    enemy_list = list()
    for num in range(enemy_num):
        enemy = list()
        for e in range(2):  # x and y
            enemy.append(enemy_generate())
        enemy_list.append(enemy)
    return enemy_list
    # [ [[random_list_x, selector_x],[random_list_y, selector_y]], []...* enemy_num ]


def enemies_move(enemy_list):
    def positive_negative_changer(enemy_random_num, pnc):
        if area_range_max <= enemy_random_num and pnc == 1:
            pnc = -1
        elif enemy_random_num <= area_range_min and pnc == -1:
            pnc = 1
        else:
            pass
        return pnc

    def increase(enemy_random_num, pnc):
        enemy_random_num += pnc
        return enemy_random_num, pnc

    def enemy_list_make(xy_list):
        x = list()
        y = list()
        for xy in xy_list:
            x.append(xy[0][0])
            y.append(xy[1][0])
        return x, y

    for enemy in enemy_list:
        for e in enemy:
            e[0], e[1] = increase(e[0], positive_negative_changer(e[0], e[1]))
    return enemy_list_make(enemy_list)    # enemy_list_x, enemy_list_y


@jit
def move_in_map(xin_m, yin_m):
    if get_key(0x28):    # 真後'↓'
        yin_m -= 1
    elif get_key(0x25):    # 真左'←'
        xin_m -= 1
    elif get_key(0x27):    # 真右'→'
        xin_m += 1
    elif get_key(0x26):    # 真正面'↑'
        yin_m += 1
    return xin_m, yin_m


# 1Fにおいて、ゴールである"階段"までの移動テスト
@jit
def main():
    (x, y) = (7, 7)     # 初期値
    (xg, yg) = (3, 3)   # ランダム
    enemies = enemies_generator(number)     # 階層ごとに増やす
    plt.ion()           # 対話モードオン

    while True:
        ex, ey = enemies_move(enemies)
        if get_key(0x1B) or (x == xg and y == yg):  # ESCキー(仮想キーコード)が押されたら終了
            break

        if (area_range_min <= x <= area_range_max) and (area_range_min <= y <= area_range_max):
            realtime_graph(xg, yg, x, y, ex, ey)
        else:
            continue
        x, y = move_in_map(x, y)

    plt.close()


if __name__ == '__main__':
    main()
