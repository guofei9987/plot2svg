# plot2svg

I was using some other tools to plot and save to `.SVG` file, And I found the files are too big.  
So I make this package myself to generate SVG graphs with small file size.  

For example, this package plot a bar which is **0.6 KB**, compared to other tools plot the same bar which is **40 KB**


## install

`pip install plot2svg`

## usage

plot a bar
```python
from plot2svg import Bar

data = list(range(25))

view = Bar(width=500, height=300, color="red", data=data)
svg_context = view.get_svg_context()
print(svg_context)
view.save_svg('data_bar.svg')
```

![](/examples/data_bar.svg)

plot texts

```python
from plot2svg import Text

text = '''test
测试
换行
plot2svg is light'''

view = Text(width=500, height=300, color="red", data=text)
svg_context = view.get_svg_context()
print(svg_context)
view.save_svg('data_text.svg')
```

![](/examples/data_text.svg)
