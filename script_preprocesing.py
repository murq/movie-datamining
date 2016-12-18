import csv
from collections import Counter
import plotly.plotly as py
import plotly.graph_objs as go
import plotly



def cut_off(dict, limit):
    res = []
    for d in dict:
        if (d[1]>=limit):
            res.append(d)
    return res
def generate_histogram(dict,name):
    x = []
    y = []
    for d in dict:
        x.append(d[0])
        y.append(d[1])
    data = [go.Bar(
            x=x,
            y=y
    )]
    py.iplot(data, filename=name)


def get_all_index_counted(reader, index):
    result = []
    first = True
    for row in reader:
        if not first and row[9] == 'USA':
            result_aux = row[index].split("|")
            for g in result_aux:
                result.append(g)
        else:
            first = False
    return Counter(result).most_common()

def get_all_actors_counted(reader):
    result = []
    first = True
    for row in reader:
        if not first and row[9] == 'USA':
            result.append(row[2])
            result.append(row[3])
            result.append(row[4])
        else:
            first = False
    return Counter(result).most_common()

def build_header(directors, actors, genres, keywords, crating):
    headers = ['movie_title','director_popularity', 'main_actor', 'secondary_actor', 'third_actor']

    headers.append('duration')

    for g in genres:
       headers.append("gen_"+ g[0])

    headers.append('num_voted_users')

    headers.append("keyword_1")
    headers.append("keyword_2")
    headers.append("keyword_3")
    headers.append("keyword_4")
    headers.append("keyword_5")

    for cr in crating:
        headers.append("crat_"+ cr[0])
    headers.append("profit_ratio")
    headers.append("imdb_score")
    return headers

#plotly.tools.set_credentials_file(username='DavidGarcia8ea2', api_key='#')
with open('metadata.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    genres = get_all_index_counted(reader, 6)
    #generate_histogram(genres, 'genres')
    csvfile.seek(0)
    keywords = get_all_index_counted(reader, 8)
    #keywords = cut_off(keywords, 5)
    #generate_histogram(keywords, 'keywords')
    csvfile.seek(0)
    actors = get_all_actors_counted(reader)
    #actors = cut_off(actors, 5)

    #generate_histogram(actors, 'actors')
    csvfile.seek(0)
    directors = get_all_index_counted(reader, 1)
    #directors = cut_off(directors, 5)
    #generate_histogram(directors, 'directors')
    csvfile.seek(0)

    crating = get_all_index_counted(reader, 10)
    csvfile.seek(0)

    with open('metadata_clean.csv', 'wb') as csvfile_clean:
        writter = csv.writer(csvfile_clean)
        header = build_header(directors,actors, genres, keywords, crating)
        writter.writerow(header)
        first = True
        for row in reader:
            if not first:
                if row[9] != 'USA':
                    continue
                if row[1] == '':
                    #director
                    continue
                if row[2] == '' or row[3] == '' or row[4] =='':
                    #actors
                    continue
                if row[5] == '':
                    continue
                if row[6] == '':
                    continue
                if row[7] == '':
                    continue
                if row[10] == '':
                    continue
                if row[14] == '':
                    continue
                line = []
                line.append(row[0].rstrip())
                found_d = False
                for d in directors:
                    if d[0] == row[1]:
                        line.append(d[1])
                        found_d = True
                        break
                if not found_d:
                    line.append(0)

                found_a_1 = False
                for a in actors:
                    if a[0] == row[2]:
                        line.append(a[1])
                        found_a_1 = True
                        break
                if not found_a_1:
                    line.append(0)


                found_a_2 = False
                for a in actors:
                    if a[0] == row[3]:
                        line.append(a[1])
                        found_a_2 = True
                        break
                if not found_a_2:
                    line.append(0)


                found_a_3 = False
                for a in actors:
                    if a[0] == row[4]:
                        line.append(a[1])
                        found_a_3 = True
                        break
                if not found_a_3:
                    line.append(0)


                line.append(row[5])
                for g in genres:
                    if g[0] in row[6]:
                        line.append(1)
                    else: line.append(0)

                line.append(row[7])

                keys = row[8].split('|')
                ar = keys[:5]
                count_k = 1

                for a in ar:
                    f_k = False
                    for k in keywords:
                        if k[0] == a:
                            line.append(k[1])
                            f_k = True
                            break
                    if not f_k:
                        line.append(0)
                    count_k = count_k +1

                while count_k <= 5:
                    count_k = count_k +1
                    line.append(0)

                for cr in crating:
                    if cr[0] == row[10]:
                        line.append(1)
                    else: line.append(0)
                line.append(row[14])
                if float(row[13]) <= 5.7:
                    line.append("LET_57")
                elif float(row[13]) >= 5.8 and float(row[13]) <= 6.5:
                    line.append("GET_58_AND_LET_65")
                elif float(row[13]) >= 6.6 and float(row[13]) <= 7.1:
                    line.append("GET_66_AND_LET_71")
                elif float(row[13]) >= 7.2:
                    line.append("GET_72")

                writter.writerow(line)
            else:
                first = False