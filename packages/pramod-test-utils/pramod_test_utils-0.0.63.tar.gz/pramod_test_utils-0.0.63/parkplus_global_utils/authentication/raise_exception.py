def raise_exception(err, django_exception):
    if django_exception:
        from rest_framework import exceptions
        raise exceptions.AuthenticationFailed({"status": err[0], "message": err[1]})
    else:
        raise Exception(err[1])