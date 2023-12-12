#1.  Create a function called create_point_geometry() that accepts two parameters, x_coord and y_coord. The function should return a 
# shapely.geometry.Point geometry object.

from shapely.geometry import Point, LineString, Polygon,base, LinearRing
import matplotlib.pyplot as plt
import fiona
import pandas as pd
import geopandas as gpd


def create_point_geometry(x_coord, y_coord):
    '''This function creates a geometry object Point'''

    point1 = Point(x_coord, y_coord)
    (type(point1)) # printing ths returns the type of geometry object
    return point1


x , y = (2.2), (4.2)

shapely_point = create_point_geometry(x ,y)
shapely_point





# 2. Create a function called create_line_geometry() that takes a list of shapely.geometry.Points as an argument, and returns a 
# shapely.geometry.LineString object of those input points. Validate the function input using assert to check if the argument; 
# 1. is a list  2. contains at least two points  3. that all values are geometry points

def create_line_geometry(list_of_points):
        '''This function creates a geometry object line by combining Points created from the create_point_geometry function above''' 

        # this checks to make sure a list of points is given as the argument
        assert isinstance(list_of_points, list), "The values should be a list of points"

        # this checks if the argument has more than one value of tuple ssets
        assert len(list_of_points) >= 2, "Two or more points make a line, one point is unaccepted"

        # this line of code checks if the arguments are geometry points
        assert (isinstance(point, Point) for point in list_of_points), 'The arguments should be geometry points'

        line = LineString(list_of_points)
        # print(type(line))
        return line
     
    
point1 = (2.2 , 4.3)
point2 = (3.3, 5.2)

line_created = create_line_geometry([point1, point2])
(line_created)




# 3.Create a function create_polygon_geometry that accepts one parameter coordinates. coordinates should be a list of coordinate tuples. 
# The function should create and return a shapely.geometry.Polygon object based on these coordinates. Use assert to check;
# 1. the input is a list  2. the input contains at least three values   3. check all values are tuples and have two coordinates. 

def create_polygon_geometry(coordinates):
    '''This function creates a geometry Polygon object  by combining Points created from the create_point_geometry function above''' 

    assert isinstance(coordinates, list), 'Input sould be a list'

    assert len(coordinates) >=3, 'At minimun three values required to create a polygon'

    assert (isinstance(cords, tuple) and len (cords) == 2 for cords in coordinates), 'The list should be a tuple of two values'

    polygon = Polygon(coordinates)
    (type(polygon))
    return polygon



point1 = (2.2 , 4.3)
point2 = (3.3, 5.2)
point3 = (5.3 , 7.1)

poly1 = create_polygon_geometry([point1, point2, point3])
(poly1)





# 4.Create a function called get_centroid() that accepts one parameter, geom. The function should take any kind of Shapely’s geometry
# objects (any instance of shapely.geometry.base.BaseGeometry) as an input, and return the centroid of that geometry.Make sure to validate the 
# function’s input arguments using assert statements:check that the input is a shapely.geometry.base.BaseGeometry or one of its child classes.
# Otherwise, raise the error "Input must be a shapely geometry".

def get_centroid(geom):
     '''this function return the centroid of any geometry objects'''

     assert isinstance(geom, base.BaseGeometry), "Input must be a shapely geometry"

     object = geom.centroid  #this method calculates the centroid of any geometry object

     return object


shapely_object = poly1  #uses the Polygon geometry object from the create_polygon_geometry function

getting_centroid = get_centroid(shapely_object)
(getting_centroid)

  



    
# 5.Create a function get_area() accepting one parameter polygon.The function should accept a shapely.geometry.Polygon and return its area. 
# Again, use assert to make sure the input values are valid, in particular, check that:the input is a shapely.geometry.Polygon. 
# If the argument is anything else, raise an error: "Input should be a shapely.geometry.Polygon"

def get_area(polygon):
     '''This function calculates the area of a given geometry polygon'''

     assert isinstance(polygon, Polygon), "Input should be a shapely.geometry.Polygon"

     area = polygon.area

     return area

calc_area = get_area(poly1) #again using the Polygon geometry object (poly1) from the create_polygon_geometry function on exercise 3

(f'The area of poly1 is {calc_area:.3f} units')






# 6.Create a function get_length() accepting one parameter, geometry. The function should accept either a shapely.geometry.LineString or a 
# shapely.geometry.Polygon as input. Check the type of the input and return the length of the line if input is a LineString and length of the 
# exterior ring if the input is a Polygon.If something else is passed to the function, raise an error "‘geometry’ should be either a 
# LineString or a Polygon". Use assert or (advanced, optional) raise a ValueError exception.

def get_length(geometry):
     '''this function  calculates the length of an input which should be either a polygon or linestring'''

     assert isinstance(geometry, Polygon) or isinstance(geometry, LineString), "geometry should be either a LineString or a Polygon"

     length_of_object = geometry.length

    #  print(type(geometry))
     return length_of_object

     
     
