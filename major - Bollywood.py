from bs4 import BeautifulSoup as SOUP 
import re 
import requests as HTTP 
  
 
def main(emotion): 
  
    
    if(emotion == "Sad" or emotion == "sad"): 
        urlhere = 'https://www.imdb.com/list/ls009576722/'
  
    elif(emotion == "Disgust" or emotion == "disgust"): 
        urlhere = 'https://www.imdb.com/list/ls075745491/'
  
    elif(emotion == "Anger" or emotion == "anger"): 
        urlhere = 'https://www.imdb.com/list/ls000445157/'
  
    elif(emotion == "Anticipation" or emotion == "anticipation"): 
        urlhere = 'https://www.imdb.com/india/upcoming/'
  
    elif(emotion == "Fear" or emotion == "fear"): 
        urlhere = 'https://www.imdb.com/list/ls058201636/'
  
    elif(emotion == "Enjoyment" or emotion == "enjoyment"): 
        urlhere = 'https://www.imdb.com/list/ls005597767/'
  
    elif(emotion == "Trust" or emotion == "trust"): 
        urlhere = 'https://www.imdb.com/list/ls051594496/'
  
    elif(emotion == "Surprise" or emotion == "surprise"): 
        urlhere = 'https://www.imdb.com/list/ls008944391/'
  
    
    response = HTTP.get(urlhere) 
    data = response.text 
  
    
    soup = SOUP(data, "html.parser")

    title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')}) 
    return title 
  

if __name__ == '__main__': 
  
    emotion = input("Enter the emotion: ") 
    a = main(emotion)
  
    count = 0
  
    for i in a: 
    
        tmp = str(i).split('>')
        print(tmp)
        if(len(tmp) == 3):
            print(tmp[1][:-3])
            
        if(count > 15): 
            break
        count += 1
   
