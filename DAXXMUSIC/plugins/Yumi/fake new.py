import requests
from pyrogram import Client
from pyrogram import filters
from DAXXMUSIC import app

# URL for generating fake user information
random_user_api_url = 'https://randomuser.me/api/'

# URL for generating test credit card information (example)
fake_credit_card_api_url = 'https://fakestoreapi.com/auth/generate'

@app.on_message(filters.command("fcc", prefixes="/"))
def generate_fake_user_and_cc(client, message):
    country_name = message.text.split("/fcc ", maxsplit=1)[1]
    
    # Call the RandomUser API to get fake user information for the specified country
    response_user = requests.get(f'{random_user_api_url}?nat={country_name}')
    
    if response_user.status_code == 200:
        user_info = response_user.json()['results'][0]
        # Extract user details
        first_name = user_info['name']['first']
        last_name = user_info['name']['last']
        email = user_info['email']
        country = user_info['location']['country']
        state = user_info['location']['state']
        city = user_info['location']['city']
        street = user_info['location']['street']['name']
        zip_code = user_info['location']['postcode']
        
        # Call the FakeStoreAPI to get fake credit card information
        response_cc = requests.get(fake_credit_card_api_url)
        
        if response_cc.status_code == 200:
            cc_info = response_cc.json()
            cc_number = cc_info['card']['number']
            cc_expiry = cc_info['card']['expiry']
            cc_cvc = cc_info['card']['code']
            
            # Reply with the generated fake user and credit card information
            message.reply_text(f"𝗡𝗔𝗠𝗘➪ {first_name} {last_name}\n\n𝗘𝗠𝗔𝗜𝗟➪ {email}\n\n𝗖𝗢𝗨𝗡𝗧𝗥𝗬➪ {country}\n\n𝗦𝗧𝗔𝗧𝗘➪ {state}\n\n𝗖𝗜𝗧𝗬: {city}\n\n𝗔𝗗𝗗𝗥𝗘𝗦𝗦:➪{street}\n\n𝗭𝗜𝗣 𝗖𝗢𝗗𝗘➪ {zip_code}\n\n𝗖𝗥𝗘𝗗𝗜𝗧 𝗖𝗔𝗥𝗗➪ {cc_number}\n\n𝗘𝗫𝗣𝗜𝗥𝗬➪ {cc_expiry}\n\n𝗖𝗩𝗖➪ {cc_cvc}")
        else:
            message.reply_text(f"Failed to generate fake credit card information.")
    else:
        message.reply_text(f"Failed to generate fake user information for {country_name}.")
