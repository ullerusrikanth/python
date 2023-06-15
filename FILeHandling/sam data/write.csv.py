import csv
f =open("data.text","w")
cp = csv.writer(f)
cp.writerow(["id","name","salaroy","email"])
f.close()