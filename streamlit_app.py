import streamlit
import pandas
import requests
# import snowflake.connector
from urllib.error import URLError




streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.title('Tea,Coffee,poha,Medu vada')


streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')


streamlit.header('Favorites Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
my_fruit_list=my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
# streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]      # it will gives only avocado and strawberries data
streamlit.dataframe(fruits_to_show)


#import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response)

#streamlit.header("Fruityvice Fruit Advice!")

#import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"kiwi")



# take the json version of the response and normalize it
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it the screen as a table
#streamlit.dataframe(fruityvice_normalized)



streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
fruity_vise_response=requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
fruityvice_normalized = pandas.json_normalize(fruity_vise_response.json())
streamlit.dataframe(fruityvice_normalized)



#import snowflake.connector
#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_data_row = my_cur.fetchone()
#streamlit.text("Hello from Snowflake:")
#streamlit.text(my_data_row)


#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("select * from fruit_load_list")
#my_data_row = my_cur.fetchone()
#streamlit.text("The fruit load list contains:")
#streamlit.text(my_data_row)


#my_data_row = my_cur.fetchone()
#streamlit.header("The fruit load list contains:")
#streamlit.dataframe(my_data_row)


#my_cur.execute("select * from fruit_load_list")
#my_data_rows = my_cur.fetchall()
#streamlit.header("The fruit load list contains:")
#streamlit.dataframe(my_data_rows)


#allow to end user add the fruit to the list
#add_my_fruit = "jackfruit"



#my_cur.execute("select * from fruit_load_list")
#my_data_rows = my_cur.fetchall()
#streamlit.header("The fruit load list contains:")
#streamlit.dataframe(my_data_rows)

#allow to end user to add the fruit to the list
#add_my_fruit = "jackfruit"

#allow to end user to add the fruit to the list
#add_my_fruit = "jackfruit"


#my_cur.execute("select * from fruit_load_list")
#my_data_rows = my_cur.fetchall()
#streamlit.header("The fruit load list contains:")
#streamlit.dataframe(my_data_rows)

fruit_choice = streamlit.text_input('what fruit would you like to add?')
fruity_vise_response=requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
fruityvice_normalized = pandas.json_normalize(fruity_vise_response.json())
streamlit.write('thanks for adding ',fruit_choice)


#This will not work correctly,but just go with it for now
#my_cur.execute("insert into fruit_load_list values('from streamlit')")

#streamlit.header("Fruityvice Fruit Advice!")
#try:
#  fruit_choice = streamlit.text_input('What fruit would you like information about?')
#  if not fruit_choice:
#    streamlit.error("please select a fruit to get information.")
 # else:
 #   fruity_vise_response=requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
  #  fruityvice_normalized = pandas.json_normalize(fruity_vise_response.json())
   # streamlit.dataframe(fruityvice_normalized)
#except URLError as e:
 # streamit.error()
  
  
  #create the repeatable code block (called a function)
  
def get_fruity_vice_data(this_fruit_choice):
  fruity_vise_response=requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruity_vise_response.json())
  return fruityvice_normalized # new section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice')
try:
fruit_choice = streamlit.text_input('What fruit would you like information about?')
#streamlit.write('thanks for adding',fruit_choice)
if not fruit_choice:
  streamlit.error('please select one fruit ')
else:
  back_from_func=get_fruity_vice_data(fruit_choice)
  streamlit.dataframe(back_from_func)
except URLError as e:
  streamlit.error()
