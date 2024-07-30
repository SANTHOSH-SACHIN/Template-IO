import streamlit as st


def show():
    
    
    inputs = {}  # dictionary to store all user inputs until return
    
    with st.sidebar:
        
       
        st.write("## Model")
        
        inputs["model"] = st.selectbox("Which model?", ["Top model", "Role model"])
        st.write("You should probably finish this... ;)")
        
    return inputs



if __name__ == "__main__":
    show()
    
    