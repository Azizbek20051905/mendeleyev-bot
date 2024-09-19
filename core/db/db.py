# import sqlite3

# # Ma'lumotlar bazasini yaratish yoki unga ulanish
# conn = sqlite3.connect('Base.db')
# c = conn.cursor()


# c.execute('''
#     CREATE TABLE IF NOT EXISTS courses (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         title TEXT NOT NULL,
#     )''')

# conn.commit()
# conn.close()

# def insert_movie(name, title):
#     conn = sqlite3.connect('Base.db')
#     c = conn.cursor()

#     c.execute('''
#         SELECT name, title FROM base WHERE name=?
#     ''', (name,))
    
    
#     movie = c.fetchone()
#     if movie is None:
#         c.execute('''
#             INSERT INTO courses (name, title) VALUES (?, ?)
#         ''', (name, title))

#         is_true = True
#     else:
#         is_true = False
    
#     conn.commit()
#     conn.close()

#     return is_true


# def update_movies(id, view):
#     conn = sqlite3.connect('movies.db')
#     c = conn.cursor()

#     # Qaysi ustunlarni yangilash kerakligini aniqlash
#     if view:
#         c.execute(f"UPDATE movies SET views = {view} WHERE id = {id}")

#     rows_affected = c.rowcount
#     conn.commit()
#     conn.close()
    
#     if rows_affected > 0:
#         print(f"ID: {id} bo'yicha save ma'lumotlari yangilandi.")
#         return True
#     else:
#         print(f"ID: {id} bo'yicha save topilmadi yoki yangilanmadi.")
#         return False