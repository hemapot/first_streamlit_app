import streamlit
import pandas as pd
streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Set the index of the DataFrame to the 'Fruit' column
my_fruit_list = my_fruit_list.set_index('Fruit')

# Display the original DataFrame
st.dataframe(my_fruit_list)

# Create a multiselect widget to pick some fruits
fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])

# Filter the original DataFrame to only include the selected fruits
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the DataFrame containing only the selected fruits
st.dataframe(fruits_to_show)
