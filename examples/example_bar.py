from plot2svg import Bar

data = list(range(25))

view = Bar(width=500, height=300, color="red", data=data)
svg_context = view.get_svg_context()
print(svg_context)
view.save_svg('data_bar.svg')
