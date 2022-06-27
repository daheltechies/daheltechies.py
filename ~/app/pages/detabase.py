import streamlit as st
from deta import Deta

deta = Deta(st.secrets["deta_key"])
db = deta.Base("assignment-Records")


def check_password():
     def password_entered():
          if st.session_state["password"] == st.secrets["password"]:
                st.session_state["password_correct"] = True
                del st.session_state["password"]
          else:
                st.session_state["password_correct"] = False
     if "password_correct" not in st.session_state:
            st.text_input(
                "password", type="password", on_change=password_entered, key="password"
            )
            return False
     elif not st.session_state["password_correct"]:
            st.text_input(
                "password", type="password", on_change=password_entered, key="password"
            )
            st.error("😏 Password incorrect")
            return False
     else:
            return True
        
if check_password():
  db_content = db.fetch().items
  st.write(db_content)
