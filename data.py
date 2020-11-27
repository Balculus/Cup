import math

import numpy as np
import pandas as pd
import xlrd

DATA_LOAD = 1
Longitude_Factor = 100000 # 经度系数
Latitude_Factor = 111332 # 纬度系数
nodes = [[1.0, 111.599628, 40.844048], [2.0, 111.604371, 40.836106], [3.0, 111.589998, 40.830211], [4.0, 111.595891, 40.818419], [5.0, 111.611126, 40.82497], [6.0, 111.622481, 40.842219], [7.0, 111.627799, 40.83174], [8.0, 111.616444, 40.851497], [9.0, 111.629236, 40.850951], [10.0, 
111.643034, 40.855863], [11.0, 111.641669, 40.860146], [12.0, 111.650005, 40.8405], [13.0, 111.650436, 40.862874], [14.0, 111.653742, 40.859055], [15.0, 111.655035, 40.854799], [16.0, 111.660928, 40.841373], [17.0, 111.659778, 40.866366], [18.0, 111.660713, 40.862929], [19.0, 111.662725, 40.856026], [20.0, 111.666318, 
40.849805], [21.0, 111.668761, 40.842274], [22.0, 111.671492, 40.870867], [23.0, 111.674654, 40.862028], [24.0, 111.675804, 40.858645], [25.0, 111.677385, 40.848059], [26.0, 111.678248, 40.843475], [27.0, 111.679972, 40.872394], [28.0, 111.682991, 40.86312], [29.0, 111.68414, 40.8593], [30.0, 111.687302, 40.849369], [31.0, 111.689027, 40.844566], [32.0, 111.701244, 40.846204], [33.0, 111.698657, 40.85177], [34.0, 111.69492, 40.861046], [35.0, 111.697507, 40.865411], [36.0, 111.700669, 40.871631], [37.0, 111.714755, 40.871085], [38.0, 111.713892, 40.867157], [39.0, 111.712311, 40.855481], [40.0, 111.712742, 40.843256], [41.0, 111.724241, 40.846094], [42.0, 111.720216, 40.85679], [43.0, 111.720648, 40.866721], [44.0, 111.720791, 40.869994], [45.0, 111.733727, 40.86432], [46.0, 111.735883, 40.859191], [47.0, 111.739476, 40.849478], [48.0, 111.737608, 40.86923], [49.0, 111.740051, 40.865957], [50.0, 111.742494, 40.86061], [51.0, 111.745081, 40.851006], [52.0, 111.747956, 40.844457], [53.0, 111.750399, 40.836816], [54.0, 111.741488, 40.843038], [55.0, 111.734158, 40.841073], [56.0, 111.736889, 40.83365], [57.0, 111.752124, 40.829174], [58.0, 111.752699, 40.824479], [59.0, 111.753849, 40.820439], [60.0, 111.754855, 40.815525], [61.0, 111.746662, 40.808317], [62.0, 111.744363, 40.813669], [63.0, 111.741632, 40.821968], [64.0, 111.739764, 40.826335], [65.0, 111.726828, 40.839873], [66.0, 111.729415, 40.832231], [67.0, 111.73229, 40.825025], [68.0, 111.734446, 40.820439], [69.0, 111.737176, 40.812467], [70.0, 111.739476, 40.807225], [71.0, 111.727547, 40.804932], [72.0, 111.725391, 
40.810174], [73.0, 111.72266, 40.817491], [74.0, 111.720827, 40.8222], [75.0, 111.717917, 40.829938], [76.0, 111.715186, 40.837143], [77.0, 111.703113, 40.841292], [78.0, 111.705987, 40.834851], [79.0, 111.70958, 40.827645], [80.0, 111.712311, 40.820657], [81.0, 111.714503, 40.815757], [82.0, 111.717629, 40.809082], [83.0, 111.719929, 40.80231], [84.0, 111.710874, 40.795757], [85.0, 111.705987, 40.807881], [86.0, 111.704119, 40.812686], [87.0, 111.701675, 40.817163], [88.0, 111.697938, 40.824697], [89.0, 111.695639, 40.832012], [90.0, 111.692477, 40.838126], [91.0, 111.680835, 40.834851], [92.0, 111.682991, 40.829283], [93.0, 111.683997, 40.827673], [94.0, 111.687015, 40.821558], [95.0, 111.690177, 40.814024], [96.0, 111.694058, 40.805942], [97.0, 111.700094, 40.792398], [98.0, 111.689315, 40.789011], [99.0, 111.686296, 40.803758], [100.0, 111.684428, 40.807908], [101.0, 111.682272, 40.81173], [102.0, 111.67911, 40.817955], [103.0, 111.676667, 40.821886], [104.0, 111.674367, 40.827345], [105.0, 111.672786, 40.832122], [106.0, 111.67178, 40.835724], [107.0, 111.660856, 40.835724], [108.0, 111.660856, 40.83103], [109.0, 111.661898, 40.82482], [110.0, 111.667648, 40.815102], [111.0, 111.671205, 40.808536], [112.0, 111.673361, 40.804713], [113.0, 111.675229, 40.800563], [114.0, 111.682559, 40.787454], [115.0, 111.669768, 40.784505], [116.0, 111.664162, 40.797395], [117.0, 111.662725, 40.801764], [118.0, 111.661862, 40.809191], [119.0, 111.661431, 40.813996], [120.0, 111.655395, 40.810174], [121.0, 111.652664, 40.800017], [122.0, 111.650077, 40.796303], [123.0, 111.647633, 40.800563], [124.0, 111.645046, 40.807662], [125.0, 111.638147, 40.817054], [126.0, 111.649789, 40.830156], [127.0, 111.648064, 40.833868], [128.0, 111.629523, 40.828846], [129.0, 111.633835, 40.823606], [130.0, 111.617738, 40.817163], [131.0, 111.598622, 40.810283], [132.0, 111.622912, 40.811157], [133.0, 111.611701, 40.806788], [134.0, 111.596322, 40.800563], [135.0, 111.595172, 40.795101], [136.0, 111.616875, 40.798597], [137.0, 111.629811, 40.800672], [138.0, 111.634267, 40.779697], [139.0, 111.594454, 40.774999], [140.0, 111.650077, 40.781664], [141.0, 111.643034, 40.788001]]

