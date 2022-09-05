import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data= pd.read_csv('Employees3. .csv') 
data

st.title('EmployeesApp')
st.header("Aplicación Streamlit")

@st.cache
def load_data(nrows):
    data = pd.read_csv("Employees3. .csv", nrows=nrows)
    lowercase = lambda x: str(x).lower()
    return data

data_load_state = st.text('Cargando los datos...')
data = load_data(501)
data_load_state.text("Datos han sido cargados")

agree = st.sidebar.checkbox("Mostrar dataframe")
if agree:
    st.header("Empleados")
    st.dataframe(data)

agree2= st.sidebar.checkbox("Histograma-edad")
if agree2:
    fig, ax = plt.subplots()
    ax.hist(data.Age)
    st.header("Histograma Empleados - atributo edad")
    st.pyplot(fig)
    st.markdown("_")

agree3= st.sidebar.checkbox("Gráfica frecuencias, empleados/unidad")
if agree3:
    fig, ax = plt.subplots()
    ax.hist(data.Unit)
    st.header("Histograma Empleados - atributo unidad")
    st.pyplot(fig)
    st.markdown("_")

agree4= st.sidebar.checkbox("Gráfica ciudades/índice deserción")
if agree4:
    fig, ax = plt.subplots()
    y= data["Attrition_rate"]
    x=data["Hometown"]
    ax.barh(x,y)
    ax.set_ylabel("Ciudad")
    ax.set_xlabel("Índice deserción")
    st.header("Índice deserción ciudad")
    st.pyplot(fig)
    st.markdown("_")

agree5= st.sidebar.checkbox("Gráfica edad/índice deserción")
if agree5:
    fig, ax = plt.subplots()
    y= data["Attrition_rate"]
    x=data["Age"]
    ax.barh(x,y)
    ax.set_ylabel("Edad")
    ax.set_xlabel("Índice deserción")
    st.header("Índice deserción por edad")
    st.pyplot(fig)
    st.markdown("_")

agree6= st.sidebar.checkbox("Gráfica tiempo servicio/tasa deserción")
if agree6:
    fig, ax = plt.subplots()
    y= data["Attrition_rate"]
    x=data["Time_of_service"]
    ax.barh(x,y)
    ax.set_ylabel("Tiempo de servicio")
    ax.set_xlabel("Índice de deserción")
    st.header("Índice deserción/tasa de servicio")
    st.pyplot(fig)
    st.markdown("_")

@st.cache
def load_data_byid(id):
    filtered_data_byid=data[data["Employee_ID"].str.upper().str.contains(id.upper())]
    
    return filtered_data_byid

myid= st.sidebar.text_input("ID empleado")
btnid=st.sidebar.button("Buscar ID")

if(btnid):
    filterbyid= load_data_byid(myid)
    count_row= filterbyid.shape[0]
    st.write(f"Total: {count_row} resultados")

    st.dataframe(filterbyid)

@st.cache
def load_data_byht(ht):
    filtered_data_byht=data[data["Hometown"].str.upper().str.contains(ht.upper())]
    
    return filtered_data_byht

myht= st.sidebar.text_input("Hometown de empleado")
btnht=st.sidebar.button("Buscar por hometown")

if(btnht):
    filterbyht= load_data_byht(myht)
    count_row= filterbyht.shape[0]
    st.write(f"Total: {count_row} resultados")

    st.dataframe(filterbyht)

@st.cache
def load_data_byunit(unit):
    filtered_data_byunit=data[data["Unit"].str.upper().str.contains(unit.upper())]
    
    return filtered_data_byunit

myunit= st.sidebar.text_input("Unidad empleado")
btnunit=st.sidebar.button("Buscar por unidad")

if(btnunit):
    filterbyunit= load_data_byunit(myunit)
    count_row= filterbyunit.shape[0]
    st.write(f"Total: {count_row} resultados")

    st.dataframe(filterbyunit)

@st.cache
def load_data_byeducation(education):
    filtered_data_byedu=data[data["Education_Level"]==education]
    
    return filtered_data_byedu

myedu= st.sidebar.selectbox("Seleccionar nivel educativo", data['Education_Level'].unique())
btnedu=st.sidebar.button("Buscar por educación")

if(btnedu):
    filterbyedu= load_data_byeducation(myedu)
    count_row= filterbyedu.shape[0]
    st.write(f"Total: {count_row} resultados")

    st.dataframe(filterbyedu)

@st.cache
def load_data_byhtw(htw):
    filtered_data_byhtw=data[data["Hometown"]==htw]
    
    return filtered_data_byhtw

myhtw= st.sidebar.selectbox("Seleccionar ciudad", data['Hometown'].unique())
btnhtw=st.sidebar.button("Buscar por ciudad")

if(btnhtw):
    filterbyhtw= load_data_byhtw(myhtw)
    count_row= filterbyhtw.shape[0]
    st.write(f"Total: {count_row} resultados")

    st.dataframe(filterbyhtw)

@st.cache
def load_data_byun(un):
    filtered_data_byun=data[data["Unit"]==un]
    
    return filtered_data_byun

myun= st.sidebar.selectbox("Seleccionar unidad en caja", data['Unit'].unique())
btnun=st.sidebar.button("Buscar por unidad en caja")

if(btnun):
    filterbyun= load_data_byun(myun)
    count_row= filterbyun.shape[0]
    st.write(f"Total: {count_row} resultados")

    st.dataframe(filterbyun)


    




