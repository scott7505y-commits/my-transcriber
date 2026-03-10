import streamlit as st
import whisper
import os

st.title("動画文字起こしサイト")

st.markdown("""
### 使い方
動画をアップロードして「文字起こし開始」ボタンを押してください。
""")

uploaded_file = st.file_uploader("動画ファイルを選択してください", type=["mp4"])

if uploaded_file is not None:
    temp_file_path = os.path.join(os.getcwd(), "temp_video.mp4")
    
    if st.button("文字起こし開始"):
        with open(temp_file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.write("文字起こし中...（少し時間がかかります）")
        
        try:
            model = whisper.load_model("base")
            result = model.transcribe(temp_file_path)
            
            st.text_area("文字起こし結果", result["text"], height=300)
            
            # ここがDeepLリンクの追加部分です
            st.markdown("---")
            st.markdown("[DeepL 翻訳サイトはこちら](https://www.deepl.com/translator)")
            
            st.download_button("テキストをダウンロード", result["text"], "result.txt")
            
        except Exception as e:
            st.error(f"エラーが発生しました: {e}")
            
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)

