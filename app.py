import streamlit as st

# # Create the SQL connection to pets_db as specified in your secrets file.
# conn = st.connection('chat_db', type='sql')

# # Insert some data with conn.session.
# with conn.session as s:
#     # s.execute('CREATE TABLE IF NOT EXISTS users (person TEXT, password_hashed TEXT);')
#     s.execute('CREATE TABLE IF NOT EXISTS users (person TEXT, pet TEXT);')
#     s.execute('DELETE FROM users;')
#     users = {'user1': 'user1', 'user2': 'user2', 'user3': 'user3'}
#     for k in users:
#         s.execute(
#             'INSERT INTO users (person, password_hashed) VALUES (:person, :password_hashed));',
#             params=dict(person=k, password_hashed=users[k])
#         )
#     s.commit()

# # Query and display the data you inserted
# pet_owners = conn.query('select * from users')
# st.dataframe(pet_owners)



st.title("Respose back the user input")

if "messages" not in st.session_state:
    st.session_state.messages = []



for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("What's up?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    
    st.session_state.messages.append({'role':'user','content':prompt})

    response = f"Mirrrorring back: {prompt}"

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({'role':'assistant','content':response})
