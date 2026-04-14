import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #練習1
    bg_img2 = pg.transform.flip(bg_img, True, False) #練習8
    kb_img = pg.image.load("fig/3.png") #練習3
    kb_img = pg.transform.flip(kb_img, True, False) 
    kb_rct =kb_img.get_rect() #練習10:こうかとんRectの取得
    kb_rct.center = 300, 200 #練習11:こうかとんRectの中心座標の設定
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed() #練習10:すべてのキーの押下状態の取得
        if key_lst[pg.K_UP]: #練習10:上矢印キーが押されていたら
            kb_rct.move_ip(0, -1) #こうかとんを上に移動
        if key_lst[pg.K_DOWN]: #練習10:下矢印キーが押されていたら
            kb_rct.move_ip(0, +1) #こうかとんを下に移動
        if key_lst[pg.K_LEFT]: #練習10:左矢印キーが押されていたら
            kb_rct.move_ip(-1, 0) #こうかとんを左に移動 
        if key_lst[pg.K_RIGHT]: #練習10:右矢印キーが押されていたら
            kb_rct.move_ip(+1, 0) #こうかとんを右に移動
        x = tmr%3200 #練習5
        screen.blit(bg_img, [-x, 0]) #練習2
        screen.blit(bg_img2, [-x+1600, 0]) #練習7
        screen.blit(bg_img, [-x+3200, 0]) #練習9
        screen.blit(kb_img, kb_rct) #練習4
        pg.display.update()
        tmr += 1        
        clock.tick(200) #練習6


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()