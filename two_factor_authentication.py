 
# two_factor_authentication.py

import pyotp

def enable_2fa(username):
    user = users.get(username)
    if user:
        totp = pyotp.TOTP(pyotp.random_base32())
        user['otp_secret'] = totp.secret
        return f'Two-Factor Authentication enabled. OTP Secret: {user["otp_secret"]}'
    else:
        return 'User not found.'

def login_2fa(username, otp_code):
    user = users.get(username)
    if user and 'otp_secret' in user:
        totp = pyotp.TOTP(user['otp_secret'])
        if totp.verify(otp_code):
            return 'Login successful with Two-Factor Authentication!'
        else:
            return 'Invalid OTP.'
    else:
        return 'User not found or Two-Factor Authentication not enabled.'
