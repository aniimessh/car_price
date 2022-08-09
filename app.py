import streamlit as st
import pickle
model = pickle.load(open('RF_price_predicting_model.pkl','rb'))

def main():
    String = 'car Price Predictor'
    st.set_page_config(page_title=String, page_icon="🚗")
    st.title("Car Price Predictor 🚗")
    st.markdown("##### Are you planning to sell your car !?\n So let's try evulating the price... 🤖")
    st.image(
        "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpngimg.com%2Fuploads%2Fhyundai%2Fhyundai_PNG11233.png&f=1&nofb=1",
        width=200,
    )
    st.write('')
    st.write('')
    years = st.number_input('In which year car was purchased ?', 1990,2022,step=1,key='year')
    year_old = 2022-years

    Present_Price = st.number_input('What is the current ex-showroom price of the car ?  (In ₹lakhs)', 0.00, 50.00, step=0.5, key ='present_price')

    Kms_Driven = st.number_input('What is distance completed by the car in Kilometers ?', 0.00, 500000.00, step=500.00, key ='drived')

    Owner = st.radio("The number of owners the car had previously ?", (0, 1, 3), key='owner')

    Fuel_Type_Petrol = st.selectbox('What is the fuel type of the car ?',('Petrol','Diesel', 'CNG'), key='fuel')
    if(Fuel_Type_Petrol=='Petrol'):
        Fuel_Type_Petrol=1
        Fuel_Type_Diesel=0
    elif(Fuel_Type_Petrol=='Diesel'):
        Fuel_Type_Petrol=0
        Fuel_Type_Diesel=1
    else:
        Fuel_Type_Petrol=0
        Fuel_Type_Diesel=0

    Seller_Type_Individual = st.selectbox('Are you a dealer or an individual ?', ('Dealer','Individual'), key='dealer')
    if(Seller_Type_Individual=='Individual'):
        Seller_Type_Individual=1
    else:
        Seller_Type_Individual=0
    
    Transmission_Mannual = st.selectbox('What is the Transmission Type ?', ('Manual','Automatic'), key='manual')
    if(Transmission_Mannual=='Mannual'):
        Transmission_Mannual=1
    else:
        Transmission_Mannual=0

    if st.button("Estimate Price", key='predict'):
        try:
            Model = model  #get_model()
            prediction = Model.predict([[Present_Price, Kms_Driven, Owner, year_old, Fuel_Type_Diesel, Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Mannual]])
            output = round(prediction[0],2)
            if output<0:
                st.warning("You will be not able to sell this car !!")
            else:
                st.success("You can sell the car for {} lakhs 🙌".format(output))
        except:
            st.warning("Opps!! Something went wrong\nTry again")
if __name__ == '__main__':
    main()
