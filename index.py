import streamlit as st
from datetime import datetime
from streamlit_option_menu import option_menu
import requests


import google.generativeai as genai






st.set_page_config(
        page_icon="media\logo3.png",
        page_title="All in one Calualtor | app",
        layout="wide"

        
        
            )







# CSS styling for the Streamlit app
page_bg_img = f"""
<style>
[data-testid="stSidebar"] > div:first-child {{
    background-repeat: no-repeat;
    background-attachment: fixed;
        background-color: rgb(2, 48, 71);
}}

.st-emotion-cache-aj5vta {{
    width: 661.333px;
    position: relative;
    margin-bottom: 13px;
}}

.st-emotion-cache-1gv3huu {{
    position: relative;
    top: 2px;
    background-color: #000;
    z-index: 999991;
    min-width: 244px;
    max-width: 550px;
    transform: none;
    transition: transform 300ms, min-width 300ms, max-width 300ms;
}}

.st-emotion-cache-1jicfl2 {{
    width: 100%;
    padding: 4rem 1rem 4rem;
    min-width: auto;
    max-width: initial;

}}


.st-emotion-cache-4uzi61 {{
    border: 1px solid rgba(49, 51, 63, 0.2);
    border-radius: 0.5rem;
    padding: calc(-1px + 1rem);
    background: rgb(240 242 246);
    box-shadow: 0 5px 8px #6c757d;
}}

.st-emotion-cache-1vt4y43 {{
    display: inline-flex;
    -webkit-box-align: center;
    align-items: center;
    -webkit-box-pack: center;
    justify-content: center;
    font-weight: 400;
    padding: 0.25rem 0.75rem;
    border-radius: 0.5rem;
    min-height: 2.5rem;
    margin: 0px;
    line-height: 1.6;
    color: inherit;
    width: auto;
    user-select: none;
    background-color: #ffc107;
    border: 1px solid rgba(49, 51, 63, 0.2);
}}

.st-emotion-cache-qcpnpn {{
    border: 1px solid rgb(163, 168, 184);
    border-radius: 0.5rem;
    padding: calc(-1px + 1rem);
    background-color: rgb(38, 39, 48);
    MARGIN-TOP: 9PX;
    box-shadow: 0 5px 8px #6c757d;
}}


.st-emotion-cache-15hul6a {{
    user-select: none;
    background-color: #ffc107;
    border: 1px solid rgba(250, 250, 250, 0.2);
    
}}

.st-emotion-cache-1hskohh {{
    margin: 0px;
    padding-right: 2.75rem;
    color: rgb(250, 250, 250);
    border-radius: 0.5rem;
    background: #000;
}}

.st-emotion-cache-12pd2es {{
    margin: 0px;
    padding-right: 2.75rem;
    color: #f0f2f6;
    border-radius: 0.5rem;
    background: #000;
}}
</style>
"""




# Custom CSS to style the BMI result box
st.markdown("""
    <style>
.bmiresult {
    font-family: Arial, sans-serif;
    background-color: #ffffff;
    border: 2px solid #ddd;
    border-radius: 8px;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    text-align: center;
    width: 300px;
    HEIGHT: 328PX;
    margin: auto;
}

.bmiresult h1 {
    margin: 0 0 10px;
    color: #333;
    font-size: 34px;
}

    .bmiresult h3 {
        margin: 0;
        color: #007BFF;
        font-size: 2em;
    }

    .bmiresult p {
        margin-top: 10px;
        color: #333;
    }
    </style>
""", unsafe_allow_html=True)


# Custom CSS to style the age result box
st.markdown("""
    <style>
.ageresult {
    font-family: Arial, sans-serif;
    background-color: rgb(250, 250, 250);
    border: 2px solid #ddd;
    border-radius: 8px;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    text-align: center;
    width: 300px;
    HEIGHT: 242PX;
    margin: auto;
}
.ageresult h1 {
    margin: 0 0 10px;
    color: #333;
    font-size: 34px;
}

.ageresult h3 {
    margin: 0;
    color: #007BFF;
    font-size: 4em;
}

.ageresult p {
        margin-top: 10px;
        color: #333;
    }
    </style>
""", unsafe_allow_html=True)

