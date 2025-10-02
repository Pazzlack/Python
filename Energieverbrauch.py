Fernseher=3
Fernseherhr=3
Fernsehertage=365
Herd=2
Herdhr=2
herdtage=208
office=2
officehr=4
officetage=365
Heizung=8
Heizunghr=20
Heizungtage=170
Preis= 0.30
euro=round(Preis*(Fernseher*Fernseherhr*Fernsehertage+Herd*Herdhr*herdtage+office*officehr*officetage+Heizung*Heizunghr*Heizungtage),2)
result=f"Der Preis beträgt: {euro} Euro pro Jahr" 
print(result)