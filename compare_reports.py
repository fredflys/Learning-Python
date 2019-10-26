import os
import re
import pandas as pd
from pyecharts.charts import Bar
from pyecharts import options as opts

# 上次和本次测试报告目录
last_folder = 'Prod-10-22'
this_folder = 'Prod-10-26'

# 要对比的页面，部分匹配即可
page_labels = ['Order List', 'My Workflows Open', 'My Workflows', 'My View', 'My Assignment', 'Login', 'Opportunity List', 'CNOC List', '总体',
              'GM My View','GM  My Workflows', 'GM  My Assignment', 'Workflow Open'
              ]

# 要对比的接口，部分匹配即可
api_labels = [
   'Post_SearchOppList',
    'Post_SearchMyWorkFlowList',
    'Post_SearchMyViewList',
    'Post_SearchMyAssignmentList',
    'Post_SearchOppList',
    'Post_SearchOrderList',
    'Get_ApplicationFormInfo'
]

# 要比较的列
target = 'Average'

# 分BU出报告
bus = ['pa', 'mcproject', 'mcp113', 'mc', 'cp', 'fa']

def read_reports_excel(folder, sheet_name):
    cp_df = pd.read_excel(os.path.join(folder, 'cp.xlsx'), sheet_name=sheet_name)
    mc_df = pd.read_excel(os.path.join(folder, 'mc.xlsx'), sheet_name=sheet_name)
    mcp113_df = pd.read_excel(os.path.join(folder, 'mcp113.xlsx'), sheet_name=sheet_name)
    mcproject_df = pd.read_excel(os.path.join(folder, 'mcproject.xlsx'), sheet_name=sheet_name)
    pa_df = pd.read_excel(os.path.join(folder, 'pa.xlsx'), sheet_name=sheet_name)
    fa_df = pd.read_excel(os.path.join(folder, 'fa.xlsx'), sheet_name=sheet_name)
    return cp_df, mc_df, mcp113_df, mcproject_df, pa_df, fa_df

def read_reports_csv(folder):
    cp_df = pd.read_csv(os.path.join(folder, 'cp.csv'))
    mc_df = pd.read_csv(os.path.join(folder, 'mc.csv'))
    mcp113_df = pd.read_csv(os.path.join(folder, 'mcp113.csv'))
    mcproject_df = pd.read_csv(os.path.join(folder, 'mcproject.csv'))
    pa_df = pd.read_csv(os.path.join(folder, 'pa.csv'))
    fa_df = pd.read_csv(os.path.join(folder, 'fa.csv'))
    return cp_df, mc_df, mcp113_df, mcproject_df, pa_df, fa_df

def df_isin(df, labels):
    return df[df['Label'].isin(labels)]


def df_contains(df, partial_labels):
    '''
	这一步是为了找出要对比的数据
	遍历列表，在Dataframe中匹配，凡是包含当前字符串的，都拿出来
    '''
    result_df = None
    for label in partial_labels:
        x = df[df['Label'].str.contains(label)]
        if result_df is None:
            result_df = x
        else:
            if not x.empty:
                result_df = result_df.append(x, ignore_index=True)
    return result_df.drop_duplicates(subset=['Label', 'Average','Median'], keep='first')

def replace_digits_in_df(df, label):
    '''
	这一步是为了取出label中的数字
	Jmeter录制的脚本中，每次请求前面都会加上序号，影响排序，需要统一去掉
	当然也许Jmeter中本身就可以设置，只是我不知道
    '''
    for row in df.iterrows():
        _ = row[1].Label
        df.loc[row[0], label] = re.sub('\d+', '', _)
    return df


def draw_api(last_df, this_df, column):
    '''
    last_df: 上一次结果，pd.Dataframe
    this_df: 本次结果，pd.Dataframe
    return: 柱状对比图，可在notebook中绘制，也可直接导出html
    '''
    last_temp = replace_digits_in_df(last_df,'Label')
    last = df_contains(last_temp, api_labels).sort_values(by=['Label'])
    
    this_temp = replace_digits_in_df(this_df,'Label')
    this = df_contains(this_df,api_labels).sort_values(by=['Label'])
   
    print(this.Label)
    print('--------')
    print(last.Label)

    # 下面都是为了取出新旧待比较数据集中的交集，避免数据错位
    this_del_index = this.append(last, sort=False).drop_duplicates(subset=['Label'], keep=False).index
    this = this.drop(this_del_index)
    
    last_del_index = last.append(this, sort=False).drop_duplicates(subset=['Label'], keep=False).index
    last = last.drop(last_del_index)
    

    
    this_average = this[column]
    this_label = this.Label
    last_average = last[column]
    last_label = last.Label
    

    bar = (
    Bar({"width": "800px", "height": "750px", })
    .add_xaxis(list(last_label))
    .add_yaxis('Response Time Average This Time',list(this_average))
    .add_yaxis('Response Time Average Last TIme',list(last_average))
    .set_global_opts(
        title_opts=opts.TitleOpts(title='接口平均相应时间对比图'),
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=15)),
        legend_opts=opts.LegendOpts(is_show=True, pos_right=10)
    )
    )
    return bar

def draw_page(last_df, this_df, column) -> Bar:
    '''
    last_df: 上一次结果，pd.Dataframe
    this_df: 本次结果，pd.Dataframe
    return: 柱状对比图，可在notebook中绘制，也可直接导出html
    '''
    
    last = df_contains(last_df, page_labels).sort_values(by=['Label'])
    this = df_contains(this_df,page_labels).sort_values(by=['Label'])
   
    print(this.Label)
    print('--------')
    print(last.Label)
    this_del_index = this.append(last, sort=False).append(last, sort=False).drop_duplicates(subset=['Label'], keep=False).index
    this = this.drop(this_del_index)

    
    last_del_index = last.append(this, sort=False).append(this, sort=False).drop_duplicates(subset=['Label'], keep=False).index
    last = last.drop(last_del_index)
    
    
    this_average = this[column]
    this_label = this.Label
    last_average = last[column]
    last_label = last.Label
#     print(this_label)
#     print('--------')
#     print(last_label)
    bar = (
    Bar({"width": "800px", "height": "700px", })
    .add_xaxis(list(last_label))
    .add_yaxis('Response Time Average This Time',list(this_average))
    .add_yaxis('Response Time Average Last TIme',list(last_average))
    .set_global_opts(
        title_opts=opts.TitleOpts(title='页面平均相应时间对比图'),
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=15)),
        legend_opts=opts.LegendOpts(is_show=True, pos_right=10)
    )
    )
    return bar


if __name__ == "__main__":
    last_cp_df, last_mc_df, last_mcp113_df, last_mcproject_df, last_pa_df, last_fa_df = read_reports_excel(last_folder, '30线程')
    this_cp_df, this_mc_df, this_mcp113_df, this_mcproject_df, this_pa_df, this_fa_df = read_reports_csv(this_folder)
    for bu in bus:
        draw_api(eval('last_'+ bu + '_df'), eval('this_'+ bu + '_df'), target).render('api_' + bu + '.html')
        draw_page(eval('last_'+ bu + '_df'), eval('this_'+ bu + '_df'), target).render('page_' + bu + '.html')
        print('Successfully done......')