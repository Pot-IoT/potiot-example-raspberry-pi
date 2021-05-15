from potiot import potiot_upload


# Change to your device ID
device_id = 'bb2a153f-xxxx-xxxx-xxxx-40aa25189859'
# Change to your private key
private_key = 'xxxxxxxxJ8VAWDKvzQXJnaUeem6xYH4u72XcbZeSg7tKTUPBv7pdc6fBoMJJnN1aPQLIELPgTOZaWsOaQKQUHWwYmQWIRrqftX9DGvw02LA2Jb7ZT6yTZn4FLBXOH8z7'
# Change to the type of the file to be uploaded
file_type = 'csv'
# Change to path of the file to be uploaded
file_path = 'test.csv'


res = potiot_upload(device_id, private_key, file_type, file_path)

print(res) # 200 --> Upload OK, Otherwise an error code
