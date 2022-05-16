from accounts.actions import UserAction, PerfileAction


def create_user(**kwargs):
	action = UserAction()
	age = kwargs.get('age')
	exist = False
 
	user = action.get(**{'username': kwargs.get('username')})
	if not user:
		kwargs.pop('age')
		user = action.create(**kwargs)

		# Create perfil
		perfil = {
			'age': age,
			'user': user
		}
		action = PerfileAction()
		action.create(**perfil)
	else:
		exist = True
		
	return exist