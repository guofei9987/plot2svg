from plot2svg import Text

text = '''test
测试
换行
plot2svg is light'''

view = Text(width=500, height=300, color="black", data=text)
svg_context = view.get_svg_context()
print(svg_context)
view.save_svg('data_text.svg')