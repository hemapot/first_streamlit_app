import streamlit as st
import pandas as pd
import numpy as np
#import plost
#from PIL import Image
import folium
from streamlit_folium import st_folium


# Page setting
st.set_page_config(layout="wide")

#********************************************************************
# HOME PAGE
def home_page():
    #    image_url = "https://upload.wikimedia.org/wikipedia/commons/9/94/Department_of_Justice_and_Community_Safety.png"
    st.image('https://upload.wikimedia.org/wikipedia/commons/9/94/Department_of_Justice_and_Community_Safety.png', width=250)
    st.title("FBAN Auto-Fill Tool Demo")
    st.header("The FBAN Briefing Auto-Fill Tool provides the State Control Centre (SCC) and Regional Control Centres (RCCs) with a three-day fire risk forecast at the ICC and RCC level to inform planning and decision making.")
    st.subheader("Please use the side menu to navigate.")
    st.text("Designed and built by [INSERT NAME AND TEAM HERE].")


#*********************************************************************
#HOW TO GUIDE PAGE
def how_to_guide_page():
    st.title("FBAN Auto-Fill Tool Demo")
    st.header ('How to Guide')
    st.text('Last updated <24 hour time> on <day> <date> <month> <year>')
    st.header('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')

    
#*********************************************************************
#FAQ PAGE
def FAQ_page():
    st.title("FBAN Auto-Fill Tool Demo")
    st.header ('Frequently Asked Questions')
    st.text('Last updated <24 hour time> on <day> <date> <month> <year>')
    st.header('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
    
#*********************************************************************
#BARWON SOUTH WEST PAGE
def barwon_south_west_page():
    st.title("FBAN Auto-Fill Tool Demo")
    st.header ('Region: Barwon South West')
    st.text('Last updated <24 hour time> on <day> <date> <month> <year>')
    #BSW Commentary
    a1, a2, a3 = st.columns(3)
    with a1:
        #st.text_input("Tomorrow:", value="", max_chars=500, type="default", placeholder="Type your commentary here", disabled=False, label_visibility="visible")
        st.text_area("Tomorrow:", value="", height=200, max_chars=500, placeholder="Type your commentary here", disabled=False, label_visibility="visible")
    
    with a2:
        #st.text_input("<Two days time>:", value="", max_chars=500, type="default", placeholder="Type your commentary here", disabled=False, label_visibility="visible")
        st.text_area("<Two days time>:", value="", height=200, max_chars=500, placeholder="Type your commentary here", disabled=False, label_visibility="visible")
        
    with a3:
        #st.text_input("<Three days time>:", value="", max_chars=500, type="default", placeholder="Type your commentary here", disabled=False, label_visibility="visible")
        st.text_area("<Three days time>:", value="", height=200, max_chars=500, placeholder="Type your commentary here", disabled=False, label_visibility="visible")
    # Dummy data - pre-poulated
    
    dummy_data = {
        'ICC': ['Heywood', 'Heywood', 'Heywood', 'Warrnambool', 'Warrnambool', 'Warrnambool', 'Colac', 'Colac', 'Colac'],
        'Day': ['Tommorrow', '<Two days time>', '<Three days time>', 'Tommorrow', '<Two days time>', '<Three days time>', 'Tommorrow', '<Two days time>', '<Three days time>'],
        'Confidence level': ['90', '80', '70', '90', '80', '70', '90', '80', '70'],
        'Fuel Type Driver': ['Grass', 'Forest', 'Mallee', 'Pine', 'Grass', 'Forest', 'Mallee', 'Pine', 'Mallee'],
        'FBI': ['Moderate', 'High', 'Extreme', 'Moderate', 'High', 'Extreme', 'Moderate', 'High', 'Extreme'],
        'FDI': ['Low-Moderate', 'High', 'Very High', 'Low-Moderate', 'High', 'Very High', 'Low-Moderate', 'High', 'Very High'],
        'Wind Change': ['Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes'],
        'Ignitability': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
        'Max Duration': ['<2hrs', '2-6hrs', '>6hrs', '<2hrs', '2-6hrs', '>6hrs', '<2hrs', '2-6hrs', '>6hrs'],
        'Min to 5ha': ['<15 min', '15-30 min', '30 min', '<15 min', '15-30 min', '30 min', '<15 min', '15-30 min', '30 min'],
        'FDP': ['Nil', 'Partial', 'Total', 'Nil', 'Partial', 'Total', 'Nil', 'Partial', 'Total'],            
        'Lightning': ['Yes', 'Partial', 'No', 'Yes', 'Partial', 'No', 'Yes', 'Partial', 'No'],
        'Harvest remaining': ['100', '50', '0', '100', '50', '0', '100', '50', '0']
        }
    
    df2 = pd.DataFrame(dummy_data)

    column_configuration = {
        "Confidence level": st.column_config.TextColumn(
            "Confidence level", help="FBAN confidence level", default="Update", max_chars=100
        ),
        "Fuel Type Driver": st.column_config.SelectboxColumn(
            "Fuel Type Driver", default="Select", options=["Forest", "Grass", "Mallee", "Pine", "Forest, Grass", "Grass, Mallee", "Mallee, Pine", "Forest, Pine", "Forest, Grass, Mallee", "Forest, Grass, Pine","Grass, Mallee, Pine", "Forest, Mallee, Pine", "Forest, Grass, Mallee, Pine"]
        ),
        "Wind Change": st.column_config.SelectboxColumn(
            "Wind Change", default="Select", options=["Yes", "No"]
        ),
        "Max Duration": st.column_config.SelectboxColumn(
            "Max Duration", default="Select", options=["<2hrs", "2-6hrs", ">6hrs"]
        ),
        "Min to 5ha": st.column_config.SelectboxColumn(
            "Min to 5ha", default="Select", options=["<15 min", "15-30 min", ">30min", ">60 min"]
        ),
        "Harvest remaining": st.column_config.ProgressColumn(
            "Harvest remaining", min_value=0, max_value=100, format="%g%%\n"
        ),
    }
        
    st.data_editor(
        df2,
        column_config=column_configuration,
        use_container_width=True,
        hide_index=True,
        num_rows="fixed",
    )

#*********************************************************************
#GRAMPIANS PAGE

def grampians_page():
    st.title("FBAN Auto-Fill Tool Demo")
    st.header ('Region: Grampians')
    st.text('Last updated <24 hour time> on <day> <date> <month> <year>')
      
    #Commentary
        
    a1, a2, a3 = st.columns(3)
    with a1:
        #st.text_input("Tomorrow:", value="", max_chars=500, type="default", placeholder="Type your commentary here", disabled=False, label_visibility="visible")
        st.text_area("Tomorrow:", value="", height=200, max_chars=500, placeholder="Type your commentary here", disabled=False, label_visibility="visible")
        
    with a2:
        #st.text_input("<Two days time>:", value="", max_chars=500, type="default", placeholder="Type your commentary here", disabled=False, label_visibility="visible")
        st.text_area("<Two days time>:", value="", height=200, max_chars=500, placeholder="Type your commentary here", disabled=False, label_visibility="visible")
            
    with a3:
        #st.text_input("<Three days time>:", value="", max_chars=500, type="default", placeholder="Type your commentary here", disabled=False, label_visibility="visible")
        st.text_area("<Three days time>:", value="", height=200, max_chars=500, placeholder="Type your commentary here", disabled=False, label_visibility="visible")
        
      
    # Style of non-editable table - NEED TO EDIT THIS ONE
    header_style = '''
        <style>
            thead{
                background-color: #C6E8F6;
                color: #FFFFFF;
                }
        </style>
    '''
    st.markdown(header_style, unsafe_allow_html=True)
         
                
    # Dummy data - pre-poulated
        
    dummy_data = {
            'ICC': ['Heywood', 'Heywood', 'Heywood', 'Warrnambool', 'Warrnambool', 'Warrnambool', 'Colac', 'Colac', 'Colac'],
            'Day': ['Tommorrow', '<Two days time>', '<Three days time>', 'Tommorrow', '<Two days time>', '<Three days time>', 'Tommorrow', '<Two days time>', '<Three days time>'],
            'Confidence level': ['90', '80', '70', '90', '80', '70', '90', '80', '70'],
            'Fuel Type Driver': ['Grass', 'Forest', 'Mallee', 'Pine', 'Grass', 'Forest', 'Mallee', 'Pine', 'Mallee'],
            'FBI': ['Moderate', 'High', 'Extreme', 'Moderate', 'High', 'Extreme', 'Moderate', 'High', 'Extreme'],
            'FDI': ['Low-Moderate', 'High', 'Very High', 'Low-Moderate', 'High', 'Very High', 'Low-Moderate', 'High', 'Very High'],
            'Wind Change': ['Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes'],
            'Ignitability': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
            'Max Duration': ['<2hrs', '2-6hrs', '>6hrs', '<2hrs', '2-6hrs', '>6hrs', '<2hrs', '2-6hrs', '>6hrs'],
            'Min to 5ha': ['<15 min', '15-30 min', '30 min', '<15 min', '15-30 min', '30 min', '<15 min', '15-30 min', '30 min'],
            'FDP': ['Nil', 'Partial', 'Total', 'Nil', 'Partial', 'Total', 'Nil', 'Partial', 'Total'],            
            'Lightning': ['Yes', 'Partial', 'No', 'Yes', 'Partial', 'No', 'Yes', 'Partial', 'No'],
            'Harvest remaining': ['100', '50', '0', '100', '50', '0', '100', '50', '0']
            }
        
    df2 = pd.DataFrame(dummy_data)
        
      
    #TRIALLING DIFFERENT FORMAT CODE FOR TABLE CONFIG
        
    column_configuration = {
        "Confidence level": st.column_config.TextColumn(
            "Confidence level", help="FBAN confidence level", default="Update", max_chars=100
        ),
        "Fuel Type Driver": st.column_config.SelectboxColumn(
            "Fuel Type Driver", default="Select", options=["Forest", "Grass", "Mallee", "Pine", "Forest, Grass", "Grass, Mallee", "Mallee, Pine", "Forest, Pine", "Forest, Grass, Mallee", "Forest, Grass, Pine","Grass, Mallee, Pine", "Forest, Mallee, Pine", "Forest, Grass, Mallee, Pine"]
        ),
        "Wind Change": st.column_config.SelectboxColumn(
            "Wind Change", default="Select", options=["Yes", "No"]
        ),
        "Max Duration": st.column_config.SelectboxColumn(
            "Max Duration", default="Select", options=["<2hrs", "2-6hrs", ">6hrs"]
        ),
        "Min to 5ha": st.column_config.SelectboxColumn(
            "Min to 5ha", default="Select", options=["<15 min", "15-30 min", ">30min", ">60 min"]
        ),
        "Harvest remaining": st.column_config.ProgressColumn(
            "Harvest remaining", min_value=0, max_value=100, format="%g%%\n"
        ),
    }
        
    st.data_editor(
        df2,
        column_config=column_configuration,
        use_container_width=True,
        hide_index=True,
        num_rows="fixed",
    )


#*********************************************************************
# LODDON MALLEE PAGE

def loddon_mallee_page():
    st.title("FBAN Auto-Fill Tool Demo")
    st.header ('Region: Loddon Mallee')
    st.text('Last updated <24 hour time> on <day> <date> <month> <year>')
    
    #COMMENTARY
        
    a1, a2, a3 = st.columns(3)
    with a1:
        #st.text_input("Tomorrow:", value="", max_chars=500, type="default", placeholder="Type your commentary here", disabled=False, label_visibility="visible")
        st.text_area("Tomorrow:", value="", height=200, max_chars=500, placeholder="Type your commentary here", disabled=False, label_visibility="visible")
        
    with a2:
        #st.text_input("<Two days time>:", value="", max_chars=500, type="default", placeholder="Type your commentary here", disabled=False, label_visibility="visible")
        st.text_area("<Two days time>:", value="", height=200, max_chars=500, placeholder="Type your commentary here", disabled=False, label_visibility="visible")
            
    with a3:
        #st.text_input("<Three days time>:", value="", max_chars=500, type="default", placeholder="Type your commentary here", disabled=False, label_visibility="visible")
        st.text_area("<Three days time>:", value="", height=200, max_chars=500, placeholder="Type your commentary here", disabled=False, label_visibility="visible")
        
    #DUMMY DATA
        
    dummy_data = {
            'ICC': ['Heywood', 'Heywood', 'Heywood', 'Warrnambool', 'Warrnambool', 'Warrnambool', 'Colac', 'Colac', 'Colac'],
            'Day': ['Tommorrow', '<Two days time>', '<Three days time>', 'Tommorrow', '<Two days time>', '<Three days time>', 'Tommorrow', '<Two days time>', '<Three days time>'],
            'Confidence level': ['90', '80', '70', '90', '80', '70', '90', '80', '70'],
            'Fuel Type Driver': ['Grass', 'Forest', 'Mallee', 'Pine', 'Grass', 'Forest', 'Mallee', 'Pine', 'Mallee'],
            'FBI': ['Moderate', 'High', 'Extreme', 'Moderate', 'High', 'Extreme', 'Moderate', 'High', 'Extreme'],
            'FDI': ['Low-Moderate', 'High', 'Very High', 'Low-Moderate', 'High', 'Very High', 'Low-Moderate', 'High', 'Very High'],
            'Wind Change': ['Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes'],
            'Ignitability': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
            'Max Duration': ['<2hrs', '2-6hrs', '>6hrs', '<2hrs', '2-6hrs', '>6hrs', '<2hrs', '2-6hrs', '>6hrs'],
            'Min to 5ha': ['<15 min', '15-30 min', '30 min', '<15 min', '15-30 min', '30 min', '<15 min', '15-30 min', '30 min'],
            'FDP': ['Nil', 'Partial', 'Total', 'Nil', 'Partial', 'Total', 'Nil', 'Partial', 'Total'],            
            'Lightning': ['Yes', 'Partial', 'No', 'Yes', 'Partial', 'No', 'Yes', 'Partial', 'No'],
            'Harvest remaining': ['100', '50', '0', '100', '50', '0', '100', '50', '0']
            }
        
    df2 = pd.DataFrame(dummy_data)
        
      
   #MAIN TABLE
        
    column_configuration = {
        "Confidence level": st.column_config.TextColumn(
            "Confidence level", help="FBAN confidence level", default="Update", max_chars=100
        ),
        "Fuel Type Driver": st.column_config.SelectboxColumn(
            "Fuel Type Driver", default="Select", options=["Forest", "Grass", "Mallee", "Pine", "Forest, Grass", "Grass, Mallee", "Mallee, Pine", "Forest, Pine", "Forest, Grass, Mallee", "Forest, Grass, Pine","Grass, Mallee, Pine", "Forest, Mallee, Pine", "Forest, Grass, Mallee, Pine"]
        ),
        "Wind Change": st.column_config.SelectboxColumn(
            "Wind Change", default="Select", options=["Yes", "No"]
        ),
        "Max Duration": st.column_config.SelectboxColumn(
            "Max Duration", default="Select", options=["<2hrs", "2-6hrs", ">6hrs"]
        ),
        "Min to 5ha": st.column_config.SelectboxColumn(
            "Min to 5ha", default="Select", options=["<15 min", "15-30 min", ">30min", ">60 min"]
        ),
        "Harvest remaining": st.column_config.ProgressColumn(
            "Harvest remaining", min_value=0, max_value=100, format="%g%%\n"
        ),
    }
        
    st.data_editor(
        df2,
        column_config=column_configuration,
        use_container_width=True,
        hide_index=True,
        num_rows="fixed",
    )

#*********************************************************************
# EASTERN METRO PAGE

def eastern_metro_page():
    st.title("FBAN Auto-Fill Tool Demo")
    st.header ('Region: Eastern Metro')
    st.text('Last updated <24 hour time> on <day> <date> <month> <year>')
    #COMMENTARY
        
    a1, a2, a3 = st.columns(3)
    with a1:
        #st.text_input("Tomorrow:", value="", max_chars=500, type="default", placeholder="Type your commentary here", disabled=False, label_visibility="visible")
        st.text_area("Tomorrow:", value="", height=200, max_chars=500, placeholder="Type your commentary here", disabled=False, label_visibility="visible")
        
    with a2:
        #st.text_input("<Two days time>:", value="", max_chars=500, type="default", placeholder="Type your commentary here", disabled=False, label_visibility="visible")
        st.text_area("<Two days time>:", value="", height=200, max_chars=500, placeholder="Type your commentary here", disabled=False, label_visibility="visible")
            
    with a3:
        #st.text_input("<Three days time>:", value="", max_chars=500, type="default", placeholder="Type your commentary here", disabled=False, label_visibility="visible")
        st.text_area("<Three days time>:", value="", height=200, max_chars=500, placeholder="Type your commentary here", disabled=False, label_visibility="visible")
        
    #DUMMY DATA
        
    dummy_data = {
            'ICC': ['Heywood', 'Heywood', 'Heywood', 'Warrnambool', 'Warrnambool', 'Warrnambool', 'Colac', 'Colac', 'Colac'],
            'Day': ['Tommorrow', '<Two days time>', '<Three days time>', 'Tommorrow', '<Two days time>', '<Three days time>', 'Tommorrow', '<Two days time>', '<Three days time>'],
            'Confidence level': ['90', '80', '70', '90', '80', '70', '90', '80', '70'],
            'Fuel Type Driver': ['Grass', 'Forest', 'Mallee', 'Pine', 'Grass', 'Forest', 'Mallee', 'Pine', 'Mallee'],
            'FBI': ['Moderate', 'High', 'Extreme', 'Moderate', 'High', 'Extreme', 'Moderate', 'High', 'Extreme'],
            'FDI': ['Low-Moderate', 'High', 'Very High', 'Low-Moderate', 'High', 'Very High', 'Low-Moderate', 'High', 'Very High'],
            'Wind Change': ['Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes'],
            'Ignitability': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
            'Max Duration': ['<2hrs', '2-6hrs', '>6hrs', '<2hrs', '2-6hrs', '>6hrs', '<2hrs', '2-6hrs', '>6hrs'],
            'Min to 5ha': ['<15 min', '15-30 min', '30 min', '<15 min', '15-30 min', '30 min', '<15 min', '15-30 min', '30 min'],
            'FDP': ['Nil', 'Partial', 'Total', 'Nil', 'Partial', 'Total', 'Nil', 'Partial', 'Total'],            
            'Lightning': ['Yes', 'Partial', 'No', 'Yes', 'Partial', 'No', 'Yes', 'Partial', 'No'],
            'Harvest remaining': ['100', '50', '0', '100', '50', '0', '100', '50', '0']
            }
        
    df2 = pd.DataFrame(dummy_data)
        
      
   #MAIN TABLE
        
    column_configuration = {
        "Confidence level": st.column_config.TextColumn(
            "Confidence level", help="FBAN confidence level", default="Update", max_chars=100
        ),
        "Fuel Type Driver": st.column_config.SelectboxColumn(
            "Fuel Type Driver", default="Select", options=["Forest", "Grass", "Mallee", "Pine", "Forest, Grass", "Grass, Mallee", "Mallee, Pine", "Forest, Pine", "Forest, Grass, Mallee", "Forest, Grass, Pine","Grass, Mallee, Pine", "Forest, Mallee, Pine", "Forest, Grass, Mallee, Pine"]
        ),
        "Wind Change": st.column_config.SelectboxColumn(
            "Wind Change", default="Select", options=["Yes", "No"]
        ),
        "Max Duration": st.column_config.SelectboxColumn(
            "Max Duration", default="Select", options=["<2hrs", "2-6hrs", ">6hrs"]
        ),
        "Min to 5ha": st.column_config.SelectboxColumn(
            "Min to 5ha", default="Select", options=["<15 min", "15-30 min", ">30min", ">60 min"]
        ),
        "Harvest remaining": st.column_config.ProgressColumn(
            "Harvest remaining", min_value=0, max_value=100, format="%g%%\n"
        ),
    }
        
    st.data_editor(
        df2,
        column_config=column_configuration,
        use_container_width=True,
        hide_index=True,
        num_rows="fixed",
    )

#*********************************************************************
# SOUTHERN METRO PAGE

def southern_metro_page():
    st.title("FBAN Auto-Fill Tool Demo")
    st.header ('Region: Southern Metro')
    st.text('Last updated <24 hour time> on <day> <date> <month> <year>')
    #COMMENTARY
        
    a1, a2, a3 = st.columns(3)
    with a1:
        #st.text_input("Tomorrow:", value="", max_chars=500, type="default", placeholder="Type your commentary here", disabled=False, label_visibility="visible")
        st.text_area("Tomorrow:", value="", height=200, max_chars=500, placeholder="Type your commentary here", disabled=False, label_visibility="visible")
        
    with a2:
        #st.text_input("<Two days time>:", value="", max_chars=500, type="default", placeholder="Type your commentary here", disabled=False, label_visibility="visible")
        st.text_area("<Two days time>:", value="", height=200, max_chars=500, placeholder="Type your commentary here", disabled=False, label_visibility="visible")
            
    with a3:
        #st.text_input("<Three days time>:", value="", max_chars=500, type="default", placeholder="Type your commentary here", disabled=False, label_visibility="visible")
        st.text_area("<Three days time>:", value="", height=200, max_chars=500, placeholder="Type your commentary here", disabled=False, label_visibility="visible")
        
    #DUMMY DATA
        
    dummy_data = {
            'ICC': ['Heywood', 'Heywood', 'Heywood', 'Warrnambool', 'Warrnambool', 'Warrnambool', 'Colac', 'Colac', 'Colac'],
            'Day': ['Tommorrow', '<Two days time>', '<Three days time>', 'Tommorrow', '<Two days time>', '<Three days time>', 'Tommorrow', '<Two days time>', '<Three days time>'],
            'Confidence level': ['90', '80', '70', '90', '80', '70', '90', '80', '70'],
            'Fuel Type Driver': ['Grass', 'Forest', 'Mallee', 'Pine', 'Grass', 'Forest', 'Mallee', 'Pine', 'Mallee'],
            'FBI': ['Moderate', 'High', 'Extreme', 'Moderate', 'High', 'Extreme', 'Moderate', 'High', 'Extreme'],
            'FDI': ['Low-Moderate', 'High', 'Very High', 'Low-Moderate', 'High', 'Very High', 'Low-Moderate', 'High', 'Very High'],
            'Wind Change': ['Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes'],
            'Ignitability': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
            'Max Duration': ['<2hrs', '2-6hrs', '>6hrs', '<2hrs', '2-6hrs', '>6hrs', '<2hrs', '2-6hrs', '>6hrs'],
            'Min to 5ha': ['<15 min', '15-30 min', '30 min', '<15 min', '15-30 min', '30 min', '<15 min', '15-30 min', '30 min'],
            'FDP': ['Nil', 'Partial', 'Total', 'Nil', 'Partial', 'Total', 'Nil', 'Partial', 'Total'],            
            'Lightning': ['Yes', 'Partial', 'No', 'Yes', 'Partial', 'No', 'Yes', 'Partial', 'No'],
            'Harvest remaining': ['100', '50', '0', '100', '50', '0', '100', '50', '0']
            }
        
    df2 = pd.DataFrame(dummy_data)
        
      
   #MAIN TABLE
        
    column_configuration = {
        "Confidence level": st.column_config.TextColumn(
            "Confidence level", help="FBAN confidence level", default="Update", max_chars=100
        ),
        "Fuel Type Driver": st.column_config.SelectboxColumn(
            "Fuel Type Driver", default="Select", options=["Forest", "Grass", "Mallee", "Pine", "Forest, Grass", "Grass, Mallee", "Mallee, Pine", "Forest, Pine", "Forest, Grass, Mallee", "Forest, Grass, Pine","Grass, Mallee, Pine", "Forest, Mallee, Pine", "Forest, Grass, Mallee, Pine"]
        ),
        "Wind Change": st.column_config.SelectboxColumn(
            "Wind Change", default="Select", options=["Yes", "No"]
        ),
        "Max Duration": st.column_config.SelectboxColumn(
            "Max Duration", default="Select", options=["<2hrs", "2-6hrs", ">6hrs"]
        ),
        "Min to 5ha": st.column_config.SelectboxColumn(
            "Min to 5ha", default="Select", options=["<15 min", "15-30 min", ">30min", ">60 min"]
        ),
        "Harvest remaining": st.column_config.ProgressColumn(
            "Harvest remaining", min_value=0, max_value=100, format="%g%%\n"
        ),
    }
        
    st.data_editor(
        df2,
        column_config=column_configuration,
        use_container_width=True,
        hide_index=True,
        num_rows="fixed",
    )

#*********************************************************************
# HUME PAGE

def hume_page():
    st.title("FBAN Auto-Fill Tool Demo")
    st.header ('Region: Hume')
    st.text('Last updated <24 hour time> on <day> <date> <month> <year>')
    #COMMENTARY
        
    a1, a2, a3 = st.columns(3)
    with a1:
        #st.text_input("Tomorrow:", value="", max_chars=500, type="default", placeholder="Type your commentary here", disabled=False, label_visibility="visible")
        st.text_area("Tomorrow:", value="", height=200, max_chars=500, placeholder="Type your commentary here", disabled=False, label_visibility="visible")
        
    with a2:
        #st.text_input("<Two days time>:", value="", max_chars=500, type="default", placeholder="Type your commentary here", disabled=False, label_visibility="visible")
        st.text_area("<Two days time>:", value="", height=200, max_chars=500, placeholder="Type your commentary here", disabled=False, label_visibility="visible")
            
    with a3:
        #st.text_input("<Three days time>:", value="", max_chars=500, type="default", placeholder="Type your commentary here", disabled=False, label_visibility="visible")
        st.text_area("<Three days time>:", value="", height=200, max_chars=500, placeholder="Type your commentary here", disabled=False, label_visibility="visible")
        
    #DUMMY DATA
        
    dummy_data = {
            'ICC': ['Heywood', 'Heywood', 'Heywood', 'Warrnambool', 'Warrnambool', 'Warrnambool', 'Colac', 'Colac', 'Colac'],
            'Day': ['Tommorrow', '<Two days time>', '<Three days time>', 'Tommorrow', '<Two days time>', '<Three days time>', 'Tommorrow', '<Two days time>', '<Three days time>'],
            'Confidence level': ['90', '80', '70', '90', '80', '70', '90', '80', '70'],
            'Fuel Type Driver': ['Grass', 'Forest', 'Mallee', 'Pine', 'Grass', 'Forest', 'Mallee', 'Pine', 'Mallee'],
            'FBI': ['Moderate', 'High', 'Extreme', 'Moderate', 'High', 'Extreme', 'Moderate', 'High', 'Extreme'],
            'FDI': ['Low-Moderate', 'High', 'Very High', 'Low-Moderate', 'High', 'Very High', 'Low-Moderate', 'High', 'Very High'],
            'Wind Change': ['Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes'],
            'Ignitability': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
            'Max Duration': ['<2hrs', '2-6hrs', '>6hrs', '<2hrs', '2-6hrs', '>6hrs', '<2hrs', '2-6hrs', '>6hrs'],
            'Min to 5ha': ['<15 min', '15-30 min', '30 min', '<15 min', '15-30 min', '30 min', '<15 min', '15-30 min', '30 min'],
            'FDP': ['Nil', 'Partial', 'Total', 'Nil', 'Partial', 'Total', 'Nil', 'Partial', 'Total'],            
            'Lightning': ['Yes', 'Partial', 'No', 'Yes', 'Partial', 'No', 'Yes', 'Partial', 'No'],
            'Harvest remaining': ['100', '50', '0', '100', '50', '0', '100', '50', '0']
            }
        
    df2 = pd.DataFrame(dummy_data)
        
      
   #MAIN TABLE
        
    column_configuration = {
        "Confidence level": st.column_config.TextColumn(
            "Confidence level", help="FBAN confidence level", default="Update", max_chars=100
        ),
        "Fuel Type Driver": st.column_config.SelectboxColumn(
            "Fuel Type Driver", default="Select", options=["Forest", "Grass", "Mallee", "Pine", "Forest, Grass", "Grass, Mallee", "Mallee, Pine", "Forest, Pine", "Forest, Grass, Mallee", "Forest, Grass, Pine","Grass, Mallee, Pine", "Forest, Mallee, Pine", "Forest, Grass, Mallee, Pine"]
        ),
        "Wind Change": st.column_config.SelectboxColumn(
            "Wind Change", default="Select", options=["Yes", "No"]
        ),
        "Max Duration": st.column_config.SelectboxColumn(
            "Max Duration", default="Select", options=["<2hrs", "2-6hrs", ">6hrs"]
        ),
        "Min to 5ha": st.column_config.SelectboxColumn(
            "Min to 5ha", default="Select", options=["<15 min", "15-30 min", ">30min", ">60 min"]
        ),
        "Harvest remaining": st.column_config.ProgressColumn(
            "Harvest remaining", min_value=0, max_value=100, format="%g%%\n"
        ),
    }
        
    st.data_editor(
        df2,
        column_config=column_configuration,
        use_container_width=True,
        hide_index=True,
        num_rows="fixed",
    )

#*********************************************************************
# GIPPSLAND PAGE

def gippsland_page():
    st.title("FBAN Auto-Fill Tool Demo")
    st.header ('Region: Gippsland')
    st.text('Last updated <24 hour time> on <day> <date> <month> <year>')
    #COMMENTARY
        
    a1, a2, a3 = st.columns(3)
    with a1:
        #st.text_input("Tomorrow:", value="", max_chars=500, type="default", placeholder="Type your commentary here", disabled=False, label_visibility="visible")
        st.text_area("Tomorrow:", value="", height=200, max_chars=500, placeholder="Type your commentary here", disabled=False, label_visibility="visible")
        
    with a2:
        #st.text_input("<Two days time>:", value="", max_chars=500, type="default", placeholder="Type your commentary here", disabled=False, label_visibility="visible")
        st.text_area("<Two days time>:", value="", height=200, max_chars=500, placeholder="Type your commentary here", disabled=False, label_visibility="visible")
            
    with a3:
        #st.text_input("<Three days time>:", value="", max_chars=500, type="default", placeholder="Type your commentary here", disabled=False, label_visibility="visible")
        st.text_area("<Three days time>:", value="", height=200, max_chars=500, placeholder="Type your commentary here", disabled=False, label_visibility="visible")
        
    #DUMMY DATA
        
    dummy_data = {
            'ICC': ['Heywood', 'Heywood', 'Heywood', 'Warrnambool', 'Warrnambool', 'Warrnambool', 'Colac', 'Colac', 'Colac'],
            'Day': ['Tommorrow', '<Two days time>', '<Three days time>', 'Tommorrow', '<Two days time>', '<Three days time>', 'Tommorrow', '<Two days time>', '<Three days time>'],
            'Confidence level': ['90', '80', '70', '90', '80', '70', '90', '80', '70'],
            'Fuel Type Driver': ['Grass', 'Forest', 'Mallee', 'Pine', 'Grass', 'Forest', 'Mallee', 'Pine', 'Mallee'],
            'FBI': ['Moderate', 'High', 'Extreme', 'Moderate', 'High', 'Extreme', 'Moderate', 'High', 'Extreme'],
            'FDI': ['Low-Moderate', 'High', 'Very High', 'Low-Moderate', 'High', 'Very High', 'Low-Moderate', 'High', 'Very High'],
            'Wind Change': ['Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes'],
            'Ignitability': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C'],
            'Max Duration': ['<2hrs', '2-6hrs', '>6hrs', '<2hrs', '2-6hrs', '>6hrs', '<2hrs', '2-6hrs', '>6hrs'],
            'Min to 5ha': ['<15 min', '15-30 min', '30 min', '<15 min', '15-30 min', '30 min', '<15 min', '15-30 min', '30 min'],
            'FDP': ['Nil', 'Partial', 'Total', 'Nil', 'Partial', 'Total', 'Nil', 'Partial', 'Total'],            
            'Lightning': ['Yes', 'Partial', 'No', 'Yes', 'Partial', 'No', 'Yes', 'Partial', 'No'],
            'Harvest remaining': ['100', '50', '0', '100', '50', '0', '100', '50', '0']
            }
        
    df2 = pd.DataFrame(dummy_data)
        
      
   #MAIN TABLE
        
    column_configuration = {
        "Confidence level": st.column_config.TextColumn(
            "Confidence level", help="FBAN confidence level", default="Update", max_chars=100
        ),
        "Fuel Type Driver": st.column_config.SelectboxColumn(
            "Fuel Type Driver", default="Select", options=["Forest", "Grass", "Mallee", "Pine", "Forest, Grass", "Grass, Mallee", "Mallee, Pine", "Forest, Pine", "Forest, Grass, Mallee", "Forest, Grass, Pine","Grass, Mallee, Pine", "Forest, Mallee, Pine", "Forest, Grass, Mallee, Pine"]
        ),
        "Wind Change": st.column_config.SelectboxColumn(
            "Wind Change", default="Select", options=["Yes", "No"]
        ),
        "Max Duration": st.column_config.SelectboxColumn(
            "Max Duration", default="Select", options=["<2hrs", "2-6hrs", ">6hrs"]
        ),
        "Min to 5ha": st.column_config.SelectboxColumn(
            "Min to 5ha", default="Select", options=["<15 min", "15-30 min", ">30min", ">60 min"]
        ),
        "Harvest remaining": st.column_config.ProgressColumn(
            "Harvest remaining", min_value=0, max_value=100, format="%g%%\n"
        ),
    }
        
    st.data_editor(
        df2,
        column_config=column_configuration,
        use_container_width=True,
        hide_index=True,
        num_rows="fixed",
    )

#*********************************************************************
# ICC READINESS

def icc_readiness_page():
    st.title("FBAN Auto-Fill Tool Demo")
    st.header ('ICC Readiness Detail JSOP 02.03')
    st.text('Last updated <24 hour time> on <day> <date> <month> <year>')

    #DUMMY DATA
        
    dummy_data_3 = {
            'RCC': ['Barwon South West', 'Barwon South West', 'Barwon South West', 'Barwon South West', 'Barwon South West', 'Barwon South West', 'Barwon South West', 'Barwon South West', 'Barwon South West', 'Grampians', 'Grampians', 'Grampians', 'Grampians', 'Grampians', 'Grampians', 'Grampians', 'Grampians', 'Grampians'],
            'ICC': ['Heywood', 'Heywood', 'Heywood', 'Warrnambool', 'Warrnambool', 'Warrnambool', 'Colac', 'Colac', 'Colac', 'Ballarat', 'Ballarat', 'Ballarat', 'Ararat', 'Ararat', 'Ararat', 'Horsham', 'Horsham', 'Horsham'],
            'Day': ['Tommorrow', '<Two days time>', '<Three days time>', 'Tommorrow', '<Two days time>', '<Three days time>', 'Tommorrow', '<Two days time>', '<Three days time>', 'Tommorrow', '<Two days time>', '<Three days time>', 'Tommorrow', '<Two days time>', '<Three days time>', 'Tommorrow', '<Two days time>', '<Three days time>'],
            'FBI': ['Moderate', 'High', 'Extreme', 'Moderate', 'High', 'Extreme', 'Moderate', 'High', 'Extreme', 'Moderate', 'High', 'Extreme', 'Moderate', 'High', 'Extreme', 'Moderate', 'High', 'Extreme'],
            'FDI': ['Low-Moderate', 'High', 'Very High', 'Low-Moderate', 'High', 'Very High', 'Low-Moderate', 'High', 'Very High', 'Low-Moderate', 'High', 'Very High', 'Low-Moderate', 'High', 'Very High', 'Low-Moderate', 'High', 'Very High'],
            'ICC Level': ['Nil', 'B (I)', 'C (60)', 'Nil', 'B (I)', 'C (60)', 'Nil', 'B (I)', 'C (60)', 'Nil', 'B (I)', 'C (60)', 'Nil', 'B (I)', 'C (60)', 'Nil', 'B (I)', 'C (60)']
            }
        
    df3 = pd.DataFrame(dummy_data_3)

#*********************************************************************

def SESMAP_page():
        st.title("SES MAP")
        st.header ('SES MAP')
        st.text('Last updated <24 hour time> on <day> <date> <month> <year>')

    data = [
        {"Incident No": 473095, "Incident Status": "NEW", "Incident Type": "TREE DOWN - TRAFFIC HAZ", "Event No": 221155700, "Territory": "SES", "Last Update DateTime": "21/11/2022 18:07:00", "Event Code": "TREE DOWN - TRAFFIC HAZ", "Incident Location": "MELTON WEST", "Incident Size": "SMALL", "Origin DateTime": "21/11/2022 18:01:00", "Name": "WESTMELTON DR/CHELMSFORD WAY", "Longitude": 144.5656267135199, "Latitude": -37.67734268908826, "Resource Count": 0},
        {"Incident No": 473085, "Incident Status": "CLEAR", "Incident Type": "TREE DOWN - TRAFFIC HAZ", "Event No": 221155689, "Territory": "SES", "Last Update DateTime": "21/11/2022 18:06:00", "Event Code": "TREE DOWN - TRAFFIC HAZ", "Incident Location": "TALLAROOK", "Incident Size": "SMALL", "Origin DateTime": "21/11/2022 17:45:00", "Name": "HUME FWY", "Longitude": 145.08058008266482, "Latitude": -37.1509268080358, "Resource Count": 0},
        {"Incident No": 472996, "Incident Status": "CLEAR", "Incident Type": "TREE DOWN - THREAT TO FALL", "Event No": 221155611, "Territory": "SES", "Last Update DateTime": "21/11/2022 18:06:00", "Event Code": "TREE DOWN - THREAT TO FALL", "Incident Location": "CAMPBELLFIELD", "Incident Size": "SMALL", "Origin DateTime": "21/11/2022 16:51:00", "Name": "1780 SYDNEY RD", "Longitude": 144.95573354601217, "Latitude": -37.66966761830623, "Resource Count": 0},
        {"Incident No": 473077, "Incident Status": "NEW", "Incident Type": "FLOOD - POT TO ENT. PREMISES", "Event No": 221155682, "Territory": "SES", "Last Update DateTime": "21/11/2022 18:06:00", "Event Code": "FLOOD - POT TO ENT. PREMISES", "Incident Location": "PORT MELBOURNE", "Incident Size": "SMALL", "Origin DateTime": "21/11/2022 17:35:00", "Name": "168 STOKES ST", "Longitude": 144.93925482896088, "Latitude": -37.838397147604034, "Resource Count": 1},
        {"Incident No": 473098, "Incident Status": "NEW", "Incident Type": "TREE DOWN - TRAFFIC HAZ", "Event No": 221155703, "Territory": "SES", "Last Update DateTime": "21/11/2022 18:06:00", "Event Code": "TREE DOWN - TRAFFIC HAZ", "Incident Location": "HEYWOOD", "Incident Size": "SMALL", "Origin DateTime": "21/11/2022 18:04:00", "Name": "MT CLAY RD", "Longitude": 141.660368137136, "Latitude": -38.15325331986467, "Resource Count": 0},
        {"Incident No": 473099, "Incident Status": "NEW", "Incident Type": "TREE DOWN - TRAFFIC HAZ", "Event No": 221155704, "Territory": "SES", "Last Update DateTime": "21/11/2022 18:05:00", "Event Code": "TREE DOWN - TRAFFIC HAZ", "Incident Location": "SHADY CREEK", "Incident Size": "SMALL", "Origin DateTime": "21/11/2022 18:05:00", "Name": "ARALUEN RD/OLD SALE RD", "Longitude": 146.08524968035803, "Latitude": -38.07554554632111, "Resource Count": 0},
        {"Incident No": 472929, "Incident Status": "CLEAR", "Incident Type": "TREE DOWN - ON VEHICLE", "Event No": 221155545, "Territory": "SES", "Last Update DateTime": "21/11/2022 18:05:00", "Event Code": "TREE DOWN - ON VEHICLE", "Incident Location": "SAILORS GULLY", "Incident Size": "SMALL", "Origin DateTime": "21/11/2022 16:14:00", "Name": "32 LETHEBYS RD", "Longitude": 144.23401827357114, "Latitude": -36.711649689712814, "Resource Count": 0},
        {"Incident No": 472218, "Incident Status": "NEW", "Incident Type": "TREE DOWN - RESTRICT ACCESS", "Event No": 221154821, "Territory": "SES", "Last Update DateTime": "21/11/2022 18:05:00", "Event Code": "TREE DOWN - RESTRICT ACCESS", "Incident Location": "MOUNT EVELYN", "Incident Size": "SMALL", "Origin DateTime": "21/11/2022 09:23:00", "Name": "19 HUNTER RD", "Longitude": 145.41294423563647, "Latitude": -37.803350898832136, "Resource Count": 1},
        {"Incident No": 473097, "Incident Status": "NEW", "Incident Type": "TREE DOWN - RESTRICT ACCESS", "Event No": 221155702, "Territory": "SES", "Last Update DateTime": "21/11/2022 18:05:00", "Event Code": "TREE DOWN - RESTRICT ACCESS", "Incident Location": "NARRE WARREN", "Incident Size": "SMALL", "Origin DateTime": "21/11/2022 18:04:00", "Name": "6 IMMY PDE", "Longitude": 145.31971358079466, "Latitude": -38.04280593990829, "Resource Count": 0},
        {"Incident No": 473096, "Incident Status": "NEW", "Incident Type": "TREE DOWN - THREAT TO FALL", "Event No": 221155701, "Territory": "SES", "Last Update DateTime": "21/11/2022 18:04:00", "Event Code": "TREE DOWN - THREAT TO FALL", "Incident Location": "CASTLEMAINE", "Incident Size": "SMALL", "Origin DateTime": "21/11/2022 18:03:00", "Name": "3 MARY ST", "Longitude": 144.21164665449749, "Latitude": -37.047305249015416, "Resource Count": 0},
    ]
    
    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(data)
    
    # Create a folium map centered around Victoria, Australia
    m = folium.Map(location=[-37.4713, 144.7852], zoom_start=6)
    
    # Add incident markers to the map
    for idx, row in df.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=f"{row['Incident Type']} at {row['Name']} ({row['Incident Location']})",
            tooltip=row['Incident No']
        ).add_to(m)
    
    # Set up the Streamlit app
    st.title("Victoria, Australia Incident Map")
    st.write("This map shows various incidents reported in Victoria, Australia.")
    
    # Display the folium map using Streamlit
    st_folium(m, width=700, height=500)