# Add the custom CSS for curancy styling
st.markdown("""
    <style>
.currency-result {
    text-align: center;
    margin: 20px;
    padding: 20px;
    border: 2px solid #f0f0f0;
    border-radius: 10px;
    background-color: #FAFAFA;
    /* height: 436px; */
    margin-top: 85px;
}
        .currency-result h1 {
            font-size: 34px;
            margin-bottom: 20px;
        }
        .currency-result .flag-container {
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .currency-result img {
            margin: 0 10px;
        }
        .currency-result .to-text {
            font-size: 18px;
            margin: 0 10px;
        }
    .currency-result h3 {
    font-size: 27px;
    margin-top: 20px;
    color: #00ACC1;
}
    </style>
""", unsafe_allow_html=True)





# Apply CSS styling to the Streamlit app
st.markdown(page_bg_img, unsafe_allow_html=True)

# Function to calculate BMI
def calculate_bmi(weight, height):
    if height > 0:
        bmi = weight / (height ** 2)
        return bmi
    else:
        return None
    

# Function to categorize BMI
def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    
    elif bmi>30.0:
        return "Obesity"




genai.configure(api_key="AIzaSyBX9BFeAk8HcMmWSuhh0xR_4CnrtEGrHok")

model = genai.GenerativeModel('gemini-pro')

def generate_bmi_feedback(bmi_value):
    prompt = f"""
    You are provided with the following Body Mass Index (BMI) value:

    BMI Value: {bmi_value}

    Your task is to:
    1. Analyze the BMI value and categorize it into one of the following ranges:
        - Underweight: BMI < 18.5
        - Normal weight: 18.5 ≤ BMI < 24.9
        - Overweight: 25 ≤ BMI < 29.9
        - Obesity: BMI ≥ 30
    2. Provide a detailed comment on what the BMI value indicates about an individual's health based on the category it falls into.
    3. Offer recommendations or tips for maintaining or improving health based on the BMI category.

    Ensure that:
    - The comments are clear and informative.
    - The recommendations are practical and relevant to the BMI category.
    - The feedback is encouraging and supportive, aiming to educate and motivate the individual.

    Provide your response in the following structure:

    **BMI Category:**
    [Specify the category based on the BMI value]

    **Health Comment:**
    [Provide a detailed comment about the individual's health]

    **Recommendations:**
    [Offer practical tips or recommendations based on the BMI category]
    """
    response = model.generate_content(prompt)
    return response




    





def home_page():


    # Display the description using Markdown with HTML support
    st.markdown("""
        <h1>All-in-One Calculator App</h1>
        <div class="description">
            <p>Welcome to our versatile app, designed to simplify your daily calculations with a user-friendly interface. This app integrates three essential tools:</p>
            <ul>
                <li><strong>BMI Calculator</strong>: Input your weight and height to calculate your Body Mass Index (BMI) instantly. This tool provides immediate results and categorizes your BMI to help you monitor your health and fitness goals.</li>
                <li><strong>Currency Converter</strong>: Convert amounts between various currencies with live exchange rates. Whether you're traveling or managing international transactions, this feature offers accurate and up-to-date currency conversions.</li>
                <li><strong>Age Calculator</strong>: Enter your date of birth to determine your exact age. This handy tool is perfect for calculating age-related milestones, planning events, or keeping track of personal information.</li>
            </ul>
            <p>Enjoy a seamless and interactive experience with all these functions combined in one easy-to-use app. Simplify your life with efficient and accurate calculations at your fingertips.</p>
        </div>
    """, unsafe_allow_html=True)




with st.sidebar:
    st.image("media\logo3.png", use_column_width=True)


    # Adding a custom style with HTML and CSS
    st.markdown("""
        <style>
            .custom-text {
                font-size: 28px;
                font-weight: bold;
                text-align: center;
                color:#ffc107
            }
            .custom-text span {
                color: #04ECF0; /* Color for the word 'Insights' */
            }
        </style>
    """, unsafe_allow_html=True)

    # Displaying the subheader with the custom class
    st.markdown('<p class="custom-text">All in  <span>One</span> Calculator</p>', unsafe_allow_html=True)



    # HTML and CSS for the button
    github_button_html = """
    <div style="text-align: center; margin-top: 50px;">
        <a class="button" href="https://github.com/Salman7292" target="_blank" rel="noopener noreferrer">Visit my GitHub</a>
    </div>

    <style>
        /* Button styles */
        .button {
            display: inline-block;
            padding: 10px 20px;
            background-color: #ffc107;
            color: black;
            text-decoration: none;
            border-radius: 5px;
            text-align: center;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .button:hover {
            background-color: #000345;
            color: white;
            text-decoration: none; /* Remove underline on hover */
        }
    </style>
    """

    # Display the GitHub button in the app
    st.markdown(github_button_html, unsafe_allow_html=True)
    
    # Footer
    # Footer content
 # HTML and CSS for the centered footer
    footer_html = """
    <div style="background-color:#023047; padding:10px; text-align:center;margin-top: 10px;">
        <p style="font-size:20px; color:#ffffff;">Made with ❤️ by Salman Malik</p>
    </div>
    """

    # Display footer in the app
    st.markdown(footer_html, unsafe_allow_html=True)




