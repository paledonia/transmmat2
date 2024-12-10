import streamlit as st 

# 1) crear las paginas 

intro = st.Page("paginas/uno.py", title = "Introducción", icon = ":material/star:")  
prueba = st.Page("paginas/dos.py", title = "Prueba")   
vectores = st.Page ("paginas/vectores.py", title = "Vectores") 
deter = st.Page("paginas/deter.py", title = "Determinantes") 
trans = st.Page("paginas/trans.py", title = "Transformaciones Lineales") 
yo = st.Page("paginas/yo.py", title = "Andres Castellanos") 
quiz = st.Page("paginas/quiz.py", title = "Quiz") 
mul_trans = st.Page("paginas/mul_trans.py", title = "Multiplicacion vista como Tranformaciones lineales")  
sub_es = st.Page("paginas/sub_es.py", title = "Subespacios Vectoriales") 




pg = st.navigation({"Corazon del Algebra lineal": [intro,vectores,sub_es,trans ], "Prueba tus conocimientos":[quiz], "Quien soy":[yo]}) 

pg.run()



