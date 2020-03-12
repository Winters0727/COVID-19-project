import os
import pandas as pd

def merge():
    file_list = os.listdir('dataset')

    if '코로나바이러스감염증-19 국내 발생 현황(총계).csv' in file_list:
        df_total = pd.read_csv('dataset/코로나바이러스감염증-19 국내 발생 현황(총계).csv', engine='python', encoding='cp949', index_col=[0])
    else:
        df_total = pd.DataFrame({0:[0,0,0,0,0,0,0,0]}, columns=['총계','계(확진)', '격리해제', '격리 중', '사망', '계(검사)', '검사 중', '결과 음성'])

    if '코로나바이러스감염증-19 국내 발생 현황(정례브리핑).csv' in file_list:
        df_brief = pd.read_csv('dataset/코로나바이러스감염증-19 국내 발생 현황(정례브리핑).csv', engine='python', encoding='cp949', index_col=[0])
    else:
        df_brief = pd.DataFrame({0:[0,0,0,0,0,0,0,0]}, columns=['총계','계(확진)', '격리해제', '격리 중', '사망', '계(검사)', '검사 중', '결과 음성'])

    for f in file_list:
        if '정례브리핑' in f and f != '코로나바이러스감염증-19 국내 발생 현황(정례브리핑).csv':
            df_temp = pd.read_csv('dataset/' + f, engine='python', encoding='cp949', index_col=[0])
            df_brief.loc[df_temp.index[0]] = df_temp.iloc[0,:]
        else: 
            if f != '코로나바이러스감염증-19 국내 발생 현황(총계).csv':
                df_temp = pd.read_csv('dataset/' + f, engine='python', encoding='cp949', index_col=[0])
                df_total.loc[df_temp.index[0]] = df_temp.iloc[0,:]
    
    df_total = df_total.sort_index()
    df_brief = df_brief.sort_index()

    df_total.to_csv('dataset/코로나바이러스감염증-19 국내 발생 현황(총계).csv', encoding='cp949')
    df_total.to_csv('코로나바이러스감염증-19 국내 발생 현황(총계).csv', encoding='cp949')
    df_brief.to_csv('dataset/코로나바이러스감염증-19 국내 발생 현황(정례브리핑).csv', encoding='cp949')
    df_brief.to_csv('코로나바이러스감염증-19 국내 발생 현황(정례브리핑).csv', encoding='cp949')

if __name__ == '__main__':
    merge()