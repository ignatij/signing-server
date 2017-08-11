def handle_upload_files(s, f):
	with open(s + str(f).replace(' ', ''), 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)

def get_user_string(user):
	return 'users/' + user.username + '/'

def get_plain_string(user):
	return get_user_string(user) + 'plain/'

def get_signed_string(user):
	return get_user_string(user) + 'signed/'

def get_verified_string(user):
	return get_user_string(user) + 'verify/'

def get_private_key_location(user):
	return get_user_string(user) + 'private.pem'

def get_public_key_location(user):
	return get_user_string(user) + 'public.pem'