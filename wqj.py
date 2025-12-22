import streamlit as st
import pandas as pd

# --------------------------
# 自定义CSS：扩大页面宽度，确保信息完整显示
# --------------------------
st.markdown("""
<style>
/* 扩大页面主容器宽度，取消最大宽度限制 */
.main .block-container {
    max-width: 95% !important;  /* 占浏览器宽度95%，足够展示完整信息 */
    width: 95% !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
}
/* 优化图表图例样式，避免公园名称换行截断 */
.stChart svg g.legend {
    font-size: 14px !important;  /* 适当放大图例字体，不挤压 */
    gap: 10px !important;  /* 增图例间距，避免重叠 */
}
/* 优化数据表格样式，确保列宽足够 */
.dataframe {
    width: 100% !important;
    table-layout: auto !important;  /* 自动适配列宽 */
}
.dataframe th, .dataframe td {
    white-space: nowrap !important;  /* 禁止文字换行 */
    padding: 8px 12px !important;  /* 增加单元格内边距 */
}
</style>
""", unsafe_allow_html=True)

# --------------------------
# 页面配置（居中布局+扩大宽度）
# --------------------------
st.set_page_config(
    page_title="南宁公园数据仪表盘",
    page_icon="🌳",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --------------------------
# 构造数据（数字月份根治排序）
# --------------------------
month_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
month_names = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]
month_num_to_name = dict(zip(month_nums, month_names))

park_info = pd.DataFrame({
    "公园名称": [
        "青秀山风景区",
        "南湖公园",
        "南宁市人民公园",
        "狮山公园",
        "石门森林公园",
        "良凤江国家森林公园"
    ],
    "地址": [
        "青秀区凤岭南路6号",
        "青秀区双拥路1号",
        "兴宁区人民东路1号",
        "兴宁区邕武路4号",
        "青秀区民族大道118号",
        "江南区友谊路78号"
    ],
    "占地面积(公顷)": [437.6, 191.9, 50.1, 80.2, 160.0, 486.7],
    "年游客量(万人次)": [650, 820, 480, 320, 390, 210],
    "游客评分(5分制)": [4.8, 4.7, 4.6, 4.5, 4.4, 4.3],
    "纬度": [22.8167, 22.8469, 22.8728, 22.8958, 22.8397, 22.6522],
    "经度": [108.3572, 108.3267, 108.3225, 108.3017, 108.3508, 108.3689]
})

price_data = pd.DataFrame({
    "月份数字": month_nums,
    "青秀山风景区": [30, 30, 20, 20, 30, 20, 20, 20, 20, 30, 20, 20],
    "南湖公园": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
    "南宁市人民公园": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
    "狮山公园": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
    "石门森林公园": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
    "良凤江国家森林公园": [20, 20, 15, 15, 20, 15, 15, 15, 15, 20, 15, 15]
})
price_data["月份"] = price_data["月份数字"].map(month_num_to_name)

monthly_visitor_data = pd.DataFrame({
    "月份数字": month_nums,
    "青秀山风景区": [55, 78, 52, 45, 60, 48, 42, 40, 38, 85, 50, 45],
    "南湖公园": [68, 85, 72, 65, 75, 62, 58, 55, 60, 90, 70, 65],
    "南宁市人民公园": [40, 55, 42, 38, 45, 35, 32, 30, 28, 60, 42, 38],
    "狮山公园": [28, 35, 30, 25, 32, 26, 24, 22, 20, 40, 28, 25],
    "石门森林公园": [32, 40, 35, 30, 38, 32, 29, 27, 25, 45, 35, 30],
    "良凤江国家森林公园": [18, 25, 20, 16, 22, 18, 15, 14, 12, 30, 19, 16]
})
monthly_visitor_data["月份"] = monthly_visitor_data["月份数字"].map(month_num_to_name)

# --------------------------
# 侧边栏
# --------------------------
with st.sidebar:
    st.header("🌳 选择公园")
    selected_parks = st.multiselect(
        "勾选要查看的公园",
        options=park_info["公园名称"].unique(),
        default=park_info["公园名称"].unique()
    )

filtered_price_data = price_data[["月份数字", "月份"] + selected_parks]
filtered_monthly_visitor = monthly_visitor_data[["月份数字", "月份"] + selected_parks]
filtered_park_info = park_info[park_info["公园名称"].isin(selected_parks)]

# --------------------------
# 主页面（完整显示所有信息）
# --------------------------
st.markdown("<h1 style='text-align: center; color: #2E8B57;'>🌳 南宁公园数据可视化仪表盘</h1>", unsafe_allow_html=True)
st.divider()

# 1. 公园基础信息
st.markdown("<h3 style='text-align: center;'>一、公园基础信息</h3>", unsafe_allow_html=True)
st.dataframe(
    filtered_park_info.drop(["纬度", "经度"], axis=1),
    use_container_width=True,
    hide_index=True,
    height=200
)

st.divider()

# 2. 价格走势折线图（完整显示图例）
st.markdown("<h3 style='text-align: center;'>二、12个月门票价格走势</h3>", unsafe_allow_html=True)
st.caption("注：x轴1-12对应1月-12月；红色=青秀山（收费），橙色=良凤江（收费），浅色=免费公园", help="鼠标悬停可查看具体价格")

color_map = {
    "青秀山风景区": "#E53E3E",
    "良凤江国家森林公园": "#DD6B20",
    "南湖公园": "#38A16980",
    "南宁市人民公园": "#3182CE80",
    "狮山公园": "#805AD580",
    "石门森林公园": "#D69E2E80"
}
chart_colors = [color_map[park] for park in selected_parks]

st.line_chart(
    data=filtered_price_data,
    x="月份数字",
    y=selected_parks,
    color=chart_colors,
    y_label="门票价格（元）",
    height=400,
    use_container_width=True
)
st.markdown("<p style='text-align: center;'>x轴：1=1月，2=2月，...，12=12月</p>", unsafe_allow_html=True)

st.divider()

# 3. 游客量图表（完整显示）
col1, col2 = st.columns([1, 1], gap="small")

with col1:
    st.markdown("<h3 style='text-align: center;'>三、年游客量对比</h3>", unsafe_allow_html=True)
    st.bar_chart(
        data=filtered_park_info.set_index("公园名称")["年游客量(万人次)"],
        color="#2E8B57",
        y_label="年游客量（万人次）",
        height=350,
        use_container_width=True
    )

with col2:
    st.markdown("<h3 style='text-align: center;'>四、月度游客量趋势</h3>", unsafe_allow_html=True)
    st.area_chart(
        data=filtered_monthly_visitor,
        x="月份数字",
        y=selected_parks,
        color=chart_colors,
        y_label="月度游客量（万人次）",
        height=350,
        use_container_width=True
    )

st.divider()

# 4. 公园位置
st.markdown("<h3 style='text-align: center;'>五、公园位置分布</h3>", unsafe_allow_html=True)
st.map(
    filtered_park_info,
    latitude="纬度",
    longitude="经度",
    zoom=11
)

st.markdown("<h3 style='text-align: center;'>📌 公园地址详情</h3>", unsafe_allow_html=True)
st.dataframe(
    filtered_park_info[["公园名称", "地址"]].set_index("公园名称"),
    use_container_width=True,
    height=150
)

st.markdown("<hr><p style='text-align: center; color: #666;'>© 2025 南宁公园数据可视化平台</p>", unsafe_allow_html=True)
