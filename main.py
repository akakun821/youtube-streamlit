import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("Streamlit 超入門") #タイトルを表示

st.write("プログレスバーの表示") #追加記載
"Start!!"

latest_iteration = st.empty() #latest_iterationを空で用意
bar = st.progress(0) #プログレスバーを表示

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}") #latest_iterationの中にテキストを表示
    # f"文字列 {変数}" 文字列の中に数字を含める
    bar.progress(i+1)
    time.sleep(0.1) #毎回0.1秒ごと休んでからi+1に進む

"Done!!!" 

df=pd.DataFrame({
    "1列目":[1, 2, 3, 4],
    "2列目":[10, 20, 30, 40],
})

st.write(df) #dfを表示。ソートはできる。

st.dataframe(df,width=100,height=100) #st.dataframeでは幅、高さも変更可能。ソートもできる。

st.dataframe(df.style.highlight_max(axis=0)) #st.dataframeではハイライトもできる。

st.table(df) #st.tableでは、ソートはできない。

"""
# 章
## 節
### 項

```python #バッククォーテーションはShift+@　```python で```で囲まれた中はpythonコードと認識される
import streamlit as st
```
"""

df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=["a", "b", "c"]
)

st.line_chart(df) #折れ線グラフ

st.area_chart(df) #エリアグラフ

st.bar_chart(df) #棒グラフ

df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69,139.70],
    columns = ["lat", "lon"]
)

st.map(df)

st.write("Display Image")

img = Image.open("sample.jpg")
st.image(img, caption="sea", width="stretch")
#width="stretch" 画面幅いっぱいに表示
#caption 題名


if st.checkbox("Show Image"):
    img = Image.open("sample.jpg")
    st.image(img,caption = "sea",width ="stretch")

option = st.selectbox(
    "あなたが好きな数字を教えてください",
    list(range(1,11))
)
st.write ("あなたの好きな数字は" ,option, "です。") #st.writeを使わなくても書ける。
#st,write("文字列", a, "文字列")構文

text = st.text_input("あなたの趣味を教えてください。")
st.write("あなたの趣味：", text)

condition = st.slider("あなたの今の調子は？", 0, 100 ,50) #st.slider("文字列",max,min,デフォルト値)
st.write("コンディション：",condition)

st.write("Interractive Widgets")

#text = st.text_input("あなたの趣味を教えてください。")
#condition = st.slider("あなたの今の調子は？", 0, 100 ,50) 

#st.write("あなたの趣味：", text)
#st.write("コンディション：",condition)

left_column, right_column = st.columns(2) #もし、3分割したければ、col1, col2, col3 = st.columns(3)
button = left_column.button("ここは左カラム")
if button:
    right_column.write("ここは右カラム") #ボタンが押されたときだけ、右カラムに文字を表示

expander1 = st.expander("問い合わせ1")
expander1.write("回答1")
expander2 = st.expander("問い合わせ2")
expander2.write("回答2")
expander3 = st.expander("問い合わせ3")
expander3.write("回答3")
