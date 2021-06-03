import pandas as pd
import plotly_express as pl

#csv_data = pd.read_csv('./files/data/line_chart.csv')
#csv_data = pd.read_csv('./files/data/data.csv')
csv_data = pd.read_csv('./files/data/cereal_data.csv')

#fig = pl.line(csv_data, x= "Year", y="Per capita income", color="Country", title="Change of Capital Income Per Country")
#fig = pl.bar(csv_data, x= "Country", y="InternetUsers")
#fig = pl.scatter(csv_data, x= "Population", y="Per capita", size="Percentage", color="Country", size_max=60)
#fig = pl.scatter(csv_data, x= "sugars", y="rating", hover_name="name", title="Cereal Ratings vs Sugars")
#fig = pl.histogram(csv_data, x="rating", title="Cereal Ratings")
#fig = pl.scatter(csv_data, x= "sugars", y="rating", size="calories", color= "mfr", hover_name="name", facet_row="shelf", facet_col= "type", title="Cereal Ratings vs Sugars")
#fig = pl.treemap(csv_data, path=["shelf", "mfr"], title="Cereals By Shelf Location")
#fig = pl.sunburst(csv_data, path=["shelf", "mfr"], title="Cereals By Shelf Location")
#fig.write_image("shelf_data.jpg", scale= 0.75)

fig.show()

