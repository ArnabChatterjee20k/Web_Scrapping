
from bs4 import BeautifulSoup as bs
import requests,pandas as pd



link="https://www.amazon.in/Noise-Wireless-Instacharge-Hypersync-Technology/product-reviews/B092DHTXH2/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"

page=requests.get(link)
status=page.status_code
print(status)
soup=bs(page.content,"html.parser")
# print(soup.prettify())

#we require names so we have to get its class name by inspecting the class in the web

if status==200:
    names=soup.find_all("span",class_="a-profile-name")
    # print(names)
    #In names names along with html code was also present do we have to get the text
    cust_name=[]
    for i in range(0,len(names)):
        cust_name.append(names[i].get_text())
    # print(cust_name)


    title=soup.find_all("a",class_="a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold")
    # print(title)
    review_title=[]
    for i in range(0,len(title)):
        review_title.append(title[i].get_text())
    # print(review_title)

    #we can also use the previou tag class of required class to get the data but while itegarting to get text we will get \n text \n . We will strip the \n easily by
    # review[:]=[titles.lstrip(\n) for titles in review_title]
    #similarly rstrip
    review_title[:]=[items.lstrip("\n") for items in review_title]
    review_title[:]=[items.rstrip("\n") for items in review_title]


    #next we need star
    rating=soup.find_all("i",class_="review-rating")
    # print(rating)
    rating_star=[]
    for i in range(0,len(rating)):
        rating_star.append(rating[i].get_text())
    # print(rating_star)


    #content
    content=soup.find_all("span",{"data-hook":"review-body"})#by data hook
    # print(content)
    cont=[]
    for i in range(0,len(content)):
        cont.append(content[i].get_text())

    #stripping \n from left and right
    cont[:]=[items.lstrip("\n") for items in cont]
    cont[:]=[items.rstrip("\n") for items in cont]
    # print(cont)


    try:
        cust_name.pop(0)
        cust_name.pop(0)

        rating_star.pop(0)
        rating_star.pop(0)
    except:
        raise Exception("Plz check connencrtion")

    print(f"""
    names=={len(cust_name)}
    title=={len(review_title)}
    rating=={len(rating_star)}
    content=={len(cont)}
    """)

    data={
        "customer_name":cust_name,
        "ReviewTitle":review_title,
        "Rating":rating_star,
        "COntent":cont
    }

    # print(data)
    df=pd.DataFrame(data)
    # print(df)
    df.to_csv("Amazon review.csv",index=False)



else:
    raise Exception("Status Code is not 200 ")