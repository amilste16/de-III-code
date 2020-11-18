import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

print("Make it green!")

while True:
     dot.fill((0,255,0))