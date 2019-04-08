#!/usr/bin/env python3

from PIL import Image, ImageDraw
import argparse

def base(im, four_coor, change, width, color):
    draw_im = ImageDraw.Draw(im)
    points = [four_coor[1], 
              (four_coor[1][0], four_coor[3][1] + change), 
              (four_coor[0][0] + change, four_coor[3][1] + change),
              (four_coor[0][0] + change, four_coor[2][1]),
              four_coor[2]]
    draw_im.line(points, color, width, 'curve')
    return im

def draw_pattern(im, beg_width, beg_height, start_coordinate, change,
                 number_of_blocks, colors, line_width):
    draw_im = ImageDraw.Draw(im)
    #set initial btrl values
    bottom = start_coordinate[1]
    top = bottom - beg_height
    right = start_coordinate[0]
    left = right - beg_width
    #set up for color sequence traversal
    color_i = 0
    total_colors = len(colors)

    four_coor = [(left, bottom),
                 start_coordinate]

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
        draw_im.line(points, colors[color_i], line_width, 'curve')
        color_i = (color_i + 1) % total_colors

    four_coor += [(right, bottom),
                  (right, top - change)]
    return base(im, four_coor, change, line_width, colors[0])

def main():
    default_xd = 900
    default_yd = 800
    default_totBlocks = 38
    default_line_width = 4
    default_change = 10
    default_midW = 30
    default_midH = default_yd - 2*default_change
    parser = argparse.ArgumentParser()
    parser.add_argument('-bg', '--bgcolor', default='black',
                        help='select the background color of the image')
    parser.add_argument('-xd', '--xdimension', type=int, default=default_xd,
                        help='set the x dimenstion of the image')
    parser.add_argument('-yd', '--ydimension', type=int, default=default_yd,
                        help='set y dimension of the image')
    parser.add_argument('-pc', '--pattern_color', default=['cyan'], nargs='*',
                        help='set the color of the pattern')
    parser.add_argument('-lw', '--line_width', default = default_line_width,
                        type=int, help='set the width of the pattern line')
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
                         args.change, args.total_blocks, args.pattern_color, args.line_width)
    image.save(args.outfile + '.png')

if __name__ == '__main__':
    main()
