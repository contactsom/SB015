import csv


booklist = [
        ['Title', 'Author', 'Genre', 'SubGenre', 'Height', 'Publisher'],
        ['Fundamentals of Wavelets', 'Goswami, Jaideva', 'tech', 'signal_processing', '228', 'Wiley'],
        ['Data Smart', 'Foreman, John', 'tech', 'data_science', '235', 'Wiley'],
        ['God Created the Integers', 'Hawking, Stephen', 'tech', 'mathematics', '197', 'Penguin'],
        ['Superfreakonomics', 'Dubner, Stephen', 'science', 'economics', '179', 'HarperCollins'],
        ['Orientalism', 'Said, Edward', 'nonfiction', 'history', '197', 'Penguin']
        ]

with open('teacher.csv', mode='w') as file:
    writer= csv.writer(file)

    for i in booklist:
        writer.writerow(i)

