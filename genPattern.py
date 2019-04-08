#!/usr/bin/env python3

from PIL import Image, ImageDraw
import argparse

def draw_pattern(im, beg_width, beg_height, start_coordinate, change,
                 number_of_blocks, color_sequence):
    draw_im = ImageDraw.Draw(im)
    bottom = start_coordinate[1]
    top = bottom - beg_height
    right = start_coordinate[0]
    left = right - beg_width
    color_i = 0
    total_colors = len(color_sequence)

    for i in range(number_of_blocks):
        points = []
        points.append((right, bottom))
        right += change
        points.append((left, bottom))
        bottom -= change
        points.append((left, top))
        left -= change
        points.append((right, top))
        top += change
        points.append((right, bottom))
        draw_im.line(points, color_sequence[color_i], 4, 'curve')
        color_i = (color_i + 1) % total_colors

    return im

def main():
    default_xd = 900
    default_yd = 800
    default_totBlocks = 38
    default_change = 10
    default_midW = 30
    default_midH = default_yd - 2*default_change
    parser = argparse.ArgumentParser()
    parser.add_argument('-bg', '--bgcolor', default='black',
                        help='select the background color of the image')
    parser.add_argument('-pc', '--pattern_color', default='cyan',
                        help='set the color of the pattern')
    parser.add_argument('-xd', '--xdimension', type=int, default=default_xd,
                        help='set the x dimenstion of the image')
    parser.add_argument('-yd', '--ydimension', type=int, default=default_yd,
                        help='set y dimension of the image')
    parser.add_argument('-nb', '--total_blocks', type=int, default=default_totBlocks,
                        help='set total no. of blocks to generate')
    parser.add_argument('-c', '--change', type=int, default=default_change,
                        help='set the increment to be made in the pattern')
    parser.add_argument('-mw', '--middle_width', type=int, default=default_midW,
                        help='set the width of the middle most rectangle in the pattern')
    parser.add_argument('-mh', '--middle_height', type=int, default=default_midH,
                        help='set the height of the middle most rectangle in the pattern')
    parser.add_argument('-o', '--outfile', default='pattern',
                        help='set the filename of the ouput file')
    args = parser.parse_args()
    
    image = Image.new('RGB', (args.xdimension, args.ydimension), args.bgcolor)
    image = draw_pattern(image, args.middle_width, args.ydimension - 2*args.change,
                         (args.xdimension/2 + args.middle_width/2, 
                          args.ydimension - args.change),
                         args.change, args.total_blocks, [args.pattern_color])
    image.save(args.outfile + '.png')

if __name__ == '__main__':
    main()