object = LineString([point1, point2, point3])
length = get_length(object)

#print 
(f'The length is of the {type(object)} is {length:.2f} centimeters' )





# DOCTRINGS OF THE FUNCTION

# functions = [
#     create_point_geometry,
#     create_line_geometry,
#     create_polygon_geometry,
#     get_centroid,
#     get_area,
#     get_length
# ]

# print("My functions:\n")

# for function in functions:
#     # print function name and docstring:
#     print("-", function.__name__ +":", function.__doc__)







# 7.  Create a polygon from a list of coordinates. Two lists, longitudes and latitudes, contain the input coordinates for the polygon. 
# You need to ‘assemble’ the coordinates to individual tuples of one longitude and one latitude coordinate each (The first coordinate pair 
# looks like this: (29.99671173095703, 63.748023986816406)).

longitudes = [29.99671173095703, 31.58196258544922, 27.738052368164062, 26.50013542175293, 26.652359008789062, 25.921663284301758, 22.90027618408203, 23.257217407226562,
           23.335693359375, 22.87444305419922, 23.08465003967285, 22.565473556518555, 21.452774047851562, 21.66388702392578, 21.065969467163086, 21.67659568786621,
           21.496871948242188, 22.339998245239258, 22.288192749023438, 24.539581298828125, 25.444232940673828, 25.303749084472656, 24.669166564941406, 24.689163208007812,
           24.174999237060547, 23.68471908569336, 24.000761032104492, 23.57332992553711, 23.76513671875, 23.430830001831055, 23.6597900390625, 20.580928802490234, 21.320831298828125,
           22.398330688476562, 23.97638702392578, 24.934917449951172, 25.7611083984375, 25.95930290222168, 26.476804733276367, 27.91069221496582, 29.1027774810791, 29.29846954345703,
           28.4355525970459, 28.817358016967773, 28.459857940673828, 30.028610229492188, 29.075136184692383, 30.13492774963379, 29.818885803222656, 29.640830993652344, 30.57735824584961,
           29.99671173095703]

# Latitudes in decimal degrees
latitudes = [63.748023986816406, 62.90789794921875, 60.511383056640625, 60.44499588012695, 60.646385192871094, 60.243743896484375, 59.806800842285156, 59.91944122314453,
           60.02395248413086, 60.14555358886719, 60.3452033996582, 60.211936950683594, 60.56249237060547, 61.54027557373047, 62.59798049926758, 63.02013397216797,
           63.20353698730469, 63.27652359008789, 63.525691986083984, 64.79915618896484, 64.9533920288086, 65.51513671875, 65.65470886230469, 65.89610290527344, 65.79151916503906,
           66.26332092285156, 66.80228424072266, 67.1570053100586, 67.4168701171875, 67.47978210449219, 67.94589233398438, 69.060302734375, 69.32611083984375, 68.71110534667969,
           68.83248901367188, 68.580810546875, 68.98916625976562, 69.68568420410156, 69.9363784790039, 70.08860778808594, 69.70597076416016, 69.48533630371094, 68.90263366699219,
           68.84700012207031, 68.53485107421875, 67.69471740722656, 66.90360260009766, 65.70887756347656, 65.6533203125, 64.92096710205078, 64.22373962402344, 63.748023986816406]



coordinate_pairs = []    #sets an empty list to store a list of tuple sets

for i in range(len(longitudes)):
    coordinate_pairs.append((longitudes[i], latitudes[i]))

polygon = Polygon(coordinate_pairs)  #this line of code creates a geometry polygon from the coordinate_pairs variable 

 



# 8.Insert the polygon into a newly created geopandas.GeoDataFrame called geo. Be sure to define a coordinate reference system for the data 
# (the coordinates are in WGS84 format). Plot the data set. Save the file in GeoPackage format, save it inside the data directory, and name it 
# mysterious-polygon.gpkg.

from geopandas import GeoDataFrame

#  NB:// a geodataframe created should automatically have a geometry column and a crs

# creates a coordinates reference system (WSG84) 
crs = 'EPSG:4326'  

geo = gpd.GeoDataFrame(geometry =[polygon] , crs = crs)  #creates a geodataframe taking a geometry and crs as constant arguments

# print the data frame and crs to check if it has been created
# print(geo) 


# saves the geodataframe file to the laptop directory as a GeoPackage file
saved = r'C:\Users\acer\Documents\projects\learning_gis\mysterious_polygon.gpkg'
save_file = geo.to_file(saved)
save_file






# 9. Our aim is to plot a map of points, based on a set of longitude and latitude coordinates that are stored in a csv file with some_posts.csv.
# Read the data from some_posts.csv into a Pandas dataframe called data. Create an empty column called geometry where you will store shapely 
# Point objects. Insert Point objects into the column geometry based on the coordinate columns.Convert data into a geopandas.GeoDataFrame
#  using its constructor. Make sure that the resulting GeoDataFrame has a coordinate reference system defined. Save the data in Shapefile 
# format as kruger_points.shp inside the data directory. Create a simple map of the points