links = [[1.0, 2.0, 2.0], [1.0, 3.0, 4.0], [1.0, 8.0, 4.0], [2.0, 3.0, 6.0], [2.0, 6.0, 6.0], [2.0, 5.0, 2.0], [3.0, 4.0, 4.0], [4.0, 5.0, 2.0], [4.0, 131.0, 4.0], [5.0, 7.0, 2.0], [6.0, 8.0, 6.0], [6.0, 9.0, 6.0], [6.0, 7.0, 6.0], [7.0, 12.0, 2.0], [7.0, 128.0, 6.0], [8.0, 11.0, 4.0], [9.0, 10.0, 6.0], [10.0, 11.0, 2.0], [10.0, 14.0, 6.0], [10.0, 12.0, 2.0], [11.0, 13.0, 4.0], [12.0, 16.0, 2.0], [13.0, 17.0, 4.0], [13.0, 14.0, 8.0], [14.0, 15.0, 
8.0], [14.0, 18.0, 6.0], [15.0, 19.0, 2.0], [15.0, 16.0, 8.0], [16.0, 21.0, 2.0], [16.0, 107.0, 8.0], [17.0, 18.0, 2.0], [17.0, 22.0, 4.0], [18.0, 19.0, 2.0], [18.0, 23.0, 6.0], [19.0, 24.0, 2.0], [19.0, 20.0, 2.0], [20.0, 21.0, 2.0], [21.0, 26.0, 2.0], [21.0, 106.0, 2.0], [22.0, 27.0, 4.0], [23.0, 24.0, 2.0], [23.0, 28.0, 6.0], [24.0, 29.0, 2.0], [24.0, 25.0, 2.0], [25.0, 26.0, 2.0], [25.0, 30.0, 2.0], [26.0, 91.0, 2.0], [26.0, 31.0, 2.0], [27.0, 36.0, 4.0], [27.0, 28.0, 8.0], [28.0, 35.0, 6.0], [28.0, 29.0, 8.0], [29.0, 34.0, 2.0], [29.0, 30.0, 8.0], [30.0, 31.0, 8.0], [30.0, 33.0, 2.0], [31.0, 32.0, 2.0], [31.0, 90.0, 8.0], [32.0, 33.0, 2.0], [32.0, 77.0, 2.0], [33.0, 39.0, 2.0], [33.0, 34.0, 2.0], [34.0, 35.0, 2.0], [35.0, 36.0, 2.0], [35.0, 38.0, 6.0], [36.0, 37.0, 4.0], [37.0, 38.0, 
2.0], [37.0, 44.0, 4.0], [38.0, 43.0, 6.0], [38.0, 39.0, 2.0], [39.0, 42.0, 2.0], [40.0, 77.0, 2.0], [40.0, 76.0, 2.0], [40.0, 41.0, 2.0], [41.0, 47.0, 2.0], [41.0, 65.0, 6.0], [41.0, 42.0, 6.0], [42.0, 46.0, 2.0], [42.0, 43.0, 6.0], [43.0, 45.0, 6.0], [43.0, 44.0, 6.0], [44.0, 48.0, 4.0], [45.0, 49.0, 6.0], [45.0, 46.0, 2.0], [46.0, 50.0, 2.0], [46.0, 47.0, 2.0], [47.0, 51.0, 2.0], [47.0, 54.0, 2.0], [48.0, 49.0, 4.0], [49.0, 50.0, 4.0], [50.0, 51.0, 4.0], [51.0, 52.0, 4.0], [52.0, 53.0, 4.0], [52.0, 54.0, 8.0], [53.0, 57.0, 4.0], [53.0, 56.0, 2.0], [54.0, 55.0, 8.0], [55.0, 65.0, 8.0], [55.0, 56.0, 2.0], [56.0, 66.0, 2.0], [56.0, 
64.0, 2.0], [57.0, 58.0, 4.0], [57.0, 64.0, 2.0], [58.0, 63.0, 2.0], [58.0, 59.0, 4.0], [59.0, 60.0, 4.0], [60.0, 61.0, 4.0], [60.0, 62.0, 6.0], [61.0, 62.0, 2.0], [61.0, 70.0, 4.0], [62.0, 69.0, 6.0], [62.0, 63.0, 2.0], [63.0, 64.0, 2.0], [63.0, 68.0, 2.0], [64.0, 67.0, 2.0], [65.0, 66.0, 6.0], [65.0, 76.0, 8.0], [66.0, 75.0, 2.0], [66.0, 67.0, 6.0], [67.0, 74.0, 2.0], [67.0, 68.0, 6.0], [68.0, 73.0, 2.0], [68.0, 69.0, 6.0], [69.0, 70.0, 6.0], [69.0, 72.0, 6.0], [70.0, 71.0, 4.0], [71.0, 72.0, 2.0], [71.0, 83.0, 4.0], [72.0, 82.0, 6.0], [72.0, 73.0, 2.0], [73.0, 81.0, 2.0], [73.0, 74.0, 2.0], [74.0, 80.0, 2.0], [74.0, 75.0, 2.0], [75.0, 76.0, 2.0], [75.0, 79.0, 2.0], [76.0, 78.0, 8.0], [77.0, 90.0, 2.0], [77.0, 78.0, 2.0], [78.0, 89.0, 8.0], [78.0, 79.0, 2.0], [79.0, 88.0, 2.0], [79.0, 80.0, 2.0], [80.0, 81.0, 2.0], [80.0, 87.0, 2.0], [81.0, 82.0, 2.0], [81.0, 86.0, 2.0], [82.0, 85.0, 6.0], [82.0, 83.0, 2.0], [83.0, 84.0, 4.0], [84.0, 85.0, 8.0], [84.0, 97.0, 4.0], [85.0, 86.0, 8.0], [85.0, 96.0, 6.0], [86.0, 87.0, 8.0], [87.0, 95.0, 2.0], [87.0, 88.0, 8.0], [88.0, 94.0, 2.0], [88.0, 89.0, 8.0], [89.0, 90.0, 8.0], [89.0, 92.0, 8.0], [90.0, 91.0, 2.0], [91.0, 92.0, 2.0], [91.0, 106.0, 2.0], [92.0, 93.0, 2.0], [92.0, 104.0, 8.0], [93.0, 94.0, 2.0], [93.0, 103.0, 2.0], [94.0, 95.0, 2.0], [95.0, 101.0, 2.0], [95.0, 96.0, 2.0], [96.0, 97.0, 2.0], [96.0, 99.0, 6.0], [97.0, 98.0, 4.0], [98.0, 99.0, 2.0], [98.0, 114.0, 4.0], [99.0, 100.0, 2.0], [99.0, 113.0, 6.0], [100.0, 101.0, 2.0], [100.0, 112.0, 2.0], [101.0, 111.0, 2.0], [101.0, 102.0, 2.0], [102.0, 103.0, 2.0], [103.0, 104.0, 2.0], [103.0, 110.0, 2.0], [104.0, 105.0, 2.0], [104.0, 109.0, 8.0], [105.0, 108.0, 2.0], [105.0, 106.0, 2.0], [106.0, 107.0, 2.0], [107.0, 108.0, 8.0], [107.0, 127.0, 2.0], [108.0, 126.0, 2.0], [108.0, 109.0, 8.0], [109.0, 119.0, 8.0], [109.0, 125.0, 8.0], [110.0, 119.0, 2.0], [110.0, 111.0, 2.0], [111.0, 112.0, 2.0], [111.0, 118.0, 2.0], [112.0, 113.0, 2.0], [112.0, 117.0, 2.0], [113.0, 116.0, 6.0], [113.0, 114.0, 2.0], [114.0, 115.0, 4.0], [115.0, 116.0, 8.0], [115.0, 140.0, 4.0], [116.0, 117.0, 8.0], [116.0, 121.0, 6.0], [117.0, 118.0, 8.0], [118.0, 119.0, 8.0], [118.0, 120.0, 2.0], [119.0, 120.0, 2.0], [120.0, 121.0, 2.0], [120.0, 124.0, 2.0], [121.0, 122.0, 2.0], [121.0, 123.0, 6.0], [122.0, 123.0, 6.0], [122.0, 141.0, 6.0], [123.0, 124.0, 6.0], [123.0, 137.0, 6.0], [124.0, 125.0, 
6.0], [124.0, 137.0, 2.0], [125.0, 129.0, 6.0], [125.0, 132.0, 8.0], [126.0, 127.0, 2.0], [126.0, 129.0, 2.0], [128.0, 129.0, 6.0], [129.0, 130.0, 2.0], [130.0, 132.0, 2.0], [130.0, 131.0, 2.0], [131.0, 134.0, 4.0], [132.0, 133.0, 8.0], [133.0, 134.0, 8.0], [134.0, 135.0, 4.0], [135.0, 136.0, 6.0], [135.0, 139.0, 4.0], [136.0, 137.0, 6.0], [138.0, 140.0, 4.0], [138.0, 141.0, 6.0], [138.0, 139.0, 4.0]]

