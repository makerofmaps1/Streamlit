from sqlite3 import connect

# create database and cursor connection
DBCON = connect('mystreamlitdb.db')
CUR = DBCON.cursor()

################################
# database functions
################################

# fetch a row of data where userinput is null
def fetchdatarow():

    CUR.execute("SELECT pkey, userinput \
                 FROM datatable \
                 WHERE userinput IS NULL \
                 LIMIT 1")
    datarow = CUR.fetchone()

    return datarow

# database update
def updatedb(pkey,userinput):

    CUR.execute(f"UPDATE datatable \
                  SET userinput = '{userinput}' \
                  WHERE pkey = {pkey}")
    DBCON.commit()

################################
# app
################################

import streamlit as st

with st.form('myform', clear_on_submit = True):

    datarow = fetchdatarow() # fetch data row from database
    st.write(f'These are the values (in a tuple) retrieved from database: {datarow}') # write out data row to app page (for viewing)

    pkey = datarow[0] # primary key value from database
    dbuserinput = datarow[1] # user input column from database
    st.write(pkey) # write out pkey to app page (for viewing)
    st.write(dbuserinput) # write out userinput (for viewing)

    # list of options for user input
    selectoptions = ['option 1', 'option 2']

    # drop down menu for user input options
    userinput = st.selectbox('Choose action', options = selectoptions)

    # make a submit button
    formsubmit = st.form_submit_button('submit update')

    # submit button is false by default, clicking returns True
    if formsubmit:

        # if formsubmit is true, run update database function
        updatedb(pkey,userinput)