import pandas as pd

# read the csv data frame in pandas
data = pd.read_csv('Exercises\some_posts.csv')
#printing data will display content of the file into rows and columns
# print(data)

# creates a new column for the geometry and insert shaely  points of each row of the lat and lon column
data['geometry'] = [Point(xy) for xy in zip(data['lat'], data['lon'])]



# convert the dataframe into a geodataframe
crs = 'EPSG: 4326' #set a coordinate reference system for the gdf whch is WGS84

gdf = gpd.GeoDataFrame(data, crs= crs)
# print(gdf.crs)

# saves the geodataframe into a shapefile
output = r'Exercises\kruger_points.shp'
write_files = gdf.to_file(output)
write_files



# let's create a simple map showing the points with matplotlib

# gdf['geometry'].plot(marker='o', color='cyan', markersize=2,)
# plt.title("Kruger national park South Africa  WGS84")
# # plt.xlabel("")
# # plt.ylabel("Latitude")
# plt.show()








# 10.For this, we will need to use the userid column of the data set kruger_posts.shp that we created in Problem 2.
# a. Read the input file kruger_points.shp into a geo-data frame kruger_points. Transform the data from WGS84 to an EPSG:32735 projection
# (UTM Zone 35S, suitable for South Africa). This CRS has metres as units. 
# b. Group the data by userid and store the grouped data in a variable grouped_by_users. 
# c. Create shapely.geometry.LineString objects for each user connecting the points from oldest to most recent.Use a for-loop 
# to iterate over the grouped object. For each user’s data:sort the rows by timestamp. create a shapely.geometry.LineString based on the
# user’s points. Remember that every LineString needs at least two points. Skip users who have less than two posts.
# Store the results in a geopandas.GeoDataFrame called movements, and remember to assign a CRS.
# d. Calculate the distance between all posts of a user. Check once more that the CRS of the data frame is correct. Compute the lengths of the 
# lines, and store it in a new column called distance
# e. What was the shortest distance a user travelled between all their posts (in meters)? (store the value in a variable shortest_distance)
# What was the mean distance travelled per user (in meters)? (store the value in a variable mean_distance)
# What was the maximum distance a user travelled (in meters)? (store the value in a variable longest_distance)
# f. Save the movements into a new Shapefile called movements.shp inside the data directory.


# a. reading the file into the gdf
kp_path = r'C:\Users\acer\Documents\projects\learning_gis\Exercises\kruger_points.shp'  #gets the path of the file to be read

kruger_points = gpd.read_file(kp_path)
print(kruger_points)

# Transform the data from WGS84 to an EPSG:32735 projection
to_utm = kruger_points.to_crs('EPSG:32735')
to_utm.crs   #printing this to conform if it has transformed and print the geometries if the coordinates have changed



# b. grouping data of the userid column 

# showing the unique characters that would be grouped
unique = kruger_points['userid'].unique()

# grouping the userid column
grouped_by_users = kruger_points.groupby('userid')

# printing this just gives the datatype 
# print(grouped_by_users)

# view how the column was grouped with its allocated rows.This appears in a form of dictionary with the unique/group character as the key 
# and the allocated rows as the value
view_grouping = grouped_by_users.groups
#print 
# print(view_grouping)


# grouping the timestamp in decsending order
# kruger_points['timestamp'] = gpd.to_datetime(kruger_points['timestamp'])

geo_line =[]

for user_id, group in grouped_by_users:

    # Sort the rows by timestamp
    group = group.sort_values('timestamp')
    
    # Create LineString only if the user has at least two posts
    if len(group) >= 2:
        points = list(zip(group['lon'], group['lat']))
        # print(points)
        line = LineString(points)
        
        # appends each user and their corresponding linestring. Creating a new gdf from scratch, create a dictionary of your column name
        # and the values 
        geo_line.append({'user_id' : user_id, 'geometry' : line})

# print(geo_line)      



from geopandas import GeoDataFrame

# stores linestrings as a geodataframe
movements = gpd.GeoDataFrame(geo_line, crs = 'EPSG:32735')
# print(movements)

# checks if the crs is the same
movements.crs



# create a new column names distance that calculates length of each linestring
movements['Distance'] = movements['geometry'].length


# calculate the shortest distance

shortest_distance = movements['Distance'].min()
(f'The shortest distance traveled was  {shortest_distance} meters')


# calculate the mean distance travelled
mean_distance = movements['Distance'].mean()
(f'The mean distance travelled was {mean_distance} meters')


# calculate the longest distance travelled
longest_distance = movements['Distance'].max()
(f'The longest distance travelled was {longest_distance} meters')




# Save the movements into a new Shapefile called movements.shp 

saving_movement = movements.to_file(r'C:\Users\acer\Documents\projects\learning_gis\Exercises\movements.shp')
# print(saving_movement)








