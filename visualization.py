import psycopg2
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

username = 'postgres'
password = 'postgres'
database = 'db_lab3_lukianenko'
host = 'localhost'
port = '5432'

query_1 = '''
select hours_per_day, depression 
from person 
join mental_illness on person.mental_illness_id = mental_illness.mental_illness_id
order by hours_per_day;
'''
query_2 = '''
select fav_genre, ocd
from person
join mental_illness on person.mental_illness_id = mental_illness.mental_illness_id
join music on person.music_id = music.music_id
where mental_illness.ocd < 5;
'''

query_3 = '''
select fav_genre, bpm
from person 
join mental_illness on person.mental_illness_id = mental_illness.mental_illness_id
join music on person.music_id = music.music_id
where mental_illness.averagescore > 5 and music.effects = 'Improve'
'''


conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(conn))

with conn:
    print("Database opened successfully")
    cur = conn.cursor()

    fig = plt.figure(figsize=(16, 9))
    gs = GridSpec(1, 3)

    # Запит 1. Вивести кількість годин прослуховування на день та рівень депресії
    cur.execute(query_1)
    hours_per_day, depression = zip(*cur)

    ax1 = fig.add_subplot(gs[0, 0])
    plt.bar(hours_per_day, depression, width=0.3)
    plt.bar(hours_per_day, depression,color = 'red', width=0.3, alpha = 0.3)    
    ax1.set_xlabel('Кількість годин на день')
    ax1.set_ylabel('Рівень депресії')
    ax1.set_title('Кількість годин прослуховування на день та рівень депресії')


    # Запит 2. Вивести улюблені жанри тих, у кого рівень тривоги менше 5
    cur.execute(query_2)
    fav_genres, ocd_values = zip(*cur)
    genre_counts = {}
    for genre in fav_genres:
        genre_counts[genre] = genre_counts.get(genre, 0) + 1

    labels = genre_counts.keys()
    sizes = genre_counts.values()

    ax2 = fig.add_subplot(gs[0, 1])
    ax2.pie(sizes, autopct='%1.1f%%', startangle=90)
    ax2.legend(labels)
    ax2.set_title('Улюблені жанри тих, у кого рівень тривоги менше 5')

    # Запит 3. Вивести жанри та bpm музики для людей з середнім рівнем психічних захворювань більше 5, яким музика покращує психічний стан
    cur.execute(query_3)
    fav_genres, bpm_values = zip(*cur)
    
    ax3 = fig.add_subplot(gs[0, 2])
    plt.scatter(fav_genres, bpm_values)  
    plt.xticks(fav_genres, ha='left', va='bottom') 
    ax3.set_xlabel('Улюблений жанр')
    ax3.set_ylabel('BPM')
    ax3.set_title('Жанри та bpm музики для людей з середнім рівнем психічних \n захворювань більше 5, яким музика покращує психічний стан')
    plt.savefig('graphs.png')
    plt.show()

conn.close()