location = [['L01', 111.675804, 40.858645, 510.0], ['L02',111.682991, 40.829283, 660.0], ['L03', 111.645046, 40.807662, 430.0], ['L04', 111.616444, 40.851497, 930.0], ['L05', 111.720216, 40.85679, 760.0], ['L06', 111.655395, 40.810174, 570.0], ['L07', 111.668761, 40.842274, 540.0], ['L08', 111.686296, 40.803758, 650.0], ['L09', 111.734158, 40.841073, 400.0], ['L10', 111.705987, 40.807881, 500.0], ['L11', 111.655035, 40.854799, 1000.0], ['L12', 111.745081, 40.851006, 720.0], ['L13', 111.679972, 40.872394, 840.0], ['L14', 111.687302, 
40.849369, 530.0], ['L15', 111.712311, 40.855481, 430.0], ['L16', 111.671205, 40.808536, 500.0], ['L17', 111.598622, 40.810283, 950.0], ['L18', 111.604371, 40.836106, 980.0], ['L19', 111.634267, 40.779697, 1100.0], ['L20', 111.701675, 40.817163, 610.0], ['L21', 111.700094, 40.792398, 870.0], ['L22', 111.734446, 40.820439, 420.0], ['L23', 111.690177, 40.814024, 560.0], ['L24', 111.750399, 40.836816, 540.0], ['L25', 111.740051, 40.865957, 920.0], ['L26', 111.650077, 40.796303, 
880.0], ['L27', 111.725391, 40.810174, 780.0], ['L28', 111.611701, 40.806788, 920.0], ['L29', 111.674367, 40.827345, 600.0], ['L30', 111.737176, 40.812467, 670.0]]

