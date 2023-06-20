import pygame as pg
import sys
from random import randint
# 練習4:こうかとんと爆弾が画面にでないようにする
def check_bound(obj: pg.Rect, area: pg.Rect) -> tuple[bool, bool]:
    """
    こうかとんRect，爆弾Rectが画面外 or 画面内かを判定する関数
    引数：こうかとんRect or 爆弾Rect
    戻り値：横方向，縦方向の判定結果タプル（True：画面内／False：画面外）
    """
    yoko, tate = True, True
    if obj.left < area.left or area.right < obj.right: # 横方向のはみ出し判定
        yoko = False
    if obj.top < area.top or area.bottom < obj.bottom: # 縦方向のはみ出し判定
        tate = False 
    return yoko, tate
def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img2 = pg.transform.flip(kk_img, True, False) #反転させたこうかとん
    kk_img2 = pg.transform.flip(kk_img, True, False) # 反転させたこうかとん
    tmr = 0
    # 練習1:半径10,色：赤の円で爆弾を作成する
    bb_img = pg.Surface((20, 20))  # ボムのサーフェイスを作成する
    pg.draw.circle(bb_img, (255, 0, 0), (10, 10), 10)  # ボムを描画する
    bb_img.set_colorkey((0, 0, 0)) #背景を透明にする
    # 練習1：爆弾をランダムに配置する
    bb_rct = bb_img.get_rect()  # 爆弾のrectをとる
    scr_rct = screen.get_rect()  # 画面のrectをとる
    bb_rct.center = (randint(0, scr_rct.width), randint(0, scr_rct.height))
    bb_rct.center = (randint(0, scr_rct.width),
                      randint(0, scr_rct.height))
    # 練習2:爆弾を移動させる
    vx = +1  # 横方向速度
    vy = +1  # 縦方向速度
    # 練3:こうかとんを矢印キーで移動できるようにする
    kk_rct = kk_img.get_rect()  # こうかとんのrectをとる
    kk_rct.center = 900, 400    # こうかとんの初期位置を入れる
    # キー入力の辞書を作成する
    key_dct = {
        pg.K_UP:    (0, -5),
        pg.K_DOWN:  (0, +5),
        pg.K_LEFT:  (-5, 0),
        pg.K_RIGHT: (+5, 0),
    }
    # こうかとんが向いている方向を示す辞書
    delta= {
        ( 0,  0): pg.transform.rotozoom(kk_img, 0, 2.0),
        (-5, -5): pg.transform.rotozoom(kk_img,-45,2.0),
        (-5,  0): pg.transform.rotozoom(kk_img, 0, 2.0),
        (-5, +5): pg.transform.rotozoom(kk_img, 45, 2.0),
        ( 0, +5): pg.transform.rotozoom(kk_img2, -90, 2.0),
        (+5, +5): pg.transform.rotozoom(kk_img2, -45, 2.0),
        (+5,  0): pg.transform.rotozoom(kk_img2, 0, 2.0),
        (+5, -5): pg.transform.rotozoom(kk_img2, 45, 2.0),
        ( 0, -5): pg.transform.rotozoom(kk_img2, 90, 2.0),
    }
    #演習2:爆弾を加速させる
    accs = [a for a in range(1, 11)] # 加速を管理するリスト
    # 演習3:ゲームオーバーでこうかとんの画像を切り替える
    G_done = True # ゲームが続いているフラグ
    over_tmr = 3  # ゲームが終了した後のタイマー


    while True:
        txt = "0, 0"
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0
        tmr += 1
    
        # 爆弾移動処理
        bb_rct.move_ip(vx, vy)
        avx, avy = vx*accs[min(tmr//500, 9)], vy*accs[min(tmr//500, 9)]
        print(accs[min(tmr//500, 9)])
        bb_rct.move_ip(avx, avy)
        if not check_bound(bb_rct, scr_rct)[0]:
            vx *= -1
        if not check_bound(bb_rct, scr_rct)[1]:
            vy *= -1

        # こうかとん移動処理
        key_lst = pg.key.get_pressed()
        tup_lst = [] # タプルを保存するリスト
        for key, tup in key_dct.items():
            if key_lst[key]:
                kk_rct.move_ip(tup)
                tup_lst.append(tup)
                if check_bound(kk_rct, scr_rct) != (True, True):
                    kk_rct.centerx -= tup[0]
                    kk_rct.centery -= tup[1]
                    
        # 移動している方向を確認する
        t_x = 0
        t_y = 0
        for t in tup_lst:
            t_x += t[0]
            t_y += t[1]
        kk_img = delta[(t_x, t_y)]


        #　描画処理
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct)
        screen.blit(bb_img, bb_rct) # 爆弾を描画する

        # 練習5:衝突処理
        if kk_rct.colliderect(bb_rct):
            return
        pg.display.update()
        clock.tick(1000)
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()