def get_user_by_id(user_model, id):
    user_object = None

    try:
        # Using the get method to retrieve the user by id
        user_object = user_model.objects.get(id=id)
    except Exception:
        pass

    if not user_object:
        try:
            # Using the query filter to retrieve the user by id
            user_object = user_model.query.filter_by(id=id).one()
        except Exception:
            pass

    if user_object is None:
        raise ValueError(f'User not found for the given ID: {id}')

    return user_object
