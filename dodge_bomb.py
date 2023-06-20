import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900
delta = {
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, +5),
    pg.K_LEFT: (-5, 0),
    pg.K_RIGHT: (+5, 0),
}


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    # こうかとんSurface（kk_img）からこうかとんRect（kk_rct）を抽出する
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900, 400
    bb_img = pg.Surface((20, 20))  # 練習１
    bb_img.set_colorkey((0, 0, 0))  # 黒い部分を透明にする
    pg.draw.circle(bb_img, (255, 0, 0), (10, 10), 10)
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    # 爆弾Surface（bd_img）から爆弾Rect（bd_rct）を抽出する
    bd_rct = bb_img.get_rect()
    # 爆弾Rectの中心座標を乱数で指定する
    bd_rct.center = x, y 
    vx, vy = +5, +5  # 練習２
    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]  # 合計移動量
        for k, mv in delta.items():
            if key_lst[k]: 
                sum_mv[0] += mv[0]
                sum_mv[1] += mv[1]
        kk_rct.move_ip(sum_mv)

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct)
        screen.blit(bb_img, bd_rct)
        pg.display.update()
        tmr += 1
        clock.tick(50)
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()