# Define the option menu for navigation
selections = option_menu(
    menu_title=None,  # No title for the menu
    options=['Home', "BMI Calculator",'Age Calculator',"Currency converter"],  # Options for the menu
    icons=['house-fill', "bi-activity",'bi-calendar',"bi-currency-exchange"],  # Icons for the options
    menu_icon="cast",  # Optional: Change the menu icon
    default_index=0,  # Optional: Set the default selected option
    orientation='horizontal',  # Set the menu orientation to horizontal
    styles={  # Define custom styles for the menu
        "container": {
            "padding": "5px 23px",
            "background-color": "#0d6efd",  # Background color (dark grey)
            "border-radius": "8px",
            "box-shadow": "0px 4px 10px rgba(0, 0, 0, 0.25)"
        },
        "icon": {"color": "#f9fafb", "font-size": "18px"},  # Style for the icons (light grey)
        "hr": {"color": "#0d6dfdbe"},  # Style for the horizontal line (very light grey)
        "nav-link": {
            "color": "#f9fafb",  # Light grey text color
            "font-size": "12px",
            "text-align": "center",
            "margin": "0 10px",  # Adds space between the buttons
            "--hover-color": "#0761e97e",  # Slightly lighter grey for hover
            "padding": "10px 10px",
            "border-radius": "16px"

        },
        "nav-link-selected": {"background-color": "#ffc107","font-size": "12px",},  # Green background for selected option
    }
)

# Check the selected option from the menu
if selections == 'Home':
    home_page()


elif selections =='BMI Calculator':
    bmi=0
    # Create two columns with custom widths
    col1, col2 = st.columns([2, 1])  # col1 will be twice as wide as col2

    with col1:
    
        # Create a form for the BMI Calculator
        with st.form("BMI Calculator") as BMI_PORTION:
            # Set the title of the form
            st.title("BMI Calculator")

            # Create input fields for weight and height
            weight = st.number_input("Enter your weight (kg):", min_value=0.0, format="%.2f")
            height = st.number_input("Enter your height (m):", min_value=0.0, format="%.2f")

            # Add a submit button
            submit_button = st.form_submit_button(label='Calculate BMI')

    with col2:

    # Calculate and display the BMI and its category after the form is submitted
        if submit_button:

            bmi = calculate_bmi(weight, height)
            if bmi is not None:
                category = categorize_bmi(bmi)
                st.markdown(f"""
                    <div class="bmiresult">
                        <h1>Calculated BMI</h1>
                        <h3>{bmi:.2f}</h3>
                        <p>Your BMI is considered {category}.</p>
                    </div>
                """, unsafe_allow_html=True)
        
            else:
                st.error("Please enter a valid height.")


    if bmi>0:
    
        st.title("What our App suggest for you!")
        result=generate_bmi_feedback(bmi)
        st.markdown(result.text)
        



       





elif selections == "Age Calculator":

    col1, col2 = st.columns([2, 1])  # col1 will be twice as wide as col2

    with col1:
                # Create a form for the BMI Calculator
        with st.form("Age Calculator") as age_PORTION:
            st.title("Age Calculator")

            # Create an input field for the date of birth
            dob = st.date_input("Enter your date of birth:", min_value=datetime(1900, 1, 1))
                        # Add a submit button
            submit_button = st.form_submit_button(label='Age Calculator')
    
    with col2:

        if submit_button:
            # Calculate age when the date of birth is provided
            if dob:
                today = datetime.today()
                
                age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
                st.markdown(f"""
                    <div class="ageresult">
                        <h1>Calculated Age</h1>
                        <h3>{age}</h3>
                    </div>
                """, unsafe_allow_html=True)
      
            else:
                st.warning("Please enter your date of birth.")



    



