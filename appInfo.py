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
    for i in range(1,list_len+1):
        info["Question " +str(i)+ ": " +strips[start_idx+i]] = "Answer " +str(i)+ ": " +ans[i-1]        
    return info


def return_info():
    info = obtain_reqs(URL="https://fetch-hiring.s3.amazonaws.com/data-engineer/text-similarity.html",
           list_len=5,
           answer_list=["My application does not count punctuation",
                      "My application removes common stop words",
                      "My application does not care about the ordering of words",
                      "Number of unique matched words divided by total unique words in both samples",
                      "Dictionaries, lists, sets, and tuples are employed. Sets are used for comparing unique words between two samples and are helpful because they are more performant for lookups than lists."],
           list_begin="You will have to make a number of decisions as you develop this solution:")


    return info
    