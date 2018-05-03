#################################################################
## We need Altair, Pandas,
#################################################################
import altair as alt
import pandas as pd


def filtrame(zipcode):
    RESTAURANT_URL      = "https://raw.githubusercontent.com/hvo/datasets/master/nyc_restaurants_by_cuisine.json"
    data = pd.read_json(RESTAURANT_URL)
    if str(zipcode) in data.perZip.apply(pd.Series).columns:
        quantity=data.perZip.apply(pd.Series)[zipcode].sort_values(ascending=False)[:25] #this creates a new dataframe of quantities in the zipcode
        cuisine=data["cuisine"][data.perZip.apply(pd.Series)[zipcode].sort_values(ascending=False)[:25].index]
        data=pd.concat([cuisine,quantity],axis=1)
        data.columns=["cuisine","total"]
        return data
    else:
        data=pd.DataFrame(columns=["cuisine","total"])
        return data

def createchart(data):

    #color_expression    = "(indexof(lower(datum.cuisine)) || (highlight._vgsid_==datum._vgsid_)"
    #color_condition     = alt.ConditionalPredicateValueDef(color_expression, "SteelBlue")
    #highlight_selection = alt.selection_single(name="highlight", on="mouseover", empty="none")
    #search_selection    = alt.selection_single(name="search", on="mouseover", empty="none", fields=["term"],
                                               #bind=alt.VgGenericBinding('input'))

    chart = alt.Chart(data) \
        .mark_bar(stroke="Black") \
        .encode(
            alt.X("total:Q", axis=alt.Axis(title="Restaurants")),
            alt.Y('cuisine:O', sort=alt.SortField(field="total", op="argmax")),
            alt.ColorValue("LightGrey"),
        )

    return chart