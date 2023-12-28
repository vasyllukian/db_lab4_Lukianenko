import psycopg2
import matplotlib.pyplot as plt

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

    # Запит 1. Вивести кількість годин прослуховування на день та рівень депресії
    cur.execute(query_1)
    hours_per_day, depression = zip(*cur)

    plt.bar(hours_per_day, depression, width=0.3)
    plt.bar(hours_per_day, depression,color = 'red', width=0.3, alpha = 0.3)    
    plt.xlabel('Кількість годин на день')
    plt.ylabel('Рівень депресії')
    plt.title('Кількість годин прослуховування на день та рівень депресії')
    plt.show()


    # Запит 2. Вивести улюблені жанри тих, у кого рівень тривоги менше 5
    cur.execute(query_2)
    fav_genres, ocd_values = zip(*cur)
    genre_counts = {}
    for genre in fav_genres:
        genre_counts[genre] = genre_counts.get(genre, 0) + 1

    labels = genre_counts.keys()
    sizes = genre_counts.values()

    plt.pie(sizes, autopct='%1.1f%%', startangle=90)
    plt.legend(labels, loc='best')
    plt.title('Улюблені жанри тих, у кого рівень тривоги менше 5')
    plt.show()

    # Запит 3. Вивести жанри та bpm музики для людей з середнім рівнем психічних захворювань більше 5, яким музика покращує психічний стан
    cur.execute(query_3)
    fav_genres, bpm_values = zip(*cur)

    plt.scatter(fav_genres, bpm_values)  
    plt.xticks(fav_genres, ha='left', va='bottom')
    plt.xlabel('Улюблений жанр')
    plt.ylabel('BPM')
    plt.title('Жанри та bpm музики для людей з середнім рівнем психічних \n захворювань більше 5, яким музика покращує психічний стан')
    plt.show()

conn.close()
