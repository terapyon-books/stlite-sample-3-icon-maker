import streamlit as st
from make_icon import make_icon


st.title("アイコンを生成")
st.text("アイコン画像の確認をし、ダウンロードできます。")
st.text("バックグランドの色を決め、アイコンを探し、メインのイメージをアップロードします")
st.link_button("アイコンを検索するサイトに移動", url="https://fontawesome.com/search")

base_color = st.color_picker("バックグラウンドの色を選択", "#f0f0f0")
icon_file = st.file_uploader("アイコンをアップロード", type=["svg", "png", "jpg", "jpeg"])
key_image = st.file_uploader("キー画像をアップロード", type=["png", "jpg", "jpeg"])

if base_color and icon_file and key_image:
    st.write(f"選択したバックグラウンドの色: {base_color}")
    st.write(f"選択したアイコンフォント: {icon_file.name}")
    st.write(f"選択したキー画像: {key_image.name}")

    if st.button("アイコン生成"):
        # ここにアイコン生成の処理を記述
        img_value = make_icon(base_color, icon_file, key_image)
        st.image(img_value, caption="生成したアイコン", use_column_width=True)
        st.write("アイコン生成が完了しました。")
        st.write("ダウンロードボタンを押して、アイコンをダウンロードしてください。")
        if img_value:
            st.download_button(
                "アイコンをダウンロード",
                data=img_value,
                file_name="icon.png",
                mime="image/png",
            )
