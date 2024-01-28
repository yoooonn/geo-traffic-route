import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString
from matplotlib import rcParams

from geo_traffic_route import processed_airports_data

# from geo_traffic_route.route import iata_code_2_airports

rcParams['font.family'] = 'Noto Sans Mono CJK SC'  # 指定默认字体
rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def draw_route_vector(airports_geo: dict):
    # 经纬度坐标列表
    # coordinates = [
    #     (116.403847, 39.915526),  # 北京天安门
    #     (121.473701, 31.230416),  # 上海外滩
    #     (117.200983, 39.084158)  # 天津古文化街
    # ]

    # 创建Point对象列表
    points = [Point(v) for k, v in airports_geo.items()]

    airports = [k for k, v in airports_geo.items()]

    # 创建GeoDataFrame
    gdf_points = gpd.GeoDataFrame(geometry=points)

    # 创建LineString对象连接所有点
    line = LineString(points)

    # 将LineString对象转换为GeoDataFrame
    gdf_line = gpd.GeoDataFrame(geometry=[line])

    # 绘制线
    ax = gdf_line.plot(ax=plt.gca(), linewidth=2, color='black')

    # 绘制点
    gdf_points.plot(ax=ax, marker='o', color='red', markersize=50)

    # 在每个点上添加序号，序号从1开始
    for idx, point in enumerate(gdf_points.geometry):
        plt.text(point.x, point.y, airports[idx], fontsize=12, ha='right')

    # 添加箭头以显示方向
    # 箭头的样式可以自定义
    arrow_style = '->'

    # 缩小箭头的大小
    arrow_size = 15

    num_coords = len(line.coords)
    for i in range(num_coords - 1):
        # 获取连线的起点和终点
        x0, y0 = line.coords[i]
        x1, y1 = line.coords[i + 1]
        # 计算箭头的位置（在起点和终点之间）
        arrow_x = x0 + (x1 - x0) * 0.5
        arrow_y = y0 + (y1 - y0) * 0.5
        # 添加箭头注释
        ax.annotate('',
                    xytext=(x0, y0),
                    xy=(arrow_x, arrow_y),
                    arrowprops=dict(arrowstyle=arrow_style, shrinkA=arrow_size, shrinkB=arrow_size, color='blue'))

    plt.axis('off')
    ax.axis('off')
    # 显示图形
    plt.show()


# coordinates = [
#     ,  # 北京天安门
#     ,  # 上海外滩
#       # 天津古文化街
# ]
# geos = {"北京天安门": (116.403847, 39.915526), "上海外滩": (121.473701, 31.230416),
#         "天津古文化街": (117.200983, 39.084158)}

iata_code_2_airports = processed_airports_data()

geos = {
    'URC': (iata_code_2_airports['URC']['longitude_deg'], iata_code_2_airports['URC']['latitude_deg']),
    'SIA': (iata_code_2_airports['SIA']['longitude_deg'], iata_code_2_airports['SIA']['latitude_deg']),
    'HKG': (iata_code_2_airports['HKG']['longitude_deg'], iata_code_2_airports['HKG']['latitude_deg']),
}

draw_route_vector(geos)
