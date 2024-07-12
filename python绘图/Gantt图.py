import plotly.graph_objects as go  
from datetime import datetime  
# 定义任务数据，确保Start和Finish是字符串格式的日期  
tasks = [  
    dict(Task="任务1", Start='2023-01-01', Finish='2023-01-10', Progress=40),  
    dict(Task="任务2", Start='2023-01-05', Finish='2023-01-20', Progress=20),  
    dict(Task="任务3", Start='2023-01-15', Finish='2023-01-25', Progress=60),  
    # 添加更多任务...  
]  

# 转换日期字符串为datetime对象，并计算时间差  
for task in tasks:  
    task['Start'] = datetime.strptime(task['Start'], '%Y-%m-%d')  
    task['Finish'] = datetime.strptime(task['Finish'], '%Y-%m-%d')  
    task['Duration'] = (task['Finish'] - task['Start']).total_seconds() * 1000  # 转换为毫秒  
  
# 初始化figure和添加Gantt条（略去其他代码，只展示关键部分）  
fig = go.Figure(data=[go.Bar(  
    # ... 其他参数 ...  
)]) 

# 添加Gantt条  
for i, task in enumerate(tasks):  
    fig.add_trace(go.Bar(  
        x=[task['Start'], task['Finish']], y=[i, i],  
        name=task['Task'],  
        offsetgroup=i,  
        orientation='h',  
        marker_color='rgb(49,130,189)',  
        opacity=0.6,  
        text=[f"{task['Progress']}% 完成"],  
        textposition='auto',  
        width=[(task['Finish'] - task['Start']).total_seconds() * 1000],  # 宽度以毫秒为单位  
        hoverinfo='text+name'  
    ))  
  
# 更新x轴和y轴  
fig.update_xaxes(  
    rangeslider_visible=True,  
    rangeselector=dict(  
        buttons=list([  
            dict(count=1, label="1m", step="month", stepmode="backward"),  
            dict(count=6, label="6m", step="month", stepmode="backward"),  
            dict(count=1, label="YTD", step="year", stepmode="todate"),  
            dict(count=1, label="1y", step="year", stepmode="backward"),  
            dict(step="all")  
        ])  
    )  
)  
fig.update_yaxes(showgrid=False, zeroline=False)  
  
# 更新layout  
fig.update_layout(  
    barmode='stack',  
    title='Gantt Chart',  
    margin=dict(t=100),  
    hovermode='closest'  
)  
  
# 显示图表  
fig.show()