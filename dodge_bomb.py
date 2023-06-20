import random
import sys
import pygame as pg



WIDTH, HEIGHT = 1600, 900


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    clock = pg.time.Clock()
    tmr = 0
    #練習1
    bb_img = pg.Surface((20, 20))  # ボムのサーフェイスを作成
    pg.draw.circle(bb_img, (255, 0, 0), (10, 10), 10)  # ボムを描画
    bb_img.set_colorkey((0, 0, 0)) #背景を透明
    x = random.randint(0,WIDTH)
    y = random.randint(0,HEIGHT) 
    bb_rct = bb_img.get_rect()
    bb_rct.center = x,y #爆弾rectの中心座標を乱数で指定する。
    # 練習2：爆弾をランダムに配置する
    scr_rct = screen.get_rect()  # 画面のrectをとる
    bb_rct.center = (random.randint(0, scr_rct.width), random.randint(0, scr_rct.height))
    bb_rct.center = (random.randint(0, scr_rct.width),random.randint(0, scr_rct.height))
    vx,vy = +5, -5

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        bb_rct.move_ip(vx, vy)
        screen.blit(bb_img,bb_rct)

    
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()