from datetime import datetime
import pandas as pd

def file_sort():
    def convert_to_datetime(date):
        try:
            if date[0] == '2':
                int(date[2:4])
                m, d = int(date[0]), int(date[2:4])
            else:
                int(date[3:5])
                m, d = int(date[0]), int(date[3:5])
        except:
            if date[0] == '2':
                m, d = int(date[0]), int(date[2])
            else:
                m, d = int(date[0]), int(date[3])
        return datetime(2020,m,d).strftime('%Y-%m-%d')

    df = pd.read_csv('dataset/코로나바이러스감염증-19 국내 발생 현황(총계).csv', engine='python', encoding='cp949', index_col=[0])
    idx_result = []
    for date in df.index:
        idx_result.append(convert_to_datetime(date))

    df.index = idx_result
    df = df.sort_index()
    df.to_csv('코로나바이러스감염증-19 국내 발생 현황.csv', encoding='cp949')

if __name__ == '__main__':
    file_sort()