import streamlit as st
import whisper
import os

st.title("動画文字起こしサイト")

uploaded_file = st.file_uploader("動画ファイルを選択してください", type=["mp4"])

if uploaded_file is not None:
    # ファイルを保存するパスを定義
    save_path = "temp_video.mp4"
    
    if st.button("文字起こし開始"):
        # 一旦、前のファイルを消す
        if os.path.exists(save_path):
            os.remove(save_path)
            
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.write("文字起こし中...")
        
        try:
            model = whisper.load_model("base")
            result = model.transcribe(save_path)
            
            st.text_area("結果", result["text"])
            st.markdown("---")
            st.markdown("[DeepL 翻訳はこちら](https://www.deepl.com/translator)")
            
        except Exception as e:
            st.error(f"エラー内容: {e}")
