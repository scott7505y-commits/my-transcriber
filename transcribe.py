import streamlit as st
import whisper
import os

# 1. サイトのタイトル
st.title("動画文字起こしサイト")

# 2. 説明文（ここが下に表示されます）
st.markdown("""
### 使い方
このサイトは、動画から自動で文字を起こすツールです。
1. **動画をアップロード**してください（mp4形式）。
2. **「文字起こし開始」ボタン**を押すと処理が始まります。
3. 結果をコピーして、DeepL等で翻訳してください！
""")

# 3. 綺麗な線
st.divider()

# 4. アップロード機能
uploaded_file = st.file_uploader("動画ファイルを選択してください", type=["mp4"])

if uploaded_file is not None:
    # 処理ボタンを設置
    if st.button("文字起こし開始"):
        with open("temp_video.mp4", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        st.write("文字起こし中...（少し時間がかかります）")
        
        model = whisper.load_model("base")
        result = model.transcribe("temp_video.mp4")
        
        st.text_area("文字起こし結果", result["text"], height=300)
        st.download_button("テキストをダウンロード", result["text"], "result.txt")