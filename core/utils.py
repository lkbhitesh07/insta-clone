# from crum import get_current_user

# #to save currently loggedin user by model itself
# def auto_save_current_user(obj):
#     user = get_current_user()
#     if user and not user.pk: #sometimes user gets deleted from DB but is their in request or session so that's why we are doing this check.
#         user = None
#     if not obj.pk: # Here we are doing this because until the super method below is not run we will not get any pk because the model is still not created.
#         obj.user = user # as we have done Post.user ediatable = False , so now from this it will automatically take logedin user.