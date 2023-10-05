from flask import Flask, jsonify, request
import numpy as np
import streamlit as st
from streamlit_chat import message
import regex as re
app = Flask(_name_)


@app.route("/get_request", methods=["GET"])
def chatbot():
    response_api(message)
    user_input()
    return message


st.title("OfferFeast")


def response_api(message):
    expected_greet = ['hi', 'hello', 'how', 'hey']
    ending_great = ['thank', 'thanks', 'happy', 'bye', 'good day', 'goodday', 'thankyou']
    credit_offers = ['credit', 'credit_card_offers', 'all_offers']
    card_offer_on_apparel = ['clothes', 'clothing', 'dress', 'garments', 'ajio', 'tatcliq']
    card_offer_on_Groceries = ['bigbasket', 'licious', 'groceries', 'supermarket']
    card_offer_on_travel = ['airport', 'airfield', 'runway', 'air station', 'heliport', 'cabs', 'bus']
    card_offer_on_electronics = ['smartphones', 'gadgets', 'electronics', 'croma', 'vijay', 'mobile']
    card_offer_on_dining = ['restaurant', 'hotel', 'cafe', 'cafeteria', 'bar', 'coffeehouse', 'dining', 'tea']
    card_offer_on_entertainment = ['book my show', 'pvr', 'movie', 'movies']
    reward_offer_on_cards = ['rewards', 'cashback', 'creditpoint', 'reward']
    info = message.split(" ")
    for str in info:
        is_expected_great_present = np.any([str in i for i in expected_greet])


        if is_expected_great_present == True:
            if str in expected_greet:
                return "Hi, I am Hsbc OfferFest Chatbot, How may I help you?"

        is_ending_great_present = np.any([str in i for i in ending_great])
        if is_ending_great_present == True:
            if str in ending_great:
                return "Thanks for enquiring us on our HSBC products, Have a nice day!"

    if is_expected_great_present == False and is_ending_great_present == False:

        info = message.split(" ")
        for data in info:
            print(data)
            if data in credit_offers:
                return """Sure, The currently available Credit card offers are as below:
                            *HSBC Cashback Credit Card:
                            -10% accelerated cashback on all dining, food delivery and grocery spends (capped up to INR1,000 per billing cycle)
                            -1.5% unlimited cashback on all other spends (exclusions apply)*
                            -4 complimentary domestic lounge visits per year (1 per quarter)
                            -Annual membership fees of INR999 will be reversed if your total annual spend exceeds INR200,000
                            *HSBC Visa Platinum Credit Card:
                            -Nil joining and annual fees
                            -10% cashback up to INR2,000 on all transactions made within first 30 days of card issuance
                            -2 reward points for every INR150 spent
                            -5X Rewards on subsequent purchases made after crossing spend amount of INR400,000 in an anniversary year up to a maximum 15000 accelerated reward points.
                            -Fuel surcharge waiver:
                            -Air miles conversion on InterMiles, British Airways and Singapore Airlines
                            -Discounts on movies, flights, restaurants and more
                            *HSBC Smart Value Credit Card:
                            -Nil joining and annual fees
                            -10% cashback up to INR1,000 on all transactions made within first 30 days of card issuance
                            -3X Rewards on online, dining & telecom spends
                            -Attractive Instalment plans at 10.99% per annum for EMI products booked within first 90 days of card issuance
                            -Fuel surcharge waiver
                            -Complete your credit card application online & win a BookMyShow e-Gift voucher worth INR250.
                            *HSBC Premier Mastercard© Credit Card:
                            -Nil joining and annual fees
                            -Airport lounge access
                            -Discounted green fees and dedicated 24-hour golf concierge service
                            -2 Reward points for every INR100 spent
                            -Fuel surcharge waiver
                            -Online fraud protection and lost card liability
                            -Air miles conversion on InterMiles, British Airways and Singapore Airlines"""
            elif data in card_offer_on_travel:
                return """ Sure The available card offers on Travel are as below:
                            Goibibo offer:
                            *Travel category Offer
                            -Minimum transaction -INR5,000
                            -Coupon code - GOHSBC
                            -Domestic flights - 12% off (up to INR1,500)
                            *Domestic Hotels:
                            -Minimum transaction -INR 2000
                            -Coupon code - GOHSBC
                            -offers - 15% off (up to INR5,000)
                            *International Flights:
                            -Minimum transaction -INR10,000
                            -Coupon code - GOHSBCINT
                            -International Flights - 10% off (up to INR5,000)
                            *International Hotels:
                            -15% off on selected hotels;
                            -10% off on all the other hotels (up to INR20,000)
                            -coupon code - GOHSBCINT
                            *Outstation Cabs:
                            -10% off (up to INR500)
                            -Min transaction: INR2,000
                            -coupon code - GOHSBC
                            *Bus bookings:
                            -8% off (up to INR500)
                            -INR500	GOHSBC"""
            elif data in card_offer_on_electronics:
                return """ Sure The available card offers on Electronics are as below:
                        *Vijay Sales:
                        -7.5% instant discount up to INR 7,500 at Vijay Sales stores and website, on using Instant EMI facility.
                        -T&C apply: This link will open in a new window
                        Valid on HSBC Credit Card Instant EMI payment options till 30 September 2023.
                        *Croma:
                        -Save up to INR 7,500 on a wide range of appliances & electronic gadgets on Saturdays & Sundays!
                        -T&C apply:
                        Valid once per card per month using HSBC Credit Cards till 30 September 2023."""
            elif data in card_offer_on_dining:
                return """ Sure The available card offers on Dining are as below
                            *Eazydiner:
                            -Up to 30% off  using HSBC Credit & Debit Cards
                            -Valid on both HSBC Credit & Debit Cards till 30 September.
                            *Qmin app:
                            -From experimental dinners to 5-course indulgence
                            -Experience signature classics and 5-course spreads at home! Use your HSBC credit or debit card to order via Qmin and enjoy 25% instant savings.
                            -25% instant discount (minimum order: INR1,500, excluding taxes)
                            -Use promo code: HSBC25,
                            -Offer valid on every order from 1 July 2023 to 30 September 2023,
                            -View participating hotels and menus on www.qmin.co.in.
                           * Zomato 
                            -Now enjoy exciting offers on Zomato dining & food delivery with your HSBC Card.
                            -Valid on both HSBC Credit & Debit Cards till 30 September.
                            *How to place your order:
                            -Call 1 800 266 7646 (toll-free) to place your order.
                            -If you are in Mumbai, New Delhi, Bengaluru, Chennai, Kolkata, Jaipur, Lucknow or Pune, you can also place your order via Qmin app.
                            -When you place the order, tell the agent you're using the HSBC offer and quote promo code HSBC25 (or enter the promo code on the app payment page).
                            -After placing your order, you'll receive a payment link on your mobile (with discounted amount already applied). Make the payment using your HSBC card.
                            -Order will be delivered once payment is confirmed. Please note, cash / card on delivery is not available."""
            elif data in card_offer_on_apparel:
                return """Sure The available card offers on Travel are as below
                        *Ajio:
                        -Offer details
                        -Additional 10% instant discount on a minimum transaction of INR2,499 on Tuesdays
                        -Offer period: 4 July 2023 to 26 September 2023
                        -Maximum discount – INR1000 per month
                        -Offer can be availed once per month on Tuesdays
                        *Tata Cliq
                        -Shop for your favourites online at Tata CLiQ
                        -Shop for your favourites, guilt-free, on Tata CLiQ at up to 15% discount with your HSBC Credit Card & Debit Card across apparel and more.
                        -Offer details for all customers:
                        -Up to 15% instant discount on Thursdays (once a month)
                        -Valid on HSBC Credit & Debit Cards
                        -Valid on HSBC Credit Card EMI transactions also
                        -Promo code HSBCLUX will not be valid during Tata CLiQ Luxury EOSS & other tactical Sale offers which are live on Tata CLiQ platforms as offers cannot be clubbed.
                        -Offer Period: 6 July 2023 to 26 September 2023 on Thursdays
                        -Platform	Instant discount	Minimum transaction amount	Maximum discount	Conditions	Promo code	Offer valid on payment using
                        Tata CliQ
                        -15% off	INR1,000	INR500	Valid once a month, every Thursday	HSBC500	All HSBC Credit & Debit Cards
                        -Tata CLiQ Palette^	15% off	INR1,000	INR300	Valid once a month, every Thursday	HSBCPAL300	All HSBC Credit & Debit Cards
                        -Tata CliQ Luxury*	10% off	Not applicable	INR5000	Valid once a month, every Thursday	HSBCLUX	All HSBC Credit & Debit Cards
                        *on select products available on Tata CliQ Luxury website and mobile app
                        -Click hereClick here This link will open in a new window to download the ^Tata CLiQ Palette Mobile App
                        -Additional offer for HSBC Premier Mastercard® Credit Cardholders:
                        -15% instant discount on Tata CLiQ Luxury category (once a month on any day of the week)
                        -Additional offer valid on payment using HSBC Premier Mastercard Credit Card only
                        -Promo code HSBCPR will not be valid during Luxury EOSS offer in January 2023 on Luxury Platform
                        -Offer Period: 1 July 2023 to 30 September 2023
                        -Platform	Instant discount	Minimum transaction amount	Maximum discount	Conditions	Promo code	Offer valid on payment using
                        -Tata CLiQ Luxury Premier Card Offer*	15% off	Not applicable	INR 10000	Valid once a month, any day of the week	HSBCPR	Only HSBC Premier Mastercard Credit Card
                        *on select products available on Tata CliQ Luxury website and mobile app
                        -Offer will be valid on Equated Monthly Installment (EMI) transactions in c"""
            elif data in card_offer_on_Groceries:
                return """*bigbasket 
                -10% off up to INR250 on bigbasket minimum order of INR2,000
                -Flat INR50 off on BB Now minimum order of INR600
                Licious
                -10% off up to INR150 once per month
                -Offer valid on all days of the week!
                -Minimum order value - INR 600
                -T&C applyT&C apply This link will open in a new window
                -Valid on HSBC Credit Cards till 30 September 2023.
                """
            elif data in card_offer_on_entertainment:
                return """*PVR
                -Get 10% off on food and beverages, every day, every time!
                -T&C apply
                -Valid on both HSBC Credit & Debit Cards till 30 September.
                *BookMyShow 
                -Buy-one-get-one-free offer on movie tickets booked on Saturdays
                -Valid once per card per month using HSBC Credit Cards till 30 September 2023.
                """
            elif data in reward_offer_on_cards:
                return """The HSBC Rewards Programme helps you get more out of your money every time you shop.
                -HSBC Classic Cardholders will earn 1 Reward point for every purchase of Rs. 250
                -HSBC Gold Cardholders will earn 1 Reward point for every purchase of Rs. 100
                -HSBC Smart Value Card Cardholders will earn 1 Reward point for every purchase of Rs. 100
                -HSBC Platinum Credit Cardholders will earn 2 Reward points for every purchase of Rs. 150
                -HSBC Premier Credit Cardholders will earn 2 Reward points for every purchase of Rs. 100
                """

            else:
                return """Sorry, I couldn't find any offers for that category.
                Please type from any of the below offers categories:
                1.Credit card offers - credit
                2.Travel     - travel
                3.Electronics   -gadgets
                4.Apparel & accessories  - clothes
                5.Groceries        - groceries
                6.Dining  - coffee
                7.Entertainment -movie
                8. Rewards & Credit - rewards
                """

    return message


def user_input():
    message = st.text_input("Enter your prompt: ")
    # message = request.args.get('message')
    print(message)

    return message


if 'generate' not in st.session_state:
    st.session_state['generate'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

user_text = user_input()

if user_text:
    output = response_api(user_text)
    st.session_state.generate.append(output)
    st.session_state.past.append(user_text)

if st.session_state['generate']:
    for i in range(len(st.session_state['generate']) - 1, -1, -1):
        message(st.session_state["past"][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["generate"][i], key=str(i))

if _name_ == "_main_":
    app.run()
