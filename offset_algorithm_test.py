# offset_algorithm_test.py - 3D打印薄壁零件轮廓偏置算法测试
import numpy as np

def contour_offset(contour, offset_distance):
    """
    轮廓偏置算法基础函数
    :param contour: 输入轮廓坐标列表，格式[(x1,y1), (x2,y2), ...]
    :param offset_distance: 偏置距离（mm）
    :return: 偏置后的轮廓
    """
    offset_contour = []
    for (x, y) in contour:
        # 简单偏置逻辑（后续优化）
        offset_x = x + offset_distance
        offset_y = y + offset_distance
        offset_contour.append((offset_x, offset_y))
    return offset_contour

# 测试用例
if __name__ == "__main__":
    thin_wall_contour = [(0,0), (0,0.8), (10,0.8), (10,0)]
    offset_contour = contour_offset(thin_wall_contour, 0.4)
    print("原始轮廓：", thin_wall_contour)
    print("偏置后轮廓：", offset_contour)
