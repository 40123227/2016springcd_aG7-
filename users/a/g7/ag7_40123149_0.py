# 各組分別在各自的 .py 程式中建立應用程式 (第1步/總共3步)
from flask import Blueprint, render_template

# 利用 Blueprint建立 ag1, 並且 url 前綴為 /ag1, 並設定 template 存放目錄
ag7_40123149_0 = Blueprint('ag7_40123149_0', __name__, url_prefix='/ag7', template_folder='ag7_40123149_0')

# scrum1_task1 為完整可以單獨執行的繪圖程式
@ag7_40123149_0.route('/ag7_40123149_0')
def task1():
    outstring = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>網際 2D 繪圖</title>
    <!-- IE 9: display inline SVG -->
    <meta http-equiv="X-UA-Compatible" content="IE=9">
<script type="text/javascript" src="http://brython.info/src/brython_dist.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango-8v03.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango2D-6v13.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/CangoAxes-1v33.js"></script>

</head>
<body>

<script>
window.onload=function(){
brython(1);
}
</script>

<canvas id="plotarea" width="800" height="800"></canvas>

<script type="text/python">
from javascript import JSConstructor
from browser import window
import math

cango = JSConstructor(window.Cango)
cobj = JSConstructor(window.Cobj)
shapedefs = window.shapeDefs
obj2d = JSConstructor(window.Obj2D)
cgo = cango("plotarea")

cgo.setWorldCoords(-250, -250, 500, 500) 

# 決定要不要畫座標軸線
cgo.drawAxes(0, 240, 0, 240, {
    "strokeColor":"#aaaaaa",
    "fillColor": "#aaaaaa",
    "xTickInterval": 20,
    "xLabelInterval": 20,
    "yTickInterval": 20,
    "yLabelInterval": 20})
        
#cgo.drawText("使用 Cango 繪圖程式庫!", 0, 0, {"fontSize":60, "fontWeight": 1200, "lorg":5 })

deg = math.pi/180  
def O(x, y, rx, ry, rot, color, border, linewidth):
    # 旋轉必須要針對相對中心 rot not working yet
    chamber = "M -6.8397, -1.4894 \
                     A 7, 7, 0, 1, 0, 6.8397, -1.4894 \
                     A 40, 40, 0, 0, 1, 6.8397, -18.511 \
                     A 7, 7, 0, 1, 0, -6.8397, -18.511 \
                     A 40, 40, 0, 0, 1, -6.8397, -1.4894 z"
    cgoChamber = window.svgToCgoSVG(chamber)
    cmbr = cobj(cgoChamber, "SHAPE", {
            "fillColor": color,
            "border": border,
            "strokeColor": "tan",
            "lineWidth": linewidth })

    # 複製 cmbr, 然後命名為 basic1
#K
    basic101 = cmbr.dup()
    basic101.rotate(180)
    basic101.translate(80, 100)
    basic102 = cmbr.dup()
    basic102.rotate(0)
    basic102.translate(80, 80)
    
    basic103 = cmbr.dup()
    basic103.rotate(0)
    basic103.translate(80, 140)
    
    basic105 = cmbr.dup()
    basic105.rotate(90)
    basic105.translate(80, 100)

    basic107 = cmbr.dup()
    basic107.rotate(30)
    basic107.translate(100, 100)
    
    basic108 = cmbr.dup()
    basic108.rotate(150)
    basic108.translate(100, 100)
    
    basic1011 = cmbr.dup()
    basic1011.rotate(150)
    basic1011.translate(110.5, 118)
    
    basic1012 = cmbr.dup()
    basic1012.rotate(32.5)
    basic1012.translate(110.5, 82)
    basic1013 = cmbr.dup()
    basic1013.rotate(0)
    basic1013.translate(80, 100)

  #K
    cmbr.appendPath(basic101)
    cmbr.appendPath(basic102)
    cmbr.appendPath(basic103)
    cmbr.appendPath(basic105)
    cmbr.appendPath(basic107)
    cmbr.appendPath(basic108)
    cmbr.appendPath(basic1011)
    cmbr.appendPath(basic1012)
    cmbr.appendPath(basic1013)
    
    # hole 為原點位置
    hole = cobj(shapedefs.circle(4), "PATH")
    cmbr.appendPath(hole)

    # 表示放大 3 倍
    #cgo.render(cmbr, x, y, 0.5, rot)
    # 放大 5 倍
    cgo.render(cmbr, x, y, 0.5, rot)

O(0, 0, 0, 0, 0, "lightyellow", True, 4)
</script>
<!-- 以協同方式加上 ag100 的 scrum-2 組員所寫的 task1 程式碼 -->
<script type="text/python" src="/ag7/a40123149_task0"></script>
<!-- 以協同方式加上 ag100 的  scrum-3 組員所寫的 task1 程式碼 -->
<!-- <script type="text/python" src="/ag100/scrum3_task1"></script>-->
</body>
</html>

'''
    return outstring
    

    
    
