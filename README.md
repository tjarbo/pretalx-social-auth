# Single-Sign-On plugin for pretalx

> [!CAUTION]
> This plugin is still under heacy development and releases might require the usage of unreleased pretalx versions.

This is a plugin for [pretalx](https://github.com/pretalx/pretalx). It provides an integration with [Python Social Auth](https://github.com/python-social-auth/social-core), allowing users to log in with third-party services. It is originally based on [social_django](https://github.com/python-social-auth/social-app-django) from the Python Social Auth project, but with the removal of deprecated features and the addition of pretalx-specific settings.

Due to how Social Auth is configured with API keys in `settings.py`, this **doesn't support configuring providers (backends) on a per-event basis**. This means particular care should be taken where custom event domains are in use, as some providers require a different API key per domain (or adding valid redirect URLs).


![Screenshots of pretalx orga login screen and CFP account step with extra providers](img/login_screenshots.png)

## 🚀 Installation

As long as no packages on pypi are offered, please use the following command to install the plugin. It is required to install the package into the same (virtual) environment as pretalx, so that pretalx can auto detect the plugin.

```sh
# Install the latest development version
python -m pip install git+https://github.com/tjarbo/python-social-auth.git

# Install a specific release. Check releases page on GitHub.
python -m pip install git+https://github.com/tjarbo/python-social-auth.git@v0.0.0
```

## Configuration

In your `pretalx.cfg` file, add all the auth backends you need as a comma-separated list. Then, add the backend-specific settings to the `[plugin:pretalx_social_auth]` section. You can find the backend name and required settings in the [python-social-auth documentation](https://python-social-auth.readthedocs.io/en/latest/backends/index.html).

#### Example:

```ini
[authentication]
additional_auth_backends=social_core.backends.open_id_connect.OpenIdConnectAuth

[plugin:pretalx_social_auth]
SOCIAL_AUTH_OIDC_OIDC_ENDPOINT =https://oidc.idp.local
SOCIAL_AUTH_OIDC_KEY = 'client_id'
SOCIAL_AUTH_OIDC_SECRET = 'client_secret'
```

## FAQ

### What about `django-allauth`?
I initially looked into using [django-allauth](https://github.com/pennersr/django-allauth) instead, which allows configuring providers in the database on a per-site basis, but it also replaces the full auth model, so would be more difficult to make into a plugin!

# Contrib