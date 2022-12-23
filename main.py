import streamlit as st
import resources.caesar as cs
import resources.rsa as rsa
import resources.vigenere as vig
import resources.railfence as rf
import resources.columntranspo as ct
import resources.monoalphabetic as m
import resources.file as f


st.set_page_config(page_title="SecureENc")
st.markdown("# SecureENc")
# SIDEBAR

selected_type = st.selectbox("Select a type", ("Encryption", "Decryption"))
selected_technique = st.selectbox("Select a technique", ("Vigenère", "Caesar",  "RSA", "Rail Fence", "Column Transposition", "Monoalphabetic Cipher"))


# Vigenere Cipher (text, Key, transformed_text)

if selected_technique == "Vigenère":
    st.markdown("# Vigenère")
    st.caption(""" Vigenère cipher is a method of encrypting alphabetic text by 
    using a series of interwoven Caesar ciphers, based on the letters of a keyword. 
    It employs a form of polyalphabetic substitution.
    """)


    # Text Area or File Upload

    key = st.text_area(
            "Enter key:", help="The key text for encryption.", height=45).upper()

    input_type_text = st.selectbox(
        label="Select input type for TEXT",
        options=["Text", "File"],
        help="Select your input type (i.e. text or file).",
    )
    text=""
    if input_type_text == "Text":
        text = st.text_area(
            "Enter text:", help="The text to encrypt.", height=45)
        text=text.replace(" ", "").upper()
    else:
        file = st.file_uploader(label="Upload a file:",
                                help="The text file to encrypt.")
        if file is not None:
            text=f.upload(file)
            text=text.replace(" ", "").upper()


    # Start Button
    
    if st.button("Start"):
        if text.strip() != "":
            
            if selected_type == "Encryption":
                "Encrypted Text"
                st.code(vig.encrypt(key, text))    
            else: 
                "Decrypted Text"
                st.code(vig.decrypt(key, text))

        else:
            st.error("Please enter text.")



if selected_technique == "Caesar":
    st.markdown("# Caesar")
    st.caption(""" Caesar cipher is a is a type of substitution cipher 
    in which each letter in the plaintext is replaced by a letter some 
    fixed number of positions down the alphabet.
    """)


    # Text Area or File Upload

    input_type = st.selectbox(
        label="Select input type",
        options=["Text", "File"],
        help="Select your input type (i.e. text or file).",
    )
    text=""

    if input_type == "Text":
        text = st.text_area(
            "Enter text:", help="The text to encrypt.", height=45)
    else:
        file = st.file_uploader(label="Upload a file:",
                                help="The file to encrypt.")
        if file is not None:
            text=f.upload(file)


    # Shift Value

    col1, col2 = st.columns([2,3])
    with col1:
        shift_by = st.number_input(
        label="Enter a shift value:", step=1, help="Number of bits to shift each bit with."
    )
    with col2:
        pass

    
    # Start Button

    if st.button("Start"):
        if text.strip() != "":
            if selected_type == "Encryption":
                "Encrypted Text"
                st.code(cs.encrypt(text, shift_by))    
            else: 
                "Decrypted Text"
                st.code(cs.decrypt(text, shift_by))
        else:
            st.error("Please enter text.")



if selected_technique == 'RSA':
    st.markdown("# RSA")
    st.caption(""" RSA is a public-key cryptosystem that is widely used for 
    secure data transmission. It is also one of the oldest.
    """)

    # P and Q Value

    col1, col2, col3 = st.columns(3)
    with col1:
        p = st.number_input(
        label="P value:", step=1, help="Number of bits to shift each bit with.")
    with col2:
        q = st.number_input(
        label="Q value:", step=1, help="Number of bits to shift each bit with.")
    
    # Text Area or File Upload

    input_type = st.selectbox(
        label="Select input type for text",
        options=["Text", "File"],
        help="Select your input type (i.e. text or file).",
    )
    text=""
    if input_type == "Text":
        text = st.text_area(
            "Enter text:", help="The text to encrypt.", height=45   )
    else:
        file = st.file_uploader(label="Upload a file:",
                                help="The file to encrypt.",type=['txt','docx','pdf'])
        if file is not None:
            text=f.upload(file)
        
    # Start Button

    if st.button("Start"):
        check_p = rsa.is_prime(p)
        check_q = rsa.is_prime(q)
        if(p == q):
            st.error("Value of P and Q should not be equal")
        if(check_p==False):
            st.error("Please enter prime value of p.")
        if(check_q==False):
            st.error("Please enter prime value of q.")
        if (p * q) < 256 :
            st.error("The product of 'p' and 'q' should be atleast 256")

        if text.strip() != "":
            if selected_type == "Encryption":
                "Encrypted Text"
                for i in range(10) :
                    ct = rsa.encrypt(text, p, q)
                st.code(" ".join([str(i) for i in ct]))    
            else: 
                "Decrypted Text"
                for i in range(10) :
                    ct = rsa.decrypt(text, p, q)
                st.code("".join(ct))
                # st.error(text)
        else:
            st.error("Please enter text.")



