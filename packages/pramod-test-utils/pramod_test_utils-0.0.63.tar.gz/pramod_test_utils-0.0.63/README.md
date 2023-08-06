## Add Module

Let us assume we want to add another module `mod1` to the package `parkplus_global_utils`

1. Create a folder `mod1` at path `parkplus_global_utils/`.
2. Add all of your code inside this folder.
3. Make sure to import in `mod1/__init__.py` whatever objects you want to be importable from package `mod1`.
4. Update the package version in `setup.py`.
5. Update the package wheel using `python setup.py bdist_wheel`.
6. Upload the package to pypi-server using ` twine upload dist/parkplus_global_utils-<version>-py3-none-any.whl --repository-url https://pypi-server.parkplus.io/ -u <user> -p <password>`.
7. Install the new version using `pip install --upgrade --extra-index-url https://pypi-server.parkplus.io/simple/ parkplus_global_utils
`.

```
>>> from parkplus_global_utils.cities import *
>>> cities_list()
```

## Authentication Package
Create a Package for global authentication

How to use:-
1. Make a separate file for creating an auth object
   For ex - 
   from parkplus_global_utils.authentication.utils import GenericAuth
   ```
   parkplus_auth = GenericAuth(client_id=<<your_client_id>>, client_secret=<<your_client_secret>>, x_api_key=<<your_x_api_key>>, 
   jwt_secret_key=<<your_jwt_secret_key>>, jwt_token_key=<<your_jwt_token_key>>)
   ```
2. After creating an auth_object we have four decorators user_authentication(Using Auth_Token), 
   service_authentication(Using X_API_KEY), client_authentication(ONLY CLIENT_ID AND CLIENT_SECRET) and user_or_client_authentication

3. We use these decorator according to the required authentication

```
    def post_(self, *args, **kwargs):
        if source == "b2c":
            self.post_b2c(*args, **kwargs)
        elif source == "parkplus-internal":
            self.parkplus_internal(*args, **kwargs)

    @parkplus_auth.user_authentication()
    def post_b2c(self, *args, **kwargs):
        pass

    @parkplus_auth.service_authentication()
    def parkplus_internal(self, *args, **kwargs):
        pass
```