#*********************************************************************
#SIDEBAR

st.sidebar.image('https://upload.wikimedia.org/wikipedia/commons/9/94/Department_of_Justice_and_Community_Safety.png', width=150)
st.sidebar.title("FBAN Auto-Fill Tool")
#with st.sidebar:
    #st.title("FBAN Auto-Fill Tool"),
    #st.image("https://upload.wikimedia.org/wikipedia/commons/9/94/Department_of_Justice_and_Community_Safety.png", width=150),
    #st.radio('Sections:', options=['Home', 'How to Guide', 'FAQ', 'Barwon South West', 'Grampians', 'Loddon Mallee', 'NW Metro', 'Eastern Metro', 'Southern Metro', 'Hume', 'Gippsland', 'ICC Readiness Detail JSOP 02.03'])

# Create a page selector in the sidebar
#page = st.sidebar.selectbox("Select a page", ["Home", "How to Guide", "FAQ", "Barwon South West", "Grampians","Loddon Mallee", "Eastern Metro", "Southern Metro", "Hume", "Gippsland", "ICC Readiness Detail JSOP 02.03"])

# Create a radio button menu in the sidebar
page = st.sidebar.radio("Select an option:", ["Home", "How to Guide", "FAQ", "Barwon South West", "Grampians","Loddon Mallee", "Eastern Metro", "Southern Metro", "Hume", "Gippsland", "ICC Readiness Detail JSOP 02.03"])


#*********************************************************************
#DISPLAY SELECTED PAGE FROM SIDEBAR

# Display the selected page
if page == "Home":
    home_page()
elif page == "How to Guide":
    how_to_guide_page()
elif page == "FAQ":
    FAQ_page()
elif page == "Barwon South West":
    barwon_south_west_page()
elif page == "Grampians":
    grampians_page()
elif page == "Loddon Mallee":
    loddon_mallee_page()
elif page == "Eastern Metro":
    eastern_metro_page()
elif page == "Southern Metro":
    southern_metro_page()
elif page == "Hume":
    hume_page()
elif page == "Gippsland":
    gippsland_page()
elif page == "ICC Readiness Detail JSOP 02.03":
    icc_readiness_page()
elif page == "SES_MAP":
    SESMAP_page()