def load_data():
    data = xlrd.open_workbook("Attachment 1.xlsx","rb")
    nums = len(data.sheets())
    sheet_nodes = data.sheet_by_name('nodes')
    sheet_links = data.sheet_by_name('links')
    sheet_location = data.sheet_by_name('location')
    
    for i in range(sheet_nodes.nrows):
        nodes.append(sheet_nodes.row_values(i))
    for i in range(sheet_links.nrows):
        links.append(sheet_links.row_values(i))
    for i in range(sheet_location.nrows):
        location.append(sheet_location.row_values(i))

def cal_matrix():
    a = np.zeros((141,141))
    for i in links:
        a[int(i[0])-1][int(i[1])-1] = ll_conver_distance(nodes[int(i[0]-1)][1:],nodes[int(i[1]-1)][1:])
        a[int(i[1])-1][int(i[0])-1] = a[int(i[0])-1][int(i[1])-1]
    # data = pd.DataFrame(a)
    # writer = pd.ExcelWriter('a.xlsx')   # 写入Excel文件
    # data.to_excel(writer, 'page_1', float_format='%.5f')    # ‘page_1’是写入excel的sheet名
    # writer.save()
    # writer.close()
    np.save("matrix_A.npy",a)

def ll_conver_distance(x,y):
    return math.sqrt((abs(x[0]-y[0])*Longitude_Factor)**2 + ((abs(x[1]-y[1])*Latitude_Factor))**2) 

if __name__ == "__main__":
    cal_matrix()
    b = np.load("matrix_A.npy")
    print(b[0,1])
