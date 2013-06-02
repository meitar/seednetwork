from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from seednetwork.forms import SeedNetworkAuthForm

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'seednetwork.views.home', name='home'),
    url(r'^seedlibrary/', include('seedlibrary.urls')),

    url(r'^$', 'seednetwork.views.home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # user management
	(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name':'login.html', 'authentication_form':SeedNetworkAuthForm}),
	(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name':'logout.html', 'next_page':'/'}),
	(r'^accounts/profile/$', 'seednetwork.views_user.profile'),
	(r'^accounts/profile-edit/$', 'seednetwork.views_user.edit_profile'),

    (r'^accounts/new-user/$', 'seednetwork.views_user.new_user'),

	(r'^accounts/reset-password/$', 'django.contrib.auth.views.password_reset',
		 {'template_name':'password_reset.html',
		  'email_template_name':'password_reset_email.html'}),

	(r'^accounts/reset-password/done/$', 'django.contrib.auth.views.password_reset_done',
		 {'template_name':'password_reset_done.html'}),

	(r'^accounts/change-password/$', 'django.contrib.auth.views.password_change',
		 {'template_name':'password_change.html'}),

	(r'^accounts/change-password/done/$', 'django.contrib.auth.views.password_change_done',
		 {'template_name':'password_change_done.html'}),
)
