"""
URL patterns for the views included in ``django.contrib.auth``.

Including these URLs (via the ``include()`` directive) will set up the
following patterns based at whatever URL prefix they are included
under:

* User login at ``login/``.

* User logout at ``logout/``.

* The two-step password change at ``password/change/`` and
  ``password/change/done/``.

* The four-step password reset at ``password/reset/``,
  ``password/reset/confirm/``, ``password/reset/complete/`` and
  ``password/reset/done/``.

The default registration backend already has an ``include()`` for
these URLs, so under the default setup it is not necessary to manually
include these views. Other backends may or may not include them;
consult a specific backend's documentation for details.

"""

from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = patterns('',
	url(r'^activate/(?P<activation_key>\w+)/$', 'registration.views.activate'),
	url(r'^login/$', auth_views.login,
		{'template_name': 'registration/login.html'}),
	url(r'^logout/$', auth_views.logout,
		{'template_name': 'registration/logged_out.html'}),
	url(r'^password/change/$', auth_views.password_change,
		{'template_name': 'registration/password_change_form.html',
		'post_change_redirect': 'done'}),
	url(r'^password/change/done/$', auth_views.password_change_done,
	 	{'template_name': 'registration/password_change_done.html'}),
	url(r'^password/reset/$', auth_views.password_reset,
		{'template_name': 'registration/password_reset.html',
		'from_email': 'staff@openart.com'}),
	url(r'^password/reset/done/$', auth_views.password_reset_done,
		{'template_name': 'registration/password_reset_done.html'}),
	url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
		auth_views.password_reset_confirm,
		{'post_reset_redirect': '/accounts/password/reset/complete/'}),
	url(r'^password/reset/complete/$',TemplateView.as_view(template_name='registration/password_reset_complete.html')),
    url(r'^register/$', 'registration.views.register'),
    url(r'^register/complete/$',TemplateView.as_view(template_name='registration/registration_complete.html')),


    url(r'^profile/$', 'registration.views.profile'),
)
