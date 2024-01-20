import streamlit as st
import pandas as pd

def main():
    st.title("PA Application Assistant")
    st.caption(":green[by omee :smiley:]")

    uploaded_file = st.file_uploader("Upload CSV file here.", type='csv')

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        headers = df.columns.tolist()

        new_headers = headers[1:4]
        returning_headers = headers[4:]

        # print(returning_headers)
        # print(new_headers)

        applicant = st.number_input("Input the applicant's row in the spreadsheet:", value=2,min_value=2,max_value=len(df)+1)
        st.caption(":red[SAVE ANY NOTES/COMMENTS BEFORE MOVING TO NEXT APPLICANT!]")

        df_row = applicant - 2

        responses = df.iloc[df_row]
        net_id = responses.iloc[0]
        # print(net_id)

        if responses.isnull().iloc[1]:

            st.header(f"Response for :blue[returning] applicant :blue[{net_id}]")
            st.caption(f":gray[(spreadsheet row {applicant})]")

            app_responses = responses.tolist()[4:]

            st.write("--")
            
            st.subheader(returning_headers[0])

            st.write(app_responses[0])
            text_input = st.text_input(
                ":gray[Q1 Notes]",
                placeholder="Notes..."
            )

            st.divider()

            st.subheader(returning_headers[1])

            st.write(app_responses[1])
            text_input = st.text_input(
                ":gray[Q2 Notes]",
                placeholder="Notes..."
            )

            st.divider()

            st.subheader(returning_headers[2])

            st.write(app_responses[2])
            text_input = st.text_input(
                ":gray[Q3 Notes]",
                placeholder="Notes..."
            )

            st.divider()

            st.subheader(returning_headers[3])

            st.write(app_responses[3])
            text_input = st.text_input(
                ":gray[Q4 Notes]",
                placeholder="Notes..."
            )

            

        else:
            st.header(f"Response for :blue[new] applicant :blue[{net_id}]")
            st.caption(f":gray[Spreadsheet row: {applicant}]")

            app_responses = responses.tolist()[1:4]

            st.write("--")

            st.subheader(new_headers[0])

            st.write(app_responses[0])
            text_input = st.text_input(
                ":gray[Q1 Notes]",
                placeholder="Notes..."
            )

            st.divider()

            st.subheader(new_headers[1])

            st.write(app_responses[1])
            text_input = st.text_input(
                ":gray[Q2 Notes]",
                placeholder="Notes..."
            )

            st.divider()

            st.subheader(new_headers[2])

            st.write(app_responses[2])
            text_input = st.text_input(
                ":gray[Q3 Notes]",
                placeholder="Notes..."
            )


if __name__ == "__main__":
    main()