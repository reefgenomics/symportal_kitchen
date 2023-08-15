def get_user_by_id(user_model, id):
    return user_model.objects.get(id=id)
