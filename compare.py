import streamlit as st
import pandas as pd
import numpy as np
import re
import io 

pd.set_option("styler.render.max_elements", 517751)

# CSS styles for custom appearance
st.markdown("""
<style>
    .main {
        background-color: #f0f2f5;
        color: #333;
    }
    .title {
        font-size: 2.5rem;
        color: #4a90e2;
        text-align: center;
    }
    .header {
        font-size: 1.5rem;
        color: #4a90e2;
    }
    .success {
        color: #28a745;
    }
    .error {
        color: #dc3545;
    }
    .info {
        color: #007bff;
    }
</style>
""", unsafe_allow_html=True)

def nonalpha(text):
    tt = re.sub(r'[^a-zA-Z0-9.]', '', text)
    return tt.upper()

def nonalphadot(text):
    tt = re.sub(r'[^a-zA-Z0-9]', '', text)
    tt = tt.replace(".", "")
    return tt.upper()

def numeric(text):
    return text.isnumeric()

def leng(text):
    return len(text)

def compare(lst) :
    str1=list(lst[0])
    str2=list(lst[1])
    if (len(str2) == len(str1)) and (((''.join(str2)).find(''.join(str1)))==-1):
        for i in range(len(str2)):
            for j in range(len(str1)):
                if (str2[i] == str1[j]) & (i==j):
                    str2[j]="_"
                    str1[j]="_"
                    
                    
                else:
                    str1[j]=str1[j]
                    str2[i]=str2[i]                  

                    
                j+=1
            i+=1   
    elif (len(str2) == len(str1)) and (((''.join(str2)).find(''.join(str1)))!=-1):
        for i in range(len(str2)):
            for j in range(len(str1)):
                if (str2[i] == str1[j]) & (i==j):
                    str2[j]="_"
                    str1[j]="_"
                    
                    
                else:
                    str1[j]=str1[j]
                    str2[i]=str2[i]                  

                    
                j+=1
            i+=1              
    elif (len(str2)) > (len(str1)) and (((''.join(str2)).find(''.join(str1)))==0):
        for i in range(len(str2)):
            for j in range(len(str1)):
                if (str2[i] == str1[j]) & (i==j):
                    str2[j]="_"
                    str1[j]="_"
                    
                    
                else:
                    str1[j]=str1[j]
                    str2[i]=str2[i]                  

                    
                j+=1
            i+=1

    elif (len(str1) >= len(str2)) and (((''.join(str1)).find(''.join(str2)))==0):   
        for i in range(len(str1)):
            for j in range(len(str2)):
                if (str1[i] == str2[j]) & (i==j):
                    str1[i]="_"
                    str2[j]="_"
                else:
                    str1[i]=str1[i]
                    str2[j]=str2[j]
                j+=1
            i+=1
    elif (len(str1) >= len(str2)) and (((''.join(str1)).find(''.join(str2)))==-1):   
        for i in range(len(str1)):
            for j in range(len(str2)):
                if (str1[i] == str2[j]) & (i==j):
                    str1[i]="_"
                    str2[j]="_"
                else:
                    str1[i]=str1[i]
                    str2[j]=str2[j]
                j+=1
            i+=1            
    elif ((''.join(str2)).find(''.join(str1)))==1:
        str1=list('_'+''.join(str1))
        for i in range(len(str2)):
            for j in range(len(str1)):
                if (str2[i] == str1[j]) & (i==j):
                    str1[j]="_"
                    str2[i]="_"
                else:
                    str1[j]=str1[j]
                    str2[i]=str2[i]
    elif ((''.join(str2)).find(''.join(str1)))==2:
        str1=list('__'+''.join(str1))
        for i in range(len(str2)):
            for j in range(len(str1)):
                if (str2[i] == str1[j]) & (i==j):
                    str1[j]="_"
                    str2[i]="_"
                else:
                    str1[j]=str1[j]
                    str2[i]=str2[i]
    elif ((''.join(str2)).find(''.join(str1)))==3:
        str1=list('___'+''.join(str1))
        for i in range(len(str2)):
            for j in range(len(str1)):
                if (str2[i] == str1[j]) & (i==j):
                    str1[j]="_"
                    str2[i]="_"
                else:
                    str1[j]=str1[j]
                    str2[i]=str2[i]
    elif ((''.join(str2)).find(''.join(str1)))==4:
        str1=list('____'+''.join(str1))
        for i in range(len(str2)):
            for j in range(len(str1)):
                if (str2[i] == str1[j]) & (i==j):
                    str1[j]="_"
                    str2[i]="_"
                else:
                    str1[j]=str1[j]
                    str2[i]=str2[i]
    elif ((''.join(str2)).find(''.join(str1)))==5:
        str1=list('_____'+''.join(str1))
        for i in range(len(str2)):
            for j in range(len(str1)):
                if (str2[i] == str1[j]) & (i==j):
                    str1[j]="_"
                    str2[i]="_"
                else:
                    str1[j]=str1[j]
                    str2[i]=str2[i]
    elif ((''.join(str2)).find(''.join(str1)))==6:
        str1=list('______'+''.join(str1))
        for i in range(len(str2)):
            for j in range(len(str1)):
                if (str2[i] == str1[j]) & (i==j):
                    str1[j]="_"
                    str2[i]="_"
                else:
                    str1[j]=str1[j]
                    str2[i]=str2[i]
    elif ((''.join(str2)).find(''.join(str1)))==7:
        str1=list('_______'+''.join(str1))
        for i in range(len(str2)):
            for j in range(len(str1)):
                if (str2[i] == str1[j]) & (i==j):
                    str1[j]="_"
                    str2[i]="_"
                else:
                    str1[j]=str1[j]
                    str2[i]=str2[i]
    elif ((''.join(str2)).find(''.join(str1)))==8:
        str1=list('________'+''.join(str1))
        for i in range(len(str2)):
            for j in range(len(str1)):
                if (str2[i] == str1[j]) & (i==j):
                    str1[j]="_"
                    str2[i]="_"
                else:
                    str1[j]=str1[j]
                    str2[i]=str2[i]
    elif ((''.join(str2)).find(''.join(str1)))==9:
        str1=list('_________'+''.join(str1))
        for i in range(len(str2)):
            for j in range(len(str1)):
                if (str2[i] == str1[j]) & (i==j):
                    str1[j]="_"
                    str2[i]="_"
                else:
                    str1[j]=str1[j]
                    str2[i]=str2[i]
    elif ((''.join(str2)).find(''.join(str1)))==10:
        str1=list('__________'+''.join(str1))
        for i in range(len(str2)):
            for j in range(len(str1)):
                if (str2[i] == str1[j]) & (i==j):
                    str1[j]="_"
                    str2[i]="_"
                else:
                    str1[j]=str1[j]
                    str2[i]=str2[i]
    elif ((''.join(str1)).find(''.join(str2)))==1:
        str2=list('_'+''.join(str2))
        for i in range(len(str1)):
            for j in range(len(str2)):
                if (str1[i] == str2[j]) & (i==j):
                    str2[j]="_"
                    str1[i]="_"
                else:
                    str2[j]=str2[j]
                    str1[i]=str1[i]
    elif ((''.join(str1)).find(''.join(str2)))==2:
        str2=list('__'+''.join(str2))
        for i in range(len(str1)):
            for j in range(len(str2)):
                if (str1[i] == str2[j]) & (i==j):
                    str2[j]="_"
                    str1[i]="_"
                else:
                    str2[j]=str2[j]
                    str1[i]=str1[i]
    elif ((''.join(str1)).find(''.join(str2)))==3:
        str2=list('___'+''.join(str2))
        for i in range(len(str1)):
            for j in range(len(str2)):
                if (str1[i] == str2[j]) & (i==j):
                    str2[j]="_"
                    str1[i]="_"
                else:
                    str2[j]=str2[j]
                    str1[i]=str1[i]
    elif ((''.join(str1)).find(''.join(str2)))==4:
        str2=list('____'+''.join(str2))
        for i in range(len(str1)):
            for j in range(len(str2)):
                if (str1[i] == str2[j]) & (i==j):
                    str2[j]="_"
                    str1[i]="_"
                else:
                    str2[j]=str2[j]
                    str1[i]=str1[i]
    elif ((''.join(str1)).find(''.join(str2)))==5:
        str2=list('_____'+''.join(str2))
        for i in range(len(str1)):
            for j in range(len(str2)):
                if (str1[i] == str2[j]) & (i==j):
                    str2[j]="_"
                    str1[i]="_"
                else:
                    str2[j]=str2[j]
                    str1[i]=str1[i]
    elif ((''.join(str1)).find(''.join(str2)))==6:
        str2=list('______'+''.join(str2))
        for i in range(len(str1)):
            for j in range(len(str2)):
                if (str1[i] == str2[j]) & (i==j):
                    str2[j]="_"
                    str1[i]="_"
                else:
                    str2[j]=str2[j]
                    str1[i]=str1[i]
    elif ((''.join(str1)).find(''.join(str2)))==7:
        str2=list('_______'+''.join(str2))
        for i in range(len(str1)):
            for j in range(len(str2)):
                if (str1[i] == str2[j]) & (i==j):
                    str2[j]="_"
                    str1[i]="_"
                else:
                    str2[j]=str2[j]
                    str1[i]=str1[i]
    elif ((''.join(str1)).find(''.join(str2)))==8:
        str2=list('________'+''.join(str2))
        for i in range(len(str1)):
            for j in range(len(str2)):
                if (str1[i] == str2[j]) & (i==j):
                    str2[j]="_"
                    str1[i]="_"
                else:
                    str2[j]=str2[j]
                    str1[i]=str1[i]
    elif ((''.join(str1)).find(''.join(str2)))==9:
        str2=list('_________'+''.join(str2))
        for i in range(len(str1)):
            for j in range(len(str2)):
                if (str1[i] == str2[j]) & (i==j):
                    str2[j]="_"
                    str1[i]="_"
                else:
                    str2[j]=str2[j]
                    str1[i]=str1[i]
    #new Line
    elif (len(str1)-len(str2)==1) and (((''.join(str1)).find(''.join(str2)))==-1):
        str2=list('_'+''.join(str2))
        for i in range(len(str1)):
            for j in range(len(str2)):
                if (str1[i] == str2[j]) & (i==j):
                    str1[i]="_"
                    str2[j]="_"
                else:
                    str1[i]=str1[i]
                    str2[j]=str2[j]
                j+=1
            i+=1
    elif (len(str1)-len(str2)==2) and (((''.join(str1)).find(''.join(str2)))==-1):
        str2=list('__'+''.join(str2))
        for i in range(len(str1)):
            for j in range(len(str2)):
                if (str1[i] == str2[j]) & (i==j):
                    str1[i]="_"
                    str2[j]="_"
                else:
                    str1[i]=str1[i]
                    str2[j]=str2[j]
                j+=1
            i+=1
    elif (len(str1)-len(str2)==3) and (((''.join(str1)).find(''.join(str2)))==-1):
        str2=list('___'+''.join(str2))
        for i in range(len(str1)):
            for j in range(len(str2)):
                if (str1[i] == str2[j]) & (i==j):
                    str1[i]="_"
                    str2[j]="_"
                else:
                    str1[i]=str1[i]
                    str2[j]=str2[j]
                j+=1
            i+=1
    elif (len(str1)-len(str2)==4) and (((''.join(str1)).find(''.join(str2)))==-1):
        str2=list('____'+''.join(str2))
        for i in range(len(str1)):
            for j in range(len(str2)):
                if (str1[i] == str2[j]) & (i==j):
                    str1[i]="_"
                    str2[j]="_"
                else:
                    str1[i]=str1[i]
                    str2[j]=str2[j]
                j+=1
            i+=1 
    elif (len(str1)-len(str2)==5) and (((''.join(str1)).find(''.join(str2)))==-1):
        str2=list('_____'+''.join(str2))
        for i in range(len(str1)):
            for j in range(len(str2)):
                if (str1[i] == str2[j]) & (i==j):
                    str1[i]="_"
                    str2[j]="_"
                else:
                    str1[i]=str1[i]
                    str2[j]=str2[j]
                j+=1
            i+=1
    elif (len(str1)-len(str2)==6) and (((''.join(str1)).find(''.join(str2)))==-1):
        str2=list('______'+''.join(str2))
        for i in range(len(str1)):
            for j in range(len(str2)):
                if (str1[i] == str2[j]) & (i==j):
                    str1[i]="_"
                    str2[j]="_"
                else:
                    str1[i]=str1[i]
                    str2[j]=str2[j]
                j+=1
            i+=1
    elif (len(str1)-len(str2)==7) and (((''.join(str1)).find(''.join(str2)))==-1):
        str2=list('_______'+''.join(str2))
        for i in range(len(str1)):
            for j in range(len(str2)):
                if (str1[i] == str2[j]) & (i==j):
                    str1[i]="_"
                    str2[j]="_"
                else:
                    str1[i]=str1[i]
                    str2[j]=str2[j]
                j+=1
            i+=1
    elif (len(str1)-len(str2)==8) and (((''.join(str1)).find(''.join(str2)))==-1):
        str2=list('________'+''.join(str2))
        for i in range(len(str1)):
            for j in range(len(str2)):
                if (str1[i] == str2[j]) & (i==j):
                    str1[i]="_"
                    str2[j]="_"
                else:
                    str1[i]=str1[i]
                    str2[j]=str2[j]
                j+=1
            i+=1 
    elif (len(str1)-len(str2)==9) and (((''.join(str1)).find(''.join(str2)))==-1):
        str2=list('_________'+''.join(str2))
        for i in range(len(str1)):
            for j in range(len(str2)):
                if (str1[i] == str2[j]) & (i==j):
                    str1[i]="_"
                    str2[j]="_"
                else:
                    str1[i]=str1[i]
                    str2[j]=str2[j]
                j+=1
            i+=1
    elif (len(str1)-len(str2)==10) and (((''.join(str1)).find(''.join(str2)))==-1):
        str2=list('__________'+''.join(str2))
        for i in range(len(str1)):
            for j in range(len(str2)):
                if (str1[i] == str2[j]) & (i==j):
                    str1[i]="_"
                    str2[j]="_"
                else:
                    str1[i]=str1[i]
                    str2[j]=str2[j]
                j+=1
            i+=1            
    #new Line
    #new Line2
    elif (len(str2)-len(str1)==1) and (((''.join(str2)).find(''.join(str1)))==-1):
        str1=list('_'+''.join(str1))
        for i in range(len(str1)):
            for j in range(len(str2)):
                if (str1[i] == str2[j]) & (i==j):
                    str1[i]="_"
                    str2[j]="_"
                else:
                    str1[i]=str1[i]
                    str2[j]=str2[j]
                j+=1
            i+=1
    elif (len(str2)-len(str1)==2) and (((''.join(str2)).find(''.join(str1)))==-1):
        str1=list('__'+''.join(str1))
        for i in range(len(str1)):
            for j in range(len(str2)):
                if (str1[i] == str2[j]) & (i==j):
                    str1[i]="_"
                    str2[j]="_"
                else:
                    str1[i]=str1[i]
                    str2[j]=str2[j]
                j+=1
            i+=1
    elif (len(str2)-len(str1)==3) and (((''.join(str2)).find(''.join(str1)))==-1):
        str1=list('___'+''.join(str1))
        for i in range(len(str1)):
            for j in range(len(str2)):
                if (str1[i] == str2[j]) & (i==j):
                    str1[i]="_"
                    str2[j]="_"
                else:
                    str1[i]=str1[i]
                    str2[j]=str2[j]
                j+=1
            i+=1
    elif (len(str2)-len(str1)==4) and (((''.join(str2)).find(''.join(str1)))==-1):
        str1=list('____'+''.join(str1))
        for i in range(len(str1)):
            for j in range(len(str2)):
                if (str1[i] == str2[j]) & (i==j):
                    str1[i]="_"
                    str2[j]="_"
                else:
                    str1[i]=str1[i]
                    str2[j]=str2[j]
                j+=1
            i+=1 
    elif (len(str2)-len(str1)==5) and (((''.join(str2)).find(''.join(str1)))==-1):
        str1=list('_____'+''.join(str1))
        for i in range(len(str1)):
            for j in range(len(str2)):
                if (str1[i] == str2[j]) & (i==j):
                    str1[i]="_"
                    str2[j]="_"
                else:
                    str1[i]=str1[i]
                    str2[j]=str2[j]
                j+=1
            i+=1
    elif (len(str2)-len(str1)==6) and (((''.join(str2)).find(''.join(str1)))==-1):
        str1=list('______'+''.join(str1))
        for i in range(len(str1)):
            for j in range(len(str2)):
                if (str1[i] == str2[j]) & (i==j):
                    str1[i]="_"
                    str2[j]="_"
                else:
                    str1[i]=str1[i]
                    str2[j]=str2[j]
                j+=1
            i+=1
    elif (len(str2)-len(str1)==7) and (((''.join(str2)).find(''.join(str1)))==-1):
        str1=list('_______'+''.join(str1))
        for i in range(len(str1)):
            for j in range(len(str2)):
                if (str1[i] == str2[j]) & (i==j):
                    str1[i]="_"
                    str2[j]="_"
                else:
                    str1[i]=str1[i]
                    str2[j]=str2[j]
                j+=1
            i+=1
    elif (len(str2)-len(str1)==8) and (((''.join(str2)).find(''.join(str1)))==-1):
        str1=list('________'+''.join(str1))
        for i in range(len(str1)):
            for j in range(len(str2)):
                if (str1[i] == str2[j]) & (i==j):
                    str1[i]="_"
                    str2[j]="_"
                else:
                    str1[i]=str1[i]
                    str2[j]=str2[j]
                j+=1
            i+=1 
    elif (len(str2)-len(str1)==9) and (((''.join(str2)).find(''.join(str1)))==-1):
        str1=list('_________'+''.join(str1))
        for i in range(len(str1)):
            for j in range(len(str2)):
                if (str1[i] == str2[j]) & (i==j):
                    str1[i]="_"
                    str2[j]="_"
                else:
                    str1[i]=str1[i]
                    str2[j]=str2[j]
                j+=1
            i+=1
    elif (len(str2)-len(str1)==10) and (((''.join(str2)).find(''.join(str1)))==-1):
        str1=list('__________'+''.join(str1))
        for i in range(len(str1)):
            for j in range(len(str2)):
                if (str1[i] == str2[j]) & (i==j):
                    str1[i]="_"
                    str2[j]="_"
                else:
                    str1[i]=str1[i]
                    str2[j]=str2[j]
                j+=1
            i+=1            
    #new Line2    
    elif ((''.join(str1)).find(''.join(str2)))==10:
        str2=list('__________'+''.join(str2))
        for i in range(len(str1)):
            for j in range(len(str2)):
                if (str1[i] == str2[j]) & (i==j):
                    str2[j]="_"
                    str1[i]="_"
                else:
                    str2[j]=str2[j]
                    str1[i]=str1[i]
    return [''.join(str1),''.join(str2)]

