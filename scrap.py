from bs4 import BeautifulSoup
import requests, openpyxl

excel = openpyxl.Workbook()
print(excel.sheetnames)
sheet = excel.active
sheet.title ='loans'
print(excel.sheetnames)
sheet.append(['loan','rate'])


try:
     source = requests.get('https://ticker.finology.in/')
    
     
     soup = BeautifulSoup(source.text,'html.parser')
   
    
     pop = soup.find('tbody').find_all('tr')
     
     for movies in pop:
          
          name = movies.find('td').a.text
          rank= movies.find('td',class_ ="Number").text
          print(name, rank)
          sheet.append[(name, rank)]
         
     
except Exception as e:
     print(e)
     
     excel.save('rates.xlsx')