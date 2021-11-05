# Python tool to parse new price grid and generate Insurance Platform update scripts - Domestic/Legacy price calculator ONLY
from csv import reader

f = open("new_grid_DomesticInternational.sql", "a")

with open('grid.csv', 'r') as read_obj:
	csv_reader = reader(read_obj)
	headers = next(csv_reader)
	for row in csv_reader:
		for i in range(1, 30):
			maxCarPricePerDay = str('= '+row[1])+".00" if row[1] != 'NULL' else 'is NULL'
			maxVal = str(i) if i < 29 else str(999)
			line = "UPDATE PRICING_BasePriceDuration JOIN PRICING_Duration using (idDuration) JOIN PRICING_BasePrice using (idBasePrice) SET pricePerDay = "+row[i+2].split("£")[1]+" WHERE min = "+str(i)+" and max = "+maxVal+" and minCarPricePerDay = "+str(row[0])+".00 and maxCarPricePerDay "+maxCarPricePerDay+"; \n"
			f.write(line)

# To do run execute 'python3 parseCSVDomesticInternational.py'