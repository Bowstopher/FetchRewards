from urllib.request import urlopen
from bs4 import BeautifulSoup

def obtain_reqs(URL,list_len,answer_list,list_begin):
    url = URL
    html = urlopen(url).read()
    soup = BeautifulSoup(html) 
    
    for script in soup(["script", "style"]):
        script.decompose()
        
    strips = list(soup.stripped_strings)
    
    start_idx = strips.index(list_begin)
    ans = answer_list
    
    info = {}
    print(strips[start_idx])
    print("_"*len(strips[start_idx]))
    for i in range(1,list_len+1):
        print("Question " +str(i)+ ": " +strips[start_idx+i])
        print("Answer   " +str(i)+ ": " +ans[i-1])
        info["Question " +str(i)+ ": " +strips[start_idx+i]] = "Answer " +str(i)+ ": " +ans[i-1]
        print("_"*len(strips[start_idx]))
        
    return info


def return_info():
    info = obtain_reqs(URL="https://fetch-hiring.s3.amazonaws.com/data-engineer/text-similarity.html",
           list_len=5,
           answer_list=["My application does not count punctuation",
                      "My application removes common stop words",
                      "My application does not care about the ordering of words",
                      "Number of matched words divided by total words in both variables",
                      "Dictionaries, lists, strings, and tuples are employed"],
           list_begin="You will have to make a number of decisions as you develop this solution:")


    return info
    