import streamlit as st

# 设置页面标题
st.set_page_config(page_title="视频中心")

# 视频列表
video_arr = [
    {
        'url':'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/01/84/153468401/153468401_nb3-1-16.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&uipk=5&oi=1939826609&gen=playurlv3&os=bcache&og=cos&deadline=1766568458&platform=html5&nbs=1&trid=000011f7dee85e0e4500b50a469aa245b7cp&mid=0&upsig=28823198b82cdcfaaa99c68d7384ef73&uparams=e,uipk,oi,gen,os,og,deadline,platform,nbs,trid,mid&cdnid=6590&bvc=vod&nettype=0&bw=203166&dl=0&f=p_0_0&qn_dyeid=&agrr=1&buvid=&build=0&orderid=0,1',
        'title':'喜羊羊与灰太狼-第1集'
    },
    {
        'url':'http://upos-sz-mirrorcos.bilivideo.com/upgcxcode/22/49/34889204922/34889204922-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&mid=0&oi=144233936&deadline=1766569302&nbs=1&uipk=5&gen=playurlv3&platform=html5&os=08hbv&og=hw&trid=4c8f7fd2de1748d380ea94fc7b04b27O&upsig=ead28cac9166011725b1c8a204be65a0&uparams=e,mid,oi,deadline,nbs,uipk,gen,platform,os,og,trid&bvc=vod&nettype=1&bw=568430&agrr=1&buvid=&build=7330300&dl=0&f=O_0_0&orderid=0,3',
        'title':'喜羊羊与灰太狼-第2集'
    },
    {
        'url':'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/59/03/34761540359/34761540359-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&mid=0&gen=playurlv3&os=estgcos&og=cos&nbs=1&platform=html5&oi=2067284620&deadline=1766569368&uipk=5&trid=35e4d536387444449872dde85727dc6h&upsig=fe0c1ba3dfc102e3c16f0eaff5e53272&uparams=e,mid,gen,os,og,nbs,platform,oi,deadline,uipk,trid&bvc=vod&nettype=0&bw=679039&agrr=1&buvid=&build=0&dl=0&f=h_0_0&orderid=0,1',
        'title':'喜羊羊与灰太狼-第3集'
    }
]

# 初始化当前剧集索引
if 'ind' not in st.session_state:
    st.session_state.ind = 0

# 动态显示当前剧集标题
st.title(video_arr[st.session_state.ind]['title'])

# 播放当前视频
st.video(video_arr[st.session_state.ind]['url'])

# 定义切换函数
def playVideo(index):
    st.session_state.ind = index

# 创建横向按钮：使用 columns
cols = st.columns(len(video_arr))  # 创建与视频数量相同的列

for i, col in enumerate(cols):
    with col:
        st.button(
            f"第{i+1}集",
            key=f"btn_{i}",
            on_click=playVideo,
            args=(i,),
            use_container_width=True  # 让按钮填满列宽，更美观
        )
