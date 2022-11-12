#%%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from pyecharts.charts import Geo
from pyecharts import options as opts
from pyecharts.globals import ThemeType

def KK():
    filename='data/zyly-szqdata.csv'
    outfilename='data/zyly-jgdata.csv'
    data=pd.read_csv(filename)
    df=data[[u'机构代码',u'机构名称']]
    df=df.drop_duplicates(subset=None,keep='first',inplace=False)
    df.to_csv(outfilename,index=False,encoding='utf-8')
    
def CreateNewColumn():
    filename='data/zyly-jgdata.csv'
    data=pd.read_csv(filename)
    m=Basemap(llcrnrlon=80.33,llcrnrlat=3.01,urcrnrlon=138.16,urcrnrlat=56.123,projection='lcc',lat_0=42.5,lon_0=120)
    m.drawcoastlines()
    m.drawcountries(linewidth=1.5)
    m.readshapefile(shapefile='gadm36_CHN_shp/gadm36_CHN_1',
                name='states',
                drawbounds=True) 
    #m.drawmapboundary(fill_color='white')
    #m.fillcontinents(color='white',lake_color='white')
    #m.drawcoastlines()
    plt.show()
    #print(data)
    
def createmapbypyecharts():
    filename='data/zyly-jgdata.csv'
    data=pd.read_csv(filename)
    data.dropna()
    print(data.describe())
    g=Geo().add_schema(maptype='内江')
    for i, row in data.iterrows():
        g.add_coordinate(row[1],row[3],row[2])
        g.add('',[(row[1],row[5])])
        #print('aaa:',row[1])
        #print('bbb:',row[2])
        #print('ccc:',row[3])
    g.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    g.set_global_opts(title_opts=opts.TitleOpts(title='XX区域基层医生分布情况图'),
                      visualmap_opts=opts.VisualMapOpts(
                          is_piecewise=True,
                          pieces=[
                    {"min":0,"max":5,"label":"1~5人","color":"cyan"},
                    {"min":6,"max":10,"label":"6~10人","color":"yellow"},
                    {"min":11,"max":15,"label":"11~15人","color":"orange"},
                    {"min":16,"max":20,"label":"16~20人","color":"coral"},
                    {"min":21,"max":25,"label":"21~25人","color":"blue"},
                    {"min":26,"max":30,"label":"26~30人","color":"red"},
                ]
                      ))
    #g.add_coordinate(addr,longitude,latitude)
    g.render()
    g.render_notebook()

def tjjzrs():
    filename='data/zyly-szqdata.csv'
    data=pd.read_csv(filename)
    df=data[[u'姓名',u'机构代码',u'机构名称']]
    df=df.groupby('机构代码').count()
    print(df)

def tjyszy():
    filename='data/zyly-ysdata.csv'
    data=pd.read_csv(filename)    
    df=data.groupby('机构代码').count()
    print(df)

if __name__=='__main__':
    #tjyszy()
    createmapbypyecharts()
    pass
# %%
