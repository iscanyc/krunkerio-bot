import pyautogui as sc

(width, height) = sc.size()


class Game:
    def __init__(self, rgb=[(234, 50, 50), (236, 87, 87)], detection=[140, 30], count=10):
        (self.width, self.height) = (width / 2, height / 2)
        self.count = count
        self.rgb = rgb
        self.detection = detection
        self.id = 0

    def start(self):
        img = sc.screenshot(region=(self.width - 30, self.height, self.detection[0], self.detection[1]))
        colors = img.getcolors()
        if colors:
            for color in colors:
                if self.rgb[0][0] < color[1][0] < self.rgb[1][0]:
                    if self.rgb[0][1] < color[1][1] < self.rgb[1][1]:
                        if self.rgb[0][2] < color[1][2] < self.rgb[1][2]:
                            self.shoot()
                            self.save(img)

    def shoot(self):
        print("hit")

    def save(self, img):
        img.save(self.id.__str__() + ".png")
        self.id = self.id + 1


game = Game()
while True:
    game.start()
