from plot2svg import Bar

data = list(range(15))

view = Bar(width=500, height=None, color="red", data=data)
svg_context = view.get_svg_context()
print(svg_context)
view.save_svg('data_bar.svg')