def percent(lst):
    # Percent calculation logic (placeholder)
    return 100

# App title and description
st.markdown('<h1 class="title">MPN and SE_PART Comparison App</h1>', unsafe_allow_html=True)
st.write("Upload an Excel file containing 'MPN' and 'SE_PART' columns to compare their values.")

uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")

if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file)

        if 'MPN' not in df.columns or 'SE_PART' not in df.columns:
            st.error("The uploaded file must contain 'MPN' and 'SE_PART' columns.")
        else:
            df['MPN_NAN'] = df['MPN'].astype(str).apply(nonalpha)
            df['SE_PART_NAN'] = df['SE_PART'].astype(str).apply(nonalpha)
            df['SE_PART_NAND'] = df['SE_PART_NAN'].astype(str).apply(nonalphadot)
            df['MPN_NUMERIC'] = df['MPN_NAN'].apply(numeric)
            df['SE_PART_NUMERIC'] = df['SE_PART_NAN'].apply(numeric)
            df['MPN_Compare'] = df['MPN'].astype(str).apply(nonalpha)
            df['SE_PART_Compare'] = df['SE_PART'].astype(str).apply(nonalpha)
            df['LEN_MPN'] = df['MPN_NAN'].apply(leng)
            df['LEN_SE_PART'] = df['SE_PART_NAN'].apply(leng)
            df['merg_list'] = df[['MPN_Compare', 'SE_PART_Compare']].values.tolist()
            df['merg_list'] = df['merg_list'].apply(compare)
            df['Percent'] = df['merg_list'].apply(percent)

            df[['MPN_Compare', 'SE_PART_Compare']] = pd.DataFrame(df.merg_list.tolist(), index=df.index)

            st.success("Comparison completed!")
            st.dataframe(df)  # Display the DataFrame

            # Create an in-memory Excel file
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df.to_excel(writer, index=False, sheet_name='Comparison Results')
            output.seek(0)

            st.download_button(
                label="Download Result",
                data=output,
                file_name="compare_Done.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

    except Exception as e:
        st.error(f"An error occurred: {e}")
