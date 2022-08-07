#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/08/09
# @Author  : github.com/guofei9987


class View(object):
    def __init__(self):
        self.svg_context = None

    def get_svg_context(self):
        return self.svg_context

    def save_svg(self, filename):
        with open(filename, 'w') as f:
            f.write(self.svg_context)


class Text(View):
    def __init__(self, width, height, color, data):
        super().__init__()
        tmp = ''
        num_lines = 0
        for idx, line in enumerate(data.split('\n')):
            tmp += f'<text y="{24 * idx + 20}" fill="red">{line}</text>\n'
            num_lines += 1

        height = height or (24 * num_lines + 5)
        self.svg_context = f'''<svg width="{width}px" height="{height}px" xmlns="http://www.w3.org/2000/svg" fill="{color}">
{tmp}</svg>'''


class Bar(View):
    def __init__(self, width, height, color, data):
        super().__init__()
        num_data = len(data)

        h_scale = (width // num_data // 3) // 3 * 3
        # if height is None, try to make h_scale*2 == v_scale
        height = height or (h_scale * 2 + 1) * max(data)
        v_scale = height // max(data) - 1

        path = f'M0 {height}'

        for idx, val in enumerate(data):
            path += f'''
v -{v_scale * val}
h {2 * h_scale} 
v {v_scale * val}
h {1 * h_scale}'''

        self.svg_context = f'''<svg width="{width}px" height="{height}px" xmlns="http://www.w3.org/2000/svg" fill="{color}">
<path d="{path}"/>
</svg>'''
