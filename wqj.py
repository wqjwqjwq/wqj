import streamlit as st
import requests
from io import BytesIO
from PIL import Image

# 1. 页面基础配置（设置标题、布局，默认居中）
st.set_page_config(
    page_title="Streamlit 网络相册（带图注）",
    layout="centered",  # 页面整体居中布局
    initial_sidebar_state="collapsed"  # 隐藏侧边栏，更整洁
)

# 2. 标题居中美化
st.markdown("<h1 style='text-align: center; color: #2E86AB;'>📷 网络图片相册</h1>", unsafe_allow_html=True)
st.divider()

# 3. 图片配置：包含网络图片链接和对应的专属图注（一一对应）
PHOTO_CONFIG = [
    {
        "url": "https://picsum.photos/800/500?random=1",
        "caption": "静谧的山间湖泊，清晨的薄雾笼罩着湖面，宛如人间仙境"
    },
    {
        "url": "https://picsum.photos/800/500?random=2",
        "caption": "城市天际线全景，高楼林立间藏着都市的繁华与烟火气"
    },
    {
        "url": "https://picsum.photos/800/500?random=3",
        "caption": "秋日森林小径，金黄的落叶铺满路面，尽显秋意浓情"
    },
    {
        "url": "https://picsum.photos/800/500?random=4",
        "caption": "海边日落美景，橘红色的晚霞映红海面，治愈又浪漫"
    },
    {
        "url": "https://picsum.photos/800/500?random=5",
        "caption": "雪山之巅风光，洁白的积雪与湛蓝的天空相映成趣"
    }
]

# 提取图片链接列表（用于索引匹配）
PHOTO_URLS = [item["url"] for item in PHOTO_CONFIG]
# 提取图片图注列表（与图片一一对应）
PHOTO_CAPTIONS = [item["caption"] for item in PHOTO_CONFIG]

# 4. 初始化会话状态（保存当前图片索引，持久化状态）
if "current_index" not in st.session_state:
    st.session_state.current_index = 0

def load_image_from_url(url):
    """从网络URL加载图片，返回PIL图片对象（增加请求头，提高兼容性）"""
    try:
        # 添加请求头，模拟浏览器访问，避免部分服务器拒绝
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # 抛出HTTP请求异常
        image_data = BytesIO(response.content)
        
        # 验证并打开图片
        img = Image.open(image_data)
        # 重置文件指针（避免后续读取失败）
        image_data.seek(0)
        return img
    except Exception as e:
        st.error(f"图片加载失败：{str(e)}")
        return None

# 5. 按钮布局（三列布局，实现左右按钮、中间信息居中）
col1, col2, col3 = st.columns([1, 2, 1], gap="medium")
current_idx = st.session_state.current_index

# 上一张按钮
with col1:
    if st.button("⬅️ 上一张", use_container_width=True, type="secondary"):
        if current_idx > 0:
            st.session_state.current_index -= 1
        else:
            st.warning("⚠️ 已经是第一张图片啦！")

# 当前图片信息（居中显示）
with col2:
    st.markdown(
        f"<p style='text-align: center; font-size: 18px; color: #4A4A4A;'>当前：第 {current_idx + 1} / {len(PHOTO_URLS)} 张</p>",
        unsafe_allow_html=True
    )

# 下一张按钮
with col3:
    if st.button("下一张 ➡️", use_container_width=True, type="secondary"):
        if current_idx < len(PHOTO_URLS) - 1:
            st.session_state.current_index += 1
        else:
            st.warning("⚠️ 已经是最后一张图片啦！")

# 6. 图片显示区域（居中+自定义大小+专属图注）
st.divider()
img = load_image_from_url(PHOTO_URLS[current_idx])
current_caption = PHOTO_CAPTIONS[current_idx]  # 获取当前图片对应的图注

# 图片容器（居中布局）
image_container = st.container()
with image_container:
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    if img:
        # 调整图片大小：width设置为800（可自定义），实现固定大小+居中
        st.image(
            img,
            width=800,  # 替换弃用的use_column_width，控制图片宽度
            # 图注组合：包含图片序号、尺寸和自定义描述
            caption=f"图片 {current_idx + 1} | 尺寸：{img.size[0]}x{img.size[1]} | 描述：{current_caption}",
            use_container_width=False  # 关闭容器宽度自适应，使用自定义width
        )
        # 单独放大显示图注（可选，提升可读性）
        st.markdown(
            f"<p style='text-align: center; font-size: 16px; color: #2E86AB; font-weight: 500;'>图注：{current_caption}</p>",
            unsafe_allow_html=True
        )
    else:
        # 图片加载失败时，显示占位提示+默认图注
        st.image(
            "https://picsum.photos/800/500?random=0",  # 占位图片
            width=800,
            caption=f"图片 {current_idx + 1} | 占位图 | 描述：图片加载失败，无法显示原图注",
            use_container_width=False
        )
        st.markdown(
            "<p style='text-align: center; font-size: 16px; color: #E74C3C; font-weight: 500;'>图注：图片加载失败</p>",
            unsafe_allow_html=True
        )
    st.markdown("</div>", unsafe_allow_html=True)
