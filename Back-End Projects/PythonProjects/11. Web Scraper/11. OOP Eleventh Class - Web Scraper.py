# HTML, CSS AND JS
# pip install beutifulsoup4
# pip install lxml
# pip install request


#####EXTRACT TITTLE AND PARAGRAPH TEXT FROM WEB PAGE
#import bs4
#import requests
#result = requests.get("https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html")
#soup = bs4.BeautifulSoup(result.text, "lxml")
#print(type(result))
#print(result.text)


#print(soup)
#print(soup.select("title"))
#print(soup.select("p"))
#print(len(soup.select("p")))
#print(soup.select("title")[0])
#print(soup.select("title")[0].getText())

#special_paragraph = soup.select("p")[3].get_text()
#print(special_paragraph)

#####EXTRACT CLASS ELEMENTS LESSON
#"" looks for the label, ex: <p> <div> <title>
# #_style_4 = looks for the id of _style_4
# ._bottom = looks for the class of _bottom
# div span = looks for the span elements inside a div
# div>span = looks for the span elements without elements between div and span

"""import bs4
import requests

result = requests.get("https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html")
soup = bs4.BeautifulSoup(result.text, "lxml")

post_header = soup.select(".post-header span")[0]

for span in post_header:
    print(span.getText())"""

##### EXTRACT IMAGES FROM WEB PAGE
"""import bs4
import requests

result = requests.get("https://www.escueladirecta.com/courses")
soup = bs4.BeautifulSoup(result.text, "lxml")"""

#images = soup.select("img")
#print(images)
#print(len(images))
"""images = soup.select(".course-box-image")
for i in images:
    print(i)"""

"""images = soup.select(".course-box-image")
for i in images:
    print(i["src"])

images = soup.select(".course-box-image")[0]["src"]
img_course_one = requests.get(images)
#print(img_course_one.content)
f_one = open("f_one.jpg","wb")
f_one.write(img_course_one.content)
f_one.close()"""

"""images = soup.select(".course-box-image")
for i in images:
    img = requests.get(i["src"])
    f = open("f.jpg","wb")
    f.write(img.content)
    f.close()"""

"""import bs4
import requests

base_url = "http://books.toscrape.com/catalogue/page-{}.html"

#print(base_url.format("15"))
#for n in range(1,51):
    #print(base_url.format(n))"""

#result = requests.get(base_url.format("1"))
#soup = bs4.BeautifulSoup(result.text,"lxml")
"""print(len(soup.select(".product_pod")))"""
#books_list = soup.select(".product_pod")
#ex = books_list[0].select(".star-rating.Three")
#print(ex)
#title = books_list[0].select("a")[1]["title"]
#print(title)"""


##### BOOKSTORE WEB SCRAPER
import bs4
import requests
#Creates an URL without page number
base_url = "http://books.toscrape.com/catalogue/page-{}.html"
# List of titles with 4 or 5 stars
book_titles_high_rating = []
#Iterates pages of the web page
for n in range(1,51):
    #Creates soup for each page
    result = requests.get(base_url.format(n))
    soup = bs4.BeautifulSoup(result.text, "lxml")
    #Gets all books from each page
    books_list = soup.select(".product_pod")
    #Iterate books = 4 or 5 stars
    for book in books_list:
        if (len(book.select(".star-rating.Four")) != 0 or len(book.select(".star-rating.Five"))):
            #Saves title inside a variable
            title = book.select("a")[1]["title"]
            #Add book title to a list
            book_titles_high_rating.append(title)

#See all book titles
for t in book_titles_high_rating:
    print(t)

