elif selections == "Currency converter":

    api_key_currency = "dd9e84bcd35aebf17189c39d"



    col1, col2 = st.columns([1, 1])  # col1 will be twice as wide as col2


    currency_dict = {
        "AFN": "AF",  # Afghanistan
        "PKR": "PK",  # Pakistan
        "USD": "US",  # United States
        "EUR": "EU",  # European Union
        "GBP": "GB",  # United Kingdom
        "JPY": "JP",  # Japan
        "INR": "IN",  # India
        "AUD": "AU",  # Australia
        "CAD": "CA",  # Canada
        "CHF": "CH",  # Switzerland
        "CNY": "CN",  # China
        "SEK": "SE",  # Sweden
        "NZD": "NZ",  # New Zealand
        "MXN": "MX",  # Mexico
        "SGD": "SG",  # Singapore
        "HKD": "HK",  # Hong Kong
        "NOK": "NO",  # Norway
        "KRW": "KR",  # South Korea
        "TRY": "TR",  # Turkey
        "RUB": "RU",  # Russia
        "ZAR": "ZA",  # South Africa
        "BRL": "BR",  # Brazil
        "TWD": "TW",  # Taiwan
        "DKK": "DK",  # Denmark
        "PLN": "PL",  # Poland
        "THB": "TH",  # Thailand
        "IDR": "ID",  # Indonesia
        "HUF": "HU",  # Hungary
        "ILS": "IL",  # Israel
        "CZK": "CZ",  # Czech Republic
        "AED": "AE",  # United Arab Emirates
        "SAR": "SA",  # Saudi Arabia
        "MYR": "MY",  # Malaysia
        "PHP": "PH",  # Philippines
        "RSD": "RS",  # Serbia
        "ARS": "AR",  # Argentina
        "CLP": "CL",  # Chile
        "COP": "CO",  # Colombia
        "PEN": "PE",  # Peru
        "VND": "VN",  # Vietnam
        "RWF": "RW",  # Rwanda
        "BHD": "BH",  # Bahrain
        "JOD": "JO",  # Jordan
        "KWD": "KW",  # Kuwait
        "OMR": "OM",  # Oman
        "QAR": "QA",  # Qatar
        "BND": "BN",  # Brunei
        "MUR": "MU",  # Mauritius
        "TND": "TN",  # Tunisia
        "LKR": "LK",  # Sri Lanka
        "BAM": "BA",  # Bosnia and Herzegovina
        "GEL": "GE",  # Georgia
        "KZT": "KZ",  # Kazakhstan
        "UAH": "UA",  # Ukraine
        "MZN": "MZ",  # Mozambique
        "ETB": "ET",  # Ethiopia
        "BWP": "BW",  # Botswana
        "NAD": "NA",  # Namibia
        "SYP": "SY",  # Syria
        "SDG": "SD",  # Sudan
        "MWK": "MW",  # Malawi
        "XAF": "XAF",  # Central African CFA Franc
        "XOF": "XOF",  # West African CFA Franc
        "XCD": "XCD",  # East Caribbean Dollar
        "XCU": "XCU",  # Copper (Commodity)
        "XAG": "XAG",  # Silver (Commodity)
        "XAU": "XAU",  # Gold (Commodity)
        "XDR": "XDR",  # Special Drawing Rights
        "BTC": "BTC",  # Bitcoin
        "ETH": "ETH"   # Ethereum
    }

    with col1:

        # Create a form for the Currency Converter
        with st.form("Currency converter") as Currency_PORTION:
            st.title("Currency converter")

            # Create input fields for amount, from currency, and to currency
            amount = st.number_input("Enter amount:", min_value=0.0, format="%.2f")
            from_currency = st.selectbox("From currency:", options=currency_dict.keys())
            to_currency = st.selectbox("To currency:", options=currency_dict.keys())

            # Add a submit button
            submit_button = st.form_submit_button(label='Converted Currency')

    with col2:

        if submit_button:
            source_flag = currency_dict[from_currency]
            target_flag = currency_dict[to_currency]

            url = f"https://v6.exchangerate-api.com/v6/{api_key_currency}/latest/{from_currency}"
            
            response = requests.get(url)

            if response.status_code == 200:

                data = response.json()  # Call the json() method to parse the JSON data
        
                conversion_rates=data["conversion_rates"]

                if to_currency in conversion_rates:
                    exchnage_rate=conversion_rates[to_currency]
                    Converted_amount=amount*exchnage_rate
                 

                    st.markdown(f"""
                        <div class="currency-result">
                            <h1> Converted Amount</h1>
                            <div class="flag-container">
                                <img src="https://flagsapi.com/{source_flag}/flat/64.png" width="64" height="64">
                                <span class="to-text">To</span>
                                <img src="https://flagsapi.com/{target_flag}/flat/64.png" width="64" height="64">
                            </div>
                            <h3>{Converted_amount} {to_currency}</h3>
                        </div>
                    """, unsafe_allow_html=True)


            else:
                st.write("Failed to retrieve data. Please check the API key or try again later.")



        






 


