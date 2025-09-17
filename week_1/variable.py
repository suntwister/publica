# #variable_1
# name = "susan"
# # variable_2
# age = 18
# # variable_3
# height = 1.55 #meters


# # convert input to integer
# number = int(input("input a number"))
# print(number)

# import streamlit as st
# import mymodel as m
# st.write(""""
# dial_code = input("dial *321# to recharge data\n:")
# message_1 = int(input("Welcome to data recharge/gifting: \n 1. Data recharge \n 2. Data Gifting \n 3. Data Sharing\n: "))
# message_2 = int(input("1. daily \n 2. weekly \n 3. monthly \n: "))
# message_3 = int(input("1. 50mb for 100 naira \n 2. 100mb for 200 naira \n 3. 500 mb for 500\n: "))
# message_4 = ("you've successfuly recharge 50mb for 1 day ")
# print(message_4)
# """)

import streamlit as st
#import mymodel as m  # assuming you have a model you want to use

st.title("Data Recharge App")

dial_code = st.text_input("Dial *321# to recharge data")

if dial_code:
    message_1 = st.selectbox("Welcome to data recharge/gifting:", 
                             [1, 2, 3], 
                             format_func=lambda x: {
                                 1: "Data recharge",
                                 2: "Data Gifting",
                                 3: "Data Sharing"
                             }[x])

    message_2 = st.selectbox("Choose a plan duration:", 
                             [1, 2, 3], 
                             format_func=lambda x: {
                                 1: "Daily",
                                 2: "Weekly",
                                 3: "Monthly"
                             }[x])

    message_3 = st.selectbox("Choose a data plan:", 
                             [1, 2, 3], 
                             format_func=lambda x: {
                                 1: "50MB for 100 naira",
                                 2: "100MB for 200 naira",
                                 3: "500MB for 500 naira"
                             }[x])

    if st.button("Recharge Now"):
        # You could plug in your model here if needed
        st.success("You've successfully recharged 50MB for 1 day")
