import requests
from bs4 import BeautifulSoup

url="https://www.codewithharry.com"

#step1: getting the html
r=requests.get(url)
html_content=r.content
# print(html_content)

#step2: parse the html
soup=BeautifulSoup(html_content,"html.parser")
#print(soup)
# print(soup.prettify)

#step3: HTML Tree transversal
#commonly used type of objects: 
# print(type(soup))# BeautifulSoup
# print(title)
# print(type(title))# Tag
# print(type(title.string))# NavigableString
# Comment
markup="<p><!-- this is a comment and code getted exited here-->"
soup2=BeautifulSoup(markup)
print(type(soup2.p.string))
# exit()

title=soup.title#getting title of HTML page

#getting all paragraphs from the page
paras=soup.find_all('p')
# print(paras)



print(soup.find("p"))#to get the first element in html image
print(soup.find("p")["class"])#to get the class of any element

#It will return us error as no id is present
# print(soup.find("p")["id"])#to get the id of any element

# find all the elemnts with class lead
print(soup.find_all("p",class_="lead"))

print()
#to get the text from the tags/soup
print(soup.find("p").get_text())

#to get text from whole html
print(soup.get_text())


#getting all anchor atgs from the page
anchor=soup.find_all('a')
#get all the links on the page
link_set=set()
for link in anchor:
    if (link.get("href") != "#"): #to avoid # links  
        link_text="https://www.codewithharry.com"+link.get("href")
        link_set.add(link)
        # print(link_text)
    # print(link.get("href"))  #here the links are repeated. So add the links to a set to avoid repeatation due to property of set

# print(anchor)

#MOre with bs4
#contents
navbarSupportedContent= soup.find(id="navbarSupportedContent")
# print(navbarSupportedContent)
#to get its children
# print(navbarSupportedContent.children)
# for i in navbarSupportedContent.children:
#     print(i)

#to get all the elements
# print(navbarSupportedContent.contents)
# for i in navbarSupportedContent.contents:
#     print(i)

## .content== a tag's children are available as a list.Elements are stored in memory.
## .children== a tag's children are available as a generator.They are not stored in memory but we can get it through iterator or next method

#In big page .content is slow due to memory. So use .children in big pages

#printing the strings in the id
# for i in navbarSupportedContent.strings:
#     print(i)

#printing strpped strings
# for i in navbarSupportedContent.stripped_strings:
#     print(i)


#getting parent tag
# print(navbarSupportedContent.parent)

#A generator object
# print(navbarSupportedContent.parents)
# for item in navbarSupportedContent.parents:
#     print(item.name)


#next sibling and previous sibling.Line or spaces 
# print(navbarSupportedContent.next_sibling)
# print(navbarSupportedContent.next_sibling.next_sibling)
# print(navbarSupportedContent.previous_sibling.previous_sibling)

#in these spaces andlines are considered as elements.So be careful



#Css selectors.We can aslo use css selectors
elem=soup.select("#loginModal") #getting element of id loginmodal
print(elem)

elem=soup.select(".loginModal") #getting element of class loginmodal if present
print(elem)

#These were all reading process



#Manipulating dom

