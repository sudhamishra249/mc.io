from bs4 import BeautifulSoup as SOUP 
import re 
import requests as HTTP 

def main(emotion): 
  
     
    if(emotion == "Sad" or emotion == "sad"): 
        urlhere = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'
  
    
    elif(emotion == "Disgust" or emotion =="disgust"): 
        urlhere = 'http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter, asc'
  
    
    elif(emotion == "Anger" or emotion=="anger"): 
        urlhere = 'http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc'
  
   
    elif(emotion == "Anticipation" or emotion=="anticipation"): 
        urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
   
    elif(emotion == "Fear" or emotion=="fear"): 
        urlhere = 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc'
  
    
    elif(emotion == "Enjoyment" or emotion=="enjoyment"): 
        urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
  
   
    elif(emotion == "Trust" or emotion=="trust"): 
        urlhere = 'http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc'
  
  
    elif(emotion == "Surprise" or emotion=="surprise"): 
        urlhere = 'http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter, asc'
   
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
   
