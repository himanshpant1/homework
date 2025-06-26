import pandas as pd

data = {
    'email': ['test@example.com', 'wrong.email', 'hello@site.org'],
    'phone': ['9876543210', '1234567890', '9123456789'],
    'name': ['Alice', 'Bob123', 'Charlie'],
    'pincode': ['123456', '56AB78', '400088'],
    'password': ['Pass123!', 'weak', 'Strong@123'],
    'date': ['2024-06-26', '26-06-2024', '2023-12-01']
}
df = pd.DataFrame(data)
df['valid_email'] = df['email'].str.match(r'^[\w\.-]+@[\w\.-]+\.\w+$')
df['valid_phone'] = df['phone'].str.match(r'^[6-9]\d{9}$')
df['name_is_alpha'] = df['name'].str.match(r'^[A-Za-z]+$')
df['valid_pincode'] = df['pincode'].str.match(r'^\d{6}$')
df['valid_password'] = df['password'].str.contains(r'[@#$%^&*!]')
df['valid_date'] = df['date'].str.match(r'^\d{4}-\d{2}-\d{2}$')
print(df)
