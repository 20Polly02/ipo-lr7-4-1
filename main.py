books={
    1:{"title":" Война и мир","autor":"Лев Толстой","year":"1869"},
    2:{"title":"Дом в котором","autor":"Мариам Петросян","year":"2009"},
    3:{"title":"Любовь-ненависть","autor":"Анна Джейн","year":"2018"},
    4:{"title":"Смерть в облаках","autor":"Агата Кристи","year":"1935"},
    5:{"title":"Парфюмер","autor":"Патрик Зюскинд","year":"1985"}
}#
for key,book in books.items():#
    print(f"---------------------- Книга ",key,"-----------------------")#
    print (f"Название: {book["title"]}, Автор: {book["autor"]}")#
    print(f"----------------------{book["year"]}--------------------------")# 
print()#переход на следующую строку