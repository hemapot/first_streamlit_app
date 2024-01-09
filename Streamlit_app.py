import streamlit as st
import pandas as pd
import numpy as np
#import plost
#from PIL import Image


def highlight_Quality(row):
    styles = []
    for value in row:
        if value == 'Low Moderate':
            styles.append(f'background-color: Green;') # color: white
        elif value == 'Moderate':
            styles.append(f'background-color: yellow;') # color: black
        elif value == 'High':
            styles.append(f'background-color: orange; ') #color: white
        elif value == 'Very High':
            styles.append(f'background-color: Red; ') #color: white
        elif value == 'Extreme':
            styles.append(f'background-color: DarkRed;') # color: white
        else:
            styles.append('')
    return styles    
    
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
    st.dataframe(df3.to_pandas().style.apply(highlight_Quality, axis = 1))

    
      
    #************************DROP DOWN FILTER FOR DATAFRAME - RCC ONLY - WORKING
    # Create a dropdown filter for 'RCC' column
    selected_RCC = st.selectbox('Select RCC:', df3['RCC'].unique())
        
    # Filter the DataFrame based on the selected city
    filtered_df = df3[df3['RCC'] == selected_RCC]
    
    # Display the filtered DataFrame
    st.dataframe(filtered_df, use_container_width=True, hide_index=True)


    #************************CONDITIONAL FORMATTING TEST - Trialling Hema's code - not working
    #def highlight_ICC():
    #    styles = []
    #    for value in row:
    #        styles.append(f'background-color: Green;') # color: white
    #    return styles


    #def highlight_ICC:
    #    styles = []
    #    for value in row:
    #        if value == 'Nil':
    #            styles.append(f'background-color: Green;') # color: white
    #        elif value == 'B (I)':
    #            styles.append(f'background-color: orange; ') #color: white
    #        elif value == 'C (60)':
    #            styles.append(f'background-color: Red; ') #color: white
    #        else:
    #            styles.append('')
    #    return styles
    
    #sql = f"Select TITLE as ICC , 'ICC Level' from df3"  
    #        data_df = session.sql(sql)
    #        st.dataframe(data_df.to_pandas().style.apply(highlight_ICC, axis = 1))


    # Apply the styling function to the DataFrame using applymap
    #styled_df = df3.style.applymap(highlight_ICC)

    # Render the styled DataFrame using st.dataframe
    #st.dataframe(styled_df, unsafe_allow_html=True)

    #************************CONDITIONAL FORMATTING TEST - trialing bespoke highlighting - NOT WORKING
    # Function for conditional formatting of string values
    #def highlight_strings(val):
    #    color = 'background-color: green' if 'Nil' in val.lower() else ''
    #    return color
    
    # Apply the styling function to the DataFrame using applymap
    #styled_df = df3.style.applymap(highlight_strings)
    
    # Render the styled DataFrame using st.dataframe
    #st.dataframe(styled_df, use_container_width=True, hide_index=True)
    #st.dataframe(styled_df, unsafe_allow_html=True)
    #st.dataframe(filtered_df, use_container_width=True, hide_index=True, styled_df, unsafe_allow_html=True)
    
    #************************CONDITIONAL FORMATTING TEST - trialing max and min highlighting - NOT WORKING
    # Columns to highlight
    #highlight_columns = ('ICC Level')

    #apply styling to highlihgt max and min values
    #styled_df3 = df3.style\
    #   .background_gradient(subset=highlight_columns, cmap='viridis')
        #.highlight_max(subset=highlight_columns, color='lightgreen')\
        #.highlight_min(subset=highlight_columns, color='red')
        

    #************************DROP DOWN FILTER FOR DATAFRAME - FILTERS CONNECTED - NOT QUITE WORKING, CAN'T ALSO FILTER ICC AS WELL
    # Create a dropdown filter for the 'ICC' and 'RCC' column
    #selected_RCC = st.selectbox('Select RCC:', df3['RCC'].unique())
    
    # Filter the DataFrame based on the selected city
    #filtered_ICC = df3[df3['RCC'] == selected_RCC]

    #selected_ICC = st.selectbox('Select ICC:', filtered_ICC['ICC'].unique())
    
    # Display the filtered DataFrame
    #st.dataframe(filtered_ICC, hide_index=True)

    #************************DROP DOWN FILTER FOR DATAFRAME - FILTERS NOT CONNECTED
    # Create a dropdown filter for the 'ICC' and 'RCC' column
    #selected_RCC = st.selectbox('Select RCC:', df3['RCC'].unique())
    #selected_ICC = st.selectbox('Select ICC:', df3['ICC'].unique())
    
    # Filter the DataFrame based on the selected city
    #filtered_df = df3[(df3['RCC'] == selected_RCC) & (df3['ICC'] == selected_ICC)]
    
    # Display the filtered DataFrame
    #st.dataframe(filtered_df, hide_index=True)
    
    #************************BASIC DATA FRAME
    #st.dataframe(df3, hide_index=True)


    #************************CONDITIONAL FORMATTING TEST - DOES NOT WORK
    # Function to apply conditional formatting based on specific strings
    #def highlight_specific_strings(val, target_strings):
    #    return 'background-color: red' if val in target_strings else ''
    
    # Specify the target strings for conditional formatting
    #target_strings = ['B (I)', 'C (60)']
    
    # Apply the styling function to the DataFrame
    #styled_df = df3.applymap(lambda x: highlight_specific_strings(x, target_strings))
    
    # Render the styled DataFrame
    #st.dataframe(styled_df, hide_index=True)
    #st.dataframe(styled_df, hide_index=True, unsafe_allow_html=True)


#**********************************************************
# Style of non-editable table - NEED TO EDIT THIS ONE - DOESN'T WORK FOR EDITABLE TABLES
#    header_style = '''
#        <style>
#            thead{
#                background-color: #C6E8F6;
#                color: #FFFFFF;
#                }
#        </style>
#    '''
#    st.markdown(header_style, unsafe_allow_html=True)

#***************************************************************
#OLD VERSION OF TABLES FOR REFERENCE
#st.data_editor(
#        df2, 
#        column_config={
#            "ICC": "ICC",
#            "Day": "Day",
#            "Confidence level": st.column_config.TextColumn("Confidence level", width=None, help="FBAN confidence level", disabled=None, required=True, default=None, max_chars=4, validate=None),
#            "Fuel Type Driver": st.column_config.SelectboxColumn("Fuel Type Driver", help="Fuel driving fire behaviour", disabled=None, required=True, default=None, options=["Forest", "Grass", "Mallee", "Pine"]),
#            "FBI": "FBI",
#            "FDI": "FDI",
#            "Wind Change": st.column_config.SelectboxColumn("Wind Change", help="If there is a wind change or not", disabled=None, required=True, default="No", options=["Yes", "No"]),
#            "Ignitability": "Ignitability",
#            "Max Duration": st.column_config.SelectboxColumn("Max duration", help="Maximum duration of the fire risk", disabled=None, required=True, default=None, options=["<2hrs", "2-6hrs", ">6hrs"]),
#            "Min to 5ha": st.column_config.SelectboxColumn("Min to 5ha", help="Minimum time to 5ha", disabled=None, required=True, default=None, options=["<15 min", "15-30 min", ">30min", ">60 min"]),
#            "FDP": "FDP",
#            "Lightning": "Lightning",
#            "Harvest remaining": st.column_config.ProgressColumn("Harvest remaining", width=None, help="% harvest to be completed", format=None, min_value=0, max_value=1),
#        },     
#    )


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