if selected_technique == "Rail Fence":
    st.markdown("# Rail Fence")
    st.caption(""" The rail fence cipher is a classical type of transposition cipher. 
    It derives its name from the manner in which encryption/decryption is performed, 
    in analogy to a fence built with horizontal rails.
    """)


    # Text Area or File Upload

    input_type = st.selectbox(
        label="Select input type",
        options=["Text", "File"],
        help="Select your input type (i.e. text or file).",
    )
    text=""
    if input_type == "Text":
        text = st.text_area(
            "Enter text:", help="The text to encrypt.", height=45)
    else:
        file = st.file_uploader(label="Upload a file:",
                                help="The file to encrypt.")
        if file is not None:
            text=f.upload(file)


    # Shift Value

    col1, col2 = st.columns([2,3])
    with col1:
        shift_by = st.number_input(
        label="Enter a integer key:", step=1, help="Number of rows."
    )
    with col2:
        pass

    
    # Start Button

    if st.button("Start"):
        if text.strip() != "":
            if selected_type == "Encryption":
                "Encrypted Text"
                st.code(rf.encrypt(text, shift_by))    
            else: 
                "Decrypted Text"
                st.code(rf.decrypt(text, shift_by))
        else:
            st.error("Please enter text.")

if selected_technique == "Column Transposition":
    st.markdown("# Column Transposition")
    st.caption(""" Columnar Transposition involves writing the plaintext out in rows, 
    and then reading the ciphertext off in columns one by one.
    """)


    # Text Area or File Upload

    key = st.text_area(
            "Enter key:", help="The key text for encryption.", height=45)

    input_type_text = st.selectbox(
        label="Select input type for TEXT",
        options=["Text", "File"],
        help="Select your input type (i.e. text or file).",
    )
    text=""
    if input_type_text == "Text":
        text = st.text_area(
            "Enter text:", help="The text to encrypt.", height=45)
    else:
        file = st.file_uploader(label="Upload a file:",
                                help="The text file to encrypt.")
        if file is not None:
            text=f.upload(file)


    # Start Button

    if st.button("Start"):
        if text.strip() != "":
            
            if selected_type == "Encryption":
                "Encrypted Text"
                st.code(ct.encrypt(key, text))    
            else: 
                "Decrypted Text"
                st.code(ct.decrypt(key, text))

        else:
            st.error("Please enter text.")


if selected_technique == "Monoalphabetic Cipher":
    st.markdown("# Monoalphabetic Cipher")
    st.caption(""" A monoalphabetic substitution is a cipher in which each occurrence of a 
    plaintext symbol is replaced by a corresponding ciphertext symbol to generate ciphertext.
    """)
    key = st.text_area(
            "Enter key:", help="The key of length 26.", height=45)

    input_type_text = st.selectbox(
        label="Select input type for TEXT",
        options=["Text", "File"],
        help="Select your input type (i.e. text or file).",
    )
    text=""
    if input_type_text == "Text":
        text = st.text_area(
            "Enter text:", help="The text to encrypt.", height=45)
    else:
        file = st.file_uploader(label="Upload a file:",
                                help="The text file to encrypt.")
        if file is not None:
            text=f.upload(file)

    if st.button("Start"):
        x=1
        y=1
        if(len(key)!=26):
            x=0
            st.error("Please enter key of length 26.")
        if(m.isUniqueChars(key)==False):
            y=0
            st.error("Please enter key containing unique characters.")
        if(x!=0 and y!=0):
            if text.strip() != "":
                
                if selected_type == "Encryption":
                    "Encrypted Text"
                    st.code(m.encrypt(key, text))    
                else: 
                    "Decrypted Text"
                    st.code(m.decrypt(key, text))

            else:
                st.error("Please enter text.")

hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
