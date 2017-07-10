import pandas
import folium


def get_volcano_color(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation <= 3000:
        return 'orange'
    else:
        return 'red'


def create_map():
    data = pandas.read_csv('python_mega_course_udemy/data/07_volcanoes.txt')

    map = folium.Map(location=[38.58, -99.09], tiles='Mapbox Bright', zoom_start=6)
    volcano_feature_group = folium.FeatureGroup(name='Volcanoes')

    for index, volcano in data.iterrows():
        volcano_feature_group.add_child(
            folium.CircleMarker(
                location=[volcano['LAT'], volcano['LON']],
                color='grey',
                fill_color=get_volcano_color(volcano['ELEV']),
                fill_opacity=0.7,
                radius=8,
                popup=volcano['NAME'] + '<br />Status: ' + volcano['STATUS'] + '\nElevation: ' + str(volcano['ELEV']) + '\ntype: ' + volcano['TYPE']
            )
        )

    population_feature_group = folium.FeatureGroup(name='Population')
    population_feature_group.add_child(folium.GeoJson(data=open('python_mega_course_udemy/data/07_world.json', 'r', encoding='utf-8-sig'),
                                           style_function=country_color_fill))

    map.add_child(volcano_feature_group)
    map.add_child(population_feature_group)
    map.add_child(folium.LayerControl())
    map.save('python_mega_course_udemy/data/07_volcanoes.html')


def country_color_fill(x):
    if x['properties']['POP2005'] < 10000000:
        return {'fillColor': 'green'}
    elif 10000000 <= x['properties']['POP2005'] <= 100000000:
        return {'fillColor': 'orange'}
    else:
        return {'fillColor': 'red'}

if __name__ == "__main__":
    create_map()