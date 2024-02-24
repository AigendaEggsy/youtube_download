import streamlit as st
from youtube_downloader import YouTubeDownloader
import os
import tempfile

st.set_page_config(
    page_title="YouTube Video Downloader",
    page_icon="📺",
)

st.markdown(
    """
    # YouTube Video Downloader
    ### Made by Eggsy
    ---
    """
)

url = st.text_input('YouTube video URL을 입력해주세요.', value="", placeholder="예: https://www.youtube.com/watch?v=dQw4w9WgXcQ")

if 'download_path' not in st.session_state:
    st.session_state.download_path = None

if url:
    # st.video(url)
    if st.session_state.download_path is None:
        with st.spinner('다운로드 준비중...'):
            downloader = YouTubeDownloader()
            try:
                temp_dir = tempfile.mkdtemp()
                downloader.download_path = os.path.join(temp_dir, '%(title)s.%(ext)s')
                filename = downloader.download_video(url)
                st.session_state.download_path = filename
                st.success('다운로드 준비 완료!')
            except Exception as e:
                st.error(f'비디오 다운로드 오류: {e}')


if st.session_state.download_path:
    st.markdown(
        """
        ---
        """
    )
    video_title = st.text_input('저장할 이름을 입력하세요', value="", placeholder=filename.split('/')[-1])
    if video_title:
        download_file_name = video_title + ".mp4"
    else:
        download_file_name = os.path.basename(st.session_state.download_path)
    with open(st.session_state.download_path, "rb") as file:
        st.download_button(
            label="비디오 다운로드",
            data=file,
            file_name=download_file_name,
            mime="video/mp4"
        )

    os.remove(st.session_state.download_path)
    st.session_state.download_path = None